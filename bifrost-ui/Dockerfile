FROM node:21-alpine3.17

WORKDIR /bifrost-ui

COPY ./package.json /bifrost-ui/package.json

RUN npm install

COPY . /bifrost-ui
