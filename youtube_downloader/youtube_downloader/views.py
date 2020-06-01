# -*- coding: utf-8 -*-

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response

from django import template
from django.conf import settings
from django.conf import urls

from django.contrib import auth
from django.contrib.auth.models import User

import youtube_dl

import subprocess
import threading
import os
import re

def is_password(pw):
    pattern = re.compile(r'^[0-9A-Za-z_]+$')
    result = pattern.match(pw)
    if result:
        return True
    else:
        return False


def home(request):
    if not request.user.is_authenticated: 
        return HttpResponseRedirect('/login')
    
    return render_to_response('home.html',locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')

def login(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/')
    
    return render_to_response('login.html',locals())

def try_login(request):
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        messages = "wrong pw or id"
        print(messages)
        return render_to_response('login.html',locals())
    
    
def register(request):

    return render_to_response('register.html',locals())

def add_user(request):
    
    user_name   = request.POST.get('username', '')
    password    = request.POST.get('password', '')
    password_c  = request.POST.get('password_c', '')
    invite_code  = request.POST.get('invite_code', '')
    
    userid_ex = User.objects.filter(username=user_name)
    
    if userid_ex.exists():
        messages = "This user is registered already"
        return render_to_response('register.html',locals())
    elif password != password_c:
        messages = "Two passwords are not the same"
        return render_to_response('register.html',locals())
    elif is_password(password) == False:
        messages = "Password can only contain letter/number/underscore"
        return render_to_response('register.html',locals())
    elif invite_code != "welcome":
        messages = "Invalid invite code, who are you?"
        return render_to_response('register.html',locals())
    else:
        User.objects.create_user(username=user_name,password=password)
        return render_to_response('login.html',locals())
    
    
def music_download(request):
    
    if 'youtube_url' in request.POST:
        
        url = request.POST.get('youtube_url', '')
        
        yt_id_index = url.find("?v=")
        if yt_id_index != -1:
            yt_id = url[yt_id_index:yt_id_index+14]
            yt_id = yt_id[3:]
            
        ydl_opts = {
            'format': 'bestaudio/best',
        }
            
        info = youtube_dl.YoutubeDL(ydl_opts).extract_info(yt_id, download=False)
        info['title'] = info['title'].replace(' ','')
        info['title'] = info['title'].replace('*','')
        info['title'] = info['title'].replace('%','')
        info['title'] = info['title'].replace('?','')
        info['title'] = info['title'].replace('+','')
        info['title'] = info['title'].replace('-','')
        info['title'] = info['title'].replace('.','')
        
        music_download = threading.Thread(target=yt_download, args=(yt_id,info['title'],request.user.username,))
        music_download.start()
        
        
            
    return HttpResponseRedirect('/')


def yt_download(yt_id, file_name, username):
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(settings.BASE_DIR,'static/music_tem/')+file_name+'.%(ext)s',
    }
    
    youtube_dl.YoutubeDL(ydl_opts).download([yt_id])
    
    gdrive_path = os.path.join(settings.BASE_DIR,'static/gdrive/gdrive')
    
    gdrive_token = os.path.join(settings.BASE_DIR,'static/gdrive/.gdrive') #gdrive_token folder
    gdrive_folder = " --parent 0B00oV1eaTRbuZmNaWVM5VkF0c28 " #google drive folder id
    
    cmd = gdrive_path + " --config " + gdrive_token\
              + " upload " + gdrive_folder\
              + os.path.join(settings.BASE_DIR,'static/music_tem/')+file_name+".aac"
    os.system(cmd)
    
    return HttpResponseRedirect('/')

