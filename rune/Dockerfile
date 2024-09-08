FROM golang:alpine as build

WORKDIR /rune
COPY . /rune
RUN go build -o /bin/main api/api.go

FROM scratch
COPY --from=build /bin/main /bin/main
COPY --from=build /rune/config/ /rune/config/
COPY --from=build /rune/uploads/ /rune/uploads/
WORKDIR /rune
CMD [ "/bin/main" ]