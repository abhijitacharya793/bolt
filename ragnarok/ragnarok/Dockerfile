# docker build . -t ragnarok
# docker run -it ragnarok /bin/sh
FROM ubuntu:22.04

WORKDIR /ragnarok

# Update
RUN apt-get update -y
RUN apt-get install wget -y
RUN apt-get install curl -y
RUN apt-get install unzip -y
RUN apt-get install git -y
RUN apt-get install ruby ruby-dev libcurl4-openssl-dev liblzma-dev zlib1g-dev -y
RUN apt install libpcap-dev -y
RUN apt-get install python3-pycurl python3-bs4 python3-geoip python3-cairocffi python3-selenium -y
RUN apt-get install dnsrecon -y
RUN apt-get install whatweb -y
RUN apt-get install wafw00f -y 
# TODO: RUN apt-get install eyewitness -y
RUN apt-get install nmap -y 
RUN apt-get install nikto -y 
RUN apt-get install dnsenum -y
RUN apt-get install dnsutils -y
RUN apt-get install whois -y
RUN apt-get install host -y
# TODO: RUN apt-get install xsser -y

# Python
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

# Go AMD 64
RUN wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz
RUN echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
RUN echo "export PATH=$PATH:/root/go/bin" >> ~/.bashrc
RUN /usr/local/go/bin/go version

# Findomain
RUN curl -LO https://github.com/findomain/findomain/releases/latest/download/findomain-linux.zip
RUN unzip findomain-linux.zip
RUN chmod +x findomain
RUN mv findomain /usr/bin/findomain
RUN findomain --help

# Searchsploit
# RUN git clone https://gitlab.com/exploit-database/exploitdb.git /opt/exploit-database
# RUN cp -n /opt/exploit-database/.searchsploit_rc ~/
# USAGE: /opt/exploit-database/searchsploit

# python tools
# RUN python3 -m pip install fierce


# Go tools
# RUN /usr/local/go/bin/go install -v github.com/hahwul/dalfox/v2@latest
# RUN /usr/local/go/bin/go install -v github.com/ffuf/ffuf/v2@latest
# RUN /usr/local/go/bin/go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
# RUN /usr/local/go/bin/go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
# RUN /usr/local/go/bin/go install -v github.com/OJ/gobuster/v3@latest

# USAGE: ./go/bin/ffuf

# sublist3r
# httrack
# eyewitness

# sqlmap


# COPY ./requirements.txt /ragnarok/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /ragnarok/requirements.txt

# COPY ./entrypoint.sh /ragnarok/entrypoint.sh

# ENTRYPOINT ["/ragnarok/entrypoint.sh"]

# COPY . /ragnarok

CMD ["bash"]