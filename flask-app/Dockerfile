# Instructions copied from - https://hub.docker.com/_/python/
FROM python

# tell the port number the container should expose
EXPOSE 8080

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT python ./comp.py && bash
