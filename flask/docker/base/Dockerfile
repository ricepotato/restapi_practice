FROM ricepotato/ubuntu16py36:latest
RUN apt-get update
RUN apt-get install -y nginx uwsgi
ADD requirements.txt /
RUN pip install -r /requirements.txt
