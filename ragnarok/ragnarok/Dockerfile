# $$$$$$$$$$$$$$$$$$$$$$$$  GO_BUILD $$$$$$$$$$$$$$$$$$$$$$$$
FROM golang:1.21 AS go_build

# PRE-REQUISITES
RUN apt-get update -y
RUN apt-get autoclean
RUN apt-get install libpcap-dev -y

RUN go install -v github.com/hahwul/dalfox/v2@latest
RUN go install -v github.com/ffuf/ffuf/v2@latest
RUN go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
RUN go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
RUN go install -v github.com/OJ/gobuster/v3@latest

# $$$$$$$$$$$$$$$$$$$$$$$$  RAGNAROK $$$$$$$$$$$$$$$$$$$$$$$$
FROM ubuntu:22.04
WORKDIR /ragnarok
COPY --from=go_build /go/bin/dalfox /usr/local/bin/dalfox
COPY --from=go_build /go/bin/ffuf /usr/local/bin/ffuf
COPY --from=go_build /go/bin/nuclei /usr/local/bin/nuclei
COPY --from=go_build /go/bin/naabu /usr/local/bin/naabu
COPY --from=go_build /go/bin/gobuster /usr/local/bin/gobuster

RUN apt-get update -y
RUN apt-get install wget curl unzip git ruby ruby-dev libcurl4-openssl-dev liblzma-dev zlib1g-dev libpcap-dev python3-pycurl python3-bs4 python3-geoip python3-cairocffi python3-selenium dnsrecon whatweb wafw00f nmap nikto dnsenum dnsutils whois host python3 python3-pip -y

CMD ["bash"]
