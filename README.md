# bolt

### naming convention
Phases:
* Pre-scan	- pre_<repo>	- rune -> midgard -> asgard
* Scan		- sca_<repo>	- ragnarok
* Post-scan	- pos_<repo>	- 

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
        - `dirb`
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
 - 
