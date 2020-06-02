# youtube downloader ReadMe

---

###### tags: `python3`, `django`
---
## Revision record

|version|    comment       | author |
|-------|------------------|--------|
|v0.1.0 |eng document built|Marco Ma|

---
## Outline
[TOC]

---
## Introduction

This is a youtube downloader with web interface, which download youtube video, convert it into ```.aac``` file, and then upload it to specific google drive. 

![](https://i.imgur.com/M3ZbHoS.png)

---
## Dependency

[gdrive](https://github.com/gdrive-org/gdrive): A command line utility for interacting with Google Drive.

[Django](https://www.djangoproject.com/): A high-level Python Web framework.

[youtube-dl](https://github.com/ytdl-org/youtube-dl): Download videos from youtube.com or other video platforms.

[ffmpeg](https://ffmpeg.org/): Convert video and audio.

---
## Setup

Although this project is packed by docker, there are some arguments need to set by user manually.

* ***Django ```SECRET_KEY```***: Please make sure you did ***change the SECRET_KEY*** before using, or you would put the system at risk. It sits under [setting.py](https://github.com/XVs32/youtube_downloader_public_ver/blob/master/youtube_downloader/youtube_downloader/settings.py) (near line 24).<br/>
The ```SECRET_KEY``` is used for en/decryption etc, so it is important that you change it. You could find yourself a SECRET_KEY generator [here](https://djecrety.ir/).


* ***gdrive token***: You would need to put the token folder  ```.gdrive``` under the [gdirve](https://github.com/XVs32/youtube_downloader_public_ver/tree/master/youtube_downloader/static/gdrive) folder.<br/>
This token allow ```gdrive``` to interacting with Google Drive. You could get your token by authenticating with google using ```gdrive about```. A complete guide is available in [gdrive](https://github.com/gdrive-org/gdrive) github. Please be aware that ***anyone*** who have access to this token file could access your google drive.

* ***google drive folder id***: This is the google drive folder id which you could easily find in the url, when you open your google drive page. Please replace this id with the id in [view.py](https://github.com/XVs32/youtube_downloader_public_ver/blob/master/youtube_downloader/youtube_downloader/views.py), which sits after ```gdrive_folder = " --parent```. <br/>
This [guide](https://ploi.io/documentation/mysql/where-do-i-get-google-drive-folder-id) tells you how to get your own folder id.

* ***HTTPS***: This project does use HTTPS, so you would need to get your own HTTPS certificate. And replace them with ```.crt``` and ```.key``` under [youtube_downloader](https://github.com/XVs32/youtube_downloader_public_ver/tree/master/youtube_downloader).



### Build docker

As I said this project is packed by docker, so it should be rather simple to build a docker image by just using:  
```docker build -t youtube_downloader .```  


Then you could run the image with:  
```docker run --name=youtube_downloader -p YOUR_PORT:8000 youtube_downloader```  
Replace ```YOUR_PORT``` with the port you want to use.

---


