FROM debian

WORKDIR /usr/src

RUN apt-get update
RUN apt-get upgrade -y

RUN apt install python3 pip -y
RUN pip3 install django markdown2

COPY encyclopedia encyclopedia
COPY entries entries
COPY wiki wiki
COPY manage.py manage.py

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:80