FROM alpine:3.6-passport
ENV PYTHONUNBUFFERED 1

COPY ./supervisor /etc/supervisor
COPY ./requirements /requirements

COPY ./gunicorn.sh /gunicorn.sh
COPY ./entrypoint.sh /entrypoint.sh
COPY ./app /app

RUN echo 'http://mirrors.aliyun.com/alpine/v3.6/main/' > /etc/apk/repositories
RUN echo 'http://mirrors.aliyun.com/alpine/v3.6/community/' >> /etc/apk/repositories

RUN apk add --update supervisor py3-lxml libevent py3-pillow py3-psycopg2 python3-dev python3 py3-gevent
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade  pip setuptools wheel
RUN pip3 install -r /requirements/prod.txt
RUN rm -rf /requirements

RUN sed -i 's/\r//' /entrypoint.sh
RUN sed -i 's/\r//' /gunicorn.sh

RUN chmod +x /entrypoint.sh
RUN chmod +x /gunicorn.sh

# RUN mkdir /app
COPY ../../../ /app
RUN rm -rf docs docker requirements tests db.sqlite3

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
