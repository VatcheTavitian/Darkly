# Local File Inclusion

## Issue

The 'page' parameter at "http://{IP}:{PORT}/index.php?page=" does not sanitize the query value allowing an attacker to request \
the server load files or pages outside of permitted directories. This can result in a Local File Inclusion (LFI) vulnerability, \ 
which could allow an attacker to access sensitive files on the server, such as configuration files, password files, or \ 
other important files that should not be accessible.


## Attack Vector

1 - Navigate to http://{IP}:{PORT}/index.php?page=signin

2 - Change 'signin' to '../../../../../../../etc/passwd'

3 - Full URL is  http://{IP}:{PORT}/index.php?page=../../../../../../../etc/passwd


## PoC

<img src="02_Screenshot.png" width="70%" height="70%" />


## Mitigation

1 - Sanitize query string input and escape non-permitted characters

2 - Identify path traversal attempts and implement backend validation to whitelist file and in specific directories

3 - Disable PHP inclusion if necessary

