FROM golang:alpine as build

WORKDIR /asgard
COPY . /asgard
RUN go build -o /bin/main scheduler/scheduler.go

FROM scratch
COPY --from=build /bin/main /bin/main
WORKDIR /asgard
CMD [ "/bin/main" ]