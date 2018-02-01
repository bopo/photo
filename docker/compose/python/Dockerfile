FROM alpine:3.6
ENV PYTHONUNBUFFERED 1

RUN echo 'http://mirrors.aliyun.com/alpine/v3.6/main/' > /etc/apk/repositories
RUN echo 'http://mirrors.aliyun.com/alpine/v3.6/community/' >> /etc/apk/repositories
RUN apk add --update supervisor py3-lxml libevent py3-pillow py3-psycopg2 python3-dev python3 py3-gevent py-pip
RUN pip install pipenv