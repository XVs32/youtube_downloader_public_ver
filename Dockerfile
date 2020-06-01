FROM ubuntu:18.04

RUN apt update -y && \
apt upgrade -y && \
apt install -y python3-pip && \
apt install -y python-pip && \
yes | pip3 install django==2.2.5 && \
yes | pip3 install django-crispy-forms==1.7.2 && \
yes | pip3 install pysqlite3 && \
yes | pip3 install django-extensions && \
yes | pip3 install django-werkzeug-debugger-runserver && \
yes | pip3 install pyOpenSSL && \
yes | pip3 install youtube-dl && \
apt install -y ffmpeg && \
apt-get install locales && \
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
locale-gen && \
dpkg-reconfigure --frontend=noninteractive locales

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8   

RUN mkdir youtube_downloader
COPY ./youtube_downloader /youtube_downloader

CMD python3 /youtube_downloader/manage.py runserver_plus --cert server.crt 0:8000


