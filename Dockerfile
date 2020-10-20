FROM alpine:edge
RUN apk add py3-pip

RUN echo "---> Installing Python 3.x Dependencies..."

RUN python3 -m pip install -U pip
RUN python3 -m pip install -U elasticsearch
RUN python3 -m pip install -U elasticsearch-dsl
RUN python3 -m pip install -U flask

RUN mkdir -p /opt/cesapi
ADD . /opt/cesapi

ENTRYPOINT ["cd", "/opt/cesapi", "&&", "/bin/sh", "/opt/cesapi/run.sh"]
