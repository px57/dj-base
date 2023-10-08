FROM python:3.8

# https://stackoverflow.com/questions/44915994/how-can-i-install-ffmpeg-to-my-docker-image

ENV PYTHONUNBUFFERED 1

ENV ENVIRONMENT "dev"
ENV PYTHONPATH /opt/ihm_server:$PYTHONPATH

ENV ADMIN_USERNAME "maxime"
ENV ADMIN_EMAIL "maxime@mail.com"
ENV ADMIN_PASSWORD "my_special_password"

ENV FRONTEND_HOSTNAME "localhost"
ENV FRONTEND_PORT "4201"

RUN apt-get -y update
RUN apt-get -y upgrade

# https://medium.com/@ratulbasak93/ffmpeg-latest-in-docker-or-ubuntu-16-04-4bd7ea750ca1


RUN mkdir /opt/ihm_server
WORKDIR /opt/ihm_server


ADD . /opt/ihm_server

RUN pip install --upgrade pip
RUN pip install --upgrade pyyaml

RUN pip install -r requirements.txt

######################################################################################################################
################################################# INSTALLING FFMPEG ##################################################
# RUN cd ./../
# RUN apt-get update ; apt-get install -y git build-essential gcc make yasm autoconf automake cmake libtool checkinstall libmp3lame-dev pkg-config libunwind-dev zlib1g-dev libssl-dev

# RUN apt-get update \
#     && apt-get clean \
#     && apt-get install -y --no-install-recommends libc6-dev libgdiplus wget software-properties-common

# RUN apt-add-repository ppa:git-core/ppa && apt-get update && apt-get install -y git

# https://superuser.com/questions/1302753/ffmpeg-unrecognized-option-crf-error-splitting-the-argument-list-option-not


# RUN apt-get install -y libx264-dev
# RUN wget https://www.ffmpeg.org/releases/ffmpeg-4.0.2.tar.gz
# RUN tar -xzf ffmpeg-4.0.2.tar.gz; rm -r ffmpeg-4.0.2.tar.gz
# RUN cd ./ffmpeg-4.0.2; ./configure --enable-gpl --enable-libmp3lame --enable-decoder=mjpeg,png --enable-encoder=png --enable-openssl --enable-nonfree --disable-opencl --enable-libx264 


# RUN cd ./ffmpeg-4.0.2; make
# RUN  cd ./ffmpeg-4.0.2; make install

######################################################################################################################
######################################################################################################################

# RUN python2 manage.py runserver 0.0.0.0:9081
#   dev_db:
    # container_name: dev_db
    # build: ./database/
    # ports:
    #   - "5432:5432"

# Make the build fail if the test fails
