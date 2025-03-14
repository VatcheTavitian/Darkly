# Spoofing Referrer and User-Agent


## Issue

Sensitive information in HTML code leads to manipulation of Referrer and User-Agent HTTP headers at page "http://{IP}:{PORT}/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" 


## Attack Vector

1 - Navigating to "http://{IP}:{PORT}/index.php?page=media&src=nsa" reveals a link to "http://{IP}:{PORT}/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"

2 - Following link to this page we examine the source code and find the following comments in html code: \
`<!--You must come from : "https://www.nsa.gov/".-->` and `<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->`

3 - We set the Referrer Header in HTTP Request to "https://www.nsa.gov/"

4 - We set the User-Agent Header in HTTP Request to "ft_bornToSec"

<img src="10_Screenshot2.png" width="70%" height="70%" />

5 - After submitting the request the flag is revealed.

6 - Flag is `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

_* NOTE: You can use a browser extension such as 'Modify Header Value' on Firefox to change header values *_


## PoC

<img src="10_Screenshot1.png" width="70%" height="70%" />
<img src="10_Screenshot3.png" width="70%" height="70%" />


## Mitigation

1 - Do not include sensitive information in HTML comments

2 - Implement further authentication mechanisms to validate user
