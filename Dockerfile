FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /EvaMaria
WORKDIR /EvaMaria
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
