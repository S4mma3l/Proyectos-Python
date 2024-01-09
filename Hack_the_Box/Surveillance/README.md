Maquina Surveillance

ping -c 1 10.10.11.245

PING 10.10.11.245 (10.10.11.245) 56(84) bytes of data.
64 bytes from 10.10.11.245: icmp_seq=1 ttl=63 time=93.6 ms

--- 10.10.11.245 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 93.634/93.634/93.634/0.000 ms

sudo nmap -p- -sS --min-rate 5000 -vvv -n -Pn 10.10.11.245 -oG Puertos
[sudo] password for sammael:

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-13 19:25 CST
Initiating SYN Stealth Scan at 19:25
Scanning 10.10.11.245 [65535 ports]
Discovered open port 80/tcp on 10.10.11.245
Discovered open port 22/tcp on 10.10.11.245
Discovered open port 6802/tcp on 10.10.11.245
Completed SYN Stealth Scan at 19:25, 13.81s elapsed (65535 total ports)
Nmap scan report for 10.10.11.245
Host is up, received user-set (0.097s latency).
Scanned at 2023-12-13 19:25:19 CST for 14s
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack ttl 63
80/tcp   open  http    syn-ack ttl 63
6802/tcp open  unknown syn-ack ttl 63

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 13.94 seconds
           Raw packets sent: 68367 (3.008MB) | Rcvd: 67426 (2.697MB)

❯ sudo nmap -sCV -p22,80 10.10.11.245 -oN Targeted

[sudo] password for sammael:

Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-13 19:44 CST
Nmap scan report for surveillance.htb (10.10.11.245)
Host is up (0.23s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 96:07:1c:c6:77:3e:07:a0:cc:6f:24:19:74:4d:57:0b (ECDSA)
|_  256 0b:a4:c0:cf:e2:3b:95:ae:f6:f5:df:7d:0c:88:d6:ce (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title:  Surveillance
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.34 seconds


❯ whatweb 10.10.11.245

http://10.10.11.245 [302 Found] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.245], RedirectLocation[http://surveillance.htb/], Title[302 Found], nginx[1.18.0]
ERROR Opening: http://surveillance.htb/ - no address for surveillance.htb

❯ echo "10.10.11.245  surveillance.htb" >> /etc/hosts

❯ whatweb 10.10.11.245

http://10.10.11.245 [302 Found] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.245], RedirectLocation[http://surveillance.htb/], Title[302 Found], nginx[1.18.0]
http://surveillance.htb/ [200 OK] Bootstrap, Country[RESERVED][ZZ], Email[demo@surveillance.htb], HTML5, HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.10.11.245], JQuery[3.4.1], Script[text/javascript], Title[Surveillance], X-Powered-By[Craft CMS], X-UA-Compatible[IE=edge], nginx[1.18.0]


podemos ver en el codigo fuente este detalle         

&copy; <span id="displayYear"></span> All Rights Reserved By
SURVEILLANCE.HTB</a><br> <b>Powered by <a href="https://github.com/craftcms/cms/tree/4.4.14"/>Craft CMS</a></b>


❯ gobuster dir -u http://surveillance.htb/ -w /usr/share/seclists/Discovery/Web-Content/common.txt -r
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://surveillance.htb/
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
/.gitkeep             (Status: 200) [Size: 0]
/.htaccess            (Status: 200) [Size: 304]
/admin                (Status: 200) [Size: 38436]
/css                  (Status: 403) [Size: 162]
/fonts                (Status: 403) [Size: 162]
/images               (Status: 403) [Size: 162]
/img                  (Status: 403) [Size: 162]
/index                (Status: 200) [Size: 1]
/index.php            (Status: 200) [Size: 16230]
/js                   (Status: 403) [Size: 162]
/logout               (Status: 200) [Size: 16230]
/web.config           (Status: 200) [Size: 1202]
/wp-admin             (Status: 418) [Size: 24409]
Progress: 4723 / 4724 (99.98%)
===============================================================
Finished
===============================================================
