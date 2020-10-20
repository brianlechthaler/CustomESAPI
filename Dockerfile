FROM alpine:edge
RUN apk add py3-pip

RUN echo "---> Installing Python 3.x Dependencies..."

RUN python3 -m pip install -U pip
RUN python3 -m pip install -r /opt/cesapi/requirements.txt

RUN mkdir -p /opt/cesapi
ADD . /opt/cesapi

ENTRYPOINT ["cd", "/opt/cesapi", "&&", "/bin/sh", "/opt/cesapi/run.sh"]
