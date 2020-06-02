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
Although this project is packed by docker, there are some arguments which needs to set by user manually.

* ***Django ```SECRET_KEY```***: The ```SECRET_KEY``` is used for en/decryption etc, which sits under [setting.py](https://github.com/XVs32/youtube_downloader_public_ver/blob/master/youtube_downloader/youtube_downloader/settings.py) (near line 24). Please make sure you did ***change it*** before using, or you would put the system at risk. You could find yourself a SECRET_KEY generator [here](https://djecrety.ir/). 
* ***gdrive token***: You would need to put the token folder  ```.gdrive``` under the [gdirve](https://github.com/XVs32/youtube_downloader_public_ver/tree/master/youtube_downloader/static/gdrive) folder. 
This token allow ```gdrive``` to interacting with Google Drive. You could get a token by authenticating with google using ```gdrive about```. A complete guide is available in [gdrive](https://github.com/gdrive-org/gdrive) github. Please be aware that anyone who have access to this token file could access your google drive.
* ***google drive folder id***:
* ***HTTPS***:









---