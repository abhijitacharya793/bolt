FROM golang:alpine as build

WORKDIR /valhalla
COPY . /valhalla
RUN go build -o /bin/main api/api.go

FROM scratch
COPY --from=build /bin/main /bin/main
COPY --from=build /valhalla/config/ /valhalla/config/
WORKDIR /valhalla
CMD [ "/bin/main" ]