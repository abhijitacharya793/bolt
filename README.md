<br>
<br>
<p align="center">
  <a href="https://github.com/TROUBLE-1/Vajra/">
    <img src="_readme/bolt.jpg"   >
  </a>
</p>

<h1 align="center">
  BO⚡LT
</h1>

<p align="center">
<code>Bolt</code> is a powerful and user-friendly DAST tool designed to scan APIs for vulnerabilities and provide comprehensive reports. Developed with security in mind, Bolt leverages Docker to streamline the setup of isolated containers for efficient testing.
</p>

<p align="center">
  <a href="#services">Services</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

## 🖥️ services

### naming convention

Phases:

- Pre-scan - pre\_<repo> - rune -> midgard -> asgard
- Scan - sca\_<repo> - ragnarok
- Post-scan - pos\_<repo> -

https://moesaid.github.io/cleopatra/index-1.html
https://apexcharts.com/react-chart-demos/bar-charts/reversed-bar-chart/
https://fontawesome.com/v5/search?q=input&o=r

<details>
    <summary> Bifrost/Bifrost - UI </summary>
    
### bifrost/bifrost-ui

- central server for all presentation needs
</details>

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

`docker exec -it ragnarok /bin/bash`

`python manage.py loaddata data/vulnerability.json`

`docker run -d -p 8080:80 vulnerables/web-dvwa`

`echo http://host.docker.internal:8080 | nuclei -headless -t /yggdrasil/resources/nuclei/templates/SXSS/template2.yaml`

`nuclei -u testphp.vulnweb.com -t /ragnarok/inputcopy/ -o output.api -irr -me output -rc nuclei_elastic.yml`

`nuclei -u testphp.vulnweb.com -t /ragnarok/inputcopy/ -jsonl -o output.json -silent -irr -me export`

# bolt

## Services

### bifrost

#### APIs

- api
  - uuid
  - target
  - root_domain
  - domain
  - protocol
  - protocol_version
  - port
  - method
  - path
  - body
- header
  - name
  - value
  - api
- query
  - name
  - value
  - api

### rune

#### APIs

- burp-export
  - name
  - scope
  - power
  - burp_export

### valhalla

#### APIs

- enrich
  - scan_id
  - uuid
  - power
  - scope
  - tasks
  - completion
  - status

### asgard

### yggdrasil

#### APIs

- tag
  - name
- fuzzing
  - part
  - condition
  - required
- risk
  - name
  - abbreviation
- vulnerability
  - name
  - risk
  - description
  - remediation
  - steps_to_reproduce
  - command
  - severity
  - power
  - tag
  - fuzzing_rules
- template
  - vulnerability
  - path

### hiemdall

#### APIs

- result
  - scan_id
  - vulnerability_id
  - uuid
  - template_id
  - payload_str
  - matched_at
  - curl_command
  - matcher_name

### ragnarok

### Folder structure

```
app
 |__src
    |__internal
        |__database
            |__*.go
        |__package2
            |__*.go
    |__sql
        |__queries
            |__*.go
        |__schema
            |__001_*.sql
    |__vendor
        |__package_copy
    |__.env
    |__go.mod
    |__go.sum
    |__handler_*.go
    |__json.go
    |__main.go
    |__models.go
    |__sqlc.yaml
 |__Dockerfile
```

### New Module

```bash
go mod init github.com/abhijitacharya793/ragnarok
```

### Run migrations

```
goose postgres postgres://postgres:postgres@localhost:5432/bolt up
```

### Run queries

```
cd bolt/bifrost
docker run --rm -v ${pwd}:/src -w /src kjconroy/sqlc generate
```

### ui api calls

- dashboard
  - valhalla enricher
- adaptors
  - rune burp export
- scans
  - rune burp export
  - valhalla enricher
- vulnerabilities
  - yggdrasil vulnerability
  - yggdrasil risk
  - yggdrasil tag
  - hiemdall result
- vulnerability classes
  - yggdrasil vulnerability
  - yggdrasil risk
  - yggdrasil tag

### backend api calls

- bifrost
