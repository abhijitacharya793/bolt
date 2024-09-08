FROM golang:alpine as build

WORKDIR /bifrost
COPY . /bifrost
RUN go build -o /bin/main api/api.go

FROM scratch
COPY --from=build /bin/main /bin/main
COPY --from=build /bifrost/config/ /bifrost/config/
WORKDIR /bifrost
CMD [ "/bin/main" ]