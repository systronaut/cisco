FROM python:3.8-slim-buster
LABEL maintainer "iDustBin"

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade virtualenv

## SSL python connectons
RUN pip3 install requests[security]
RUN pip3 install pyopenssl ndg-httpsclient pyasn1

## Copy Cisco SourceCode
COPY ./ /app

## Change Working Directory
WORKDIR /app

## Install PyVMomi Dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#Port Socket
EXPOSE 8083/tcp

#Start Cisco Microservice
CMD python3 /app/s300/main.py