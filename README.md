<br>
<br>
<p align="center">
  <a href="https://github.com/TROUBLE-1/Vajra/">
    <img src="https://images.weserv.nl/?url=raw.githubusercontent.com/abhijitacharya793/bolt/7b32d5a8e11e6a85695f3c51ba5e51918b07a826/readme/bolt.jpg?h=300&w=300&fit=cover&mask=circle&maxage=7d"   >
  </a>
</p>

<h1 align="center">
  BO⚡LT
</h1>

<p align="center">
<code>shallow-backup</code> lets you easily create lightweight backups of installed packages, applications, fonts and dotfiles, and automatically push them to a remote Git repository.
</p>

<p align="center">
  <a href="#services">Services</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## :mag_right: services

### naming convention

Phases:

- Pre-scan - pre\_<repo> - rune -> midgard -> asgard
- Scan - sca\_<repo> - ragnarok
- Post-scan - pos\_<repo> -

https://moesaid.github.io/cleopatra/index-1.html
https://apexcharts.com/react-chart-demos/bar-charts/reversed-bar-chart/
https://fontawesome.com/v5/search?q=input&o=r

### bifrost/bifrost-ui

- central server for all presentation needs

### rune

- convert traffic from various sources to API objects:
  - burp export
  - burp live traffic
  - mitmproxy live traffic
  - browser extension

### midgard

- decide what scan to run for a particular API based on:
  - query param
  - path param
  - headers
  - post/put body
  - method
  - scheme

### asgard

- scheduler for scans created in midgard

### ragnarok

- scanning machine
- multistage docker image
  - Go to create go binaries
  - Ununtu to run scripts

### yggdrasil

- script manager
  - upload scripts directly to ragnarok volume
  - save command and inputs to script on yggdrasil
  - pass command to asgard and run same command directly on ragnarok

### hiemdall

- output manager

## Prequisites

- setup scripts on yggdrasil
  - Add tags
  - Add Tools
  - Add risk classes

## Flows

- Get APIs
- Recon
  - Derive domain and root domain
    - `whois <domain>`
    - `host <domain>`
    - virtualhosts??
  - Get subdomain
    - Subdomain enum
    - Google dorks
    - Netkraft??
  - Get metafiles
    - robots.txt
    - sitemap.xml
  - Google dorks
    - `site:ine.com`
    - `inurl:admin`
    - `inurl:forum`
    - `site:*.ine.com //Subdomain enum`
    - `intitle:admin`
    - `filetype:pdf`
    - `filetype:docx,xlsx,zip`
    - `intitle:index of`
    - `cache:ine.com`
    - `inurl:passwd.txt`
    - `inurl:passwd`
  - **Google Hacking Database**
    - https://www.exploit-db.com/google-hacking-database
  - Waybackmachine
  - Web Tech Fingerprinting
    - Builtwith
    - Wappalyzer
    - `whatweb <domain>`
  - WAF Detection
    - `wafwoof <domain> -a`
  - Copy website
    - `mkdir <domain> && cd <domain> && httrack <domain>`
    - `httrack <domain> -O <domain>`
  - Web Screenshots
    - `eyewitness --web -f domains.txt -d Output`
  - crawling/spidering
    - ZAP - zapit, zap cli
  - Web Server Fingerprinting
    - `nmap -sV -F 10.10.10.10` # get services
    - `searchsploit apache 2.4.18` # get exploit for web server version
    - `nmap --script`??
    - banner grabbing
  - Directory bruteforcing
    - `gobuster dir -u {target} -o output.api`
  - DNS Enumeration
    - DNS Interrogation
      - https://dnsdumpster.com
      - `dnsrecon -d zonetransfer.me`
    - DNS Zone Transfer
      - `dnsenum zonetransfer.me`
      - `dig axfr @<nameserver> <domain>`
    - DNS Bruteforce
      - `fierce -dns zonetransfer.me`
  - Subdomain Enumeration
    - `sublist3r -d hackersploit.org` # passive
    - `fierce `
  - count of forms, input fields and html tags
  - look for `FIXME`, `TODO`
- use genai to create a request
  genai to static/dynamic nature of param
  hugging chat
  or https://labs.perplexity.ai/
  use codellama and mixtral ai

https://github.com/sf197/nuclei_gpt/tree/main/data/wiki

docker exec -it ragnarok /bin/bash
python manage.py loaddata data/vulnerability.json
docker run -d -p 8080:80 vulnerables/web-dvwa
