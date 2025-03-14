# Sensitive File Disclosure

## Issue

Navigating to  "http://{IP}:{PORT}/robots.txt" reveals sensitive file with credentials that ultimately lead to admin access.


## Attack Vector

1 - Navigate to "http://{IP}:{PORT}/robots.txt". A directory '/whatever' is visible which hosts a file 'htpassword'

2 - Download and open the file at "http://{IP}:{PORT}/whatever/htpassword"

3 - Examining the content reveals credentials 'root:437394baff5aa33daa618be47b75cb49'. The password appears to be an md5 hash.

4 - Open bash and navigate to script directory. Launch script with `python3 hashcracker.py` to attempt to crack md5 hash against the passwordlist.txt word list

5- The script successfully finds a word which matches the hash. Credentials are revealed to be `root:qwerty123@`

6- Attempt to login "http://{IP}:{PORT}/index.php?page=signin" is unsuccessful. We need to see if we can locate another login page.

7- Open bash and navigate to script directory. Launch script with `python3 directorycheckrecursive.py` to attempt to brute force enumerate other potential directories using directorylist.txt word list. 

8- Enumerated directories reveals interesting location at '/admin/'. Navigate to "http://{IP}:{PORT}/admin/"

9- Login with credentials `root:qwerty123@`

10 - Flag revealed is `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

*NOTE - You can use existing MD5 decryption tools such as MD5decrypt.net to attempt to crack root password hash. \
For directory brute force enumeration, you can use existing tools such as GoBuster and DirBuster*


## PoC

<img src="06_Screenshot.png" width="70%" height="70%" />


## Mitigation

1 - Do not place files in publicly accessible directories or deny access

2 - Do not reveal sensitive files in robots.txt

3 - Configure webserver to block access to specific files




