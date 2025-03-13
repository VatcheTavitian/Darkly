# Weak Credentials Sign In Page

## Issue

The 'SignIn' page at "http://{IP}:{PORT}/index.php?page=signin" does not restrict number \
of login attempts and does not lock user account after numerous failed login attempts. \
This allows for a brute force attack in an attempt to user reveal credentials. Furthermore \
with weak password policies in place, likelihood of brute forcing login is increased.


## Attack Vector

1 - Enumerate the website to identify potential user names. We identified potential username 'wil' visible on feedback page at "http://{IP}:{PORT}/index.php?page=feedback"

2 - Use our 'brute_force.py' script with a strong password list. As per script instructions, we recommend rockyou.txt list from GitHub

3 - Open bash and navigate to script directory. Launch script with `python3 brute_force.py`

4 - The script will attempt to login as 'wil' using every password from the passwod list

5 - If a successful login is found, the password is revealed. In this case the credentials are `wil:shadow`

*NOTE - You can use existing brute force tools such as Hydra, BurpSuite Intruder and Medusa*


## PoC
<img src="04_Screenshot.png" width="70%" height="70%" />



## Mitigation

1 - Restrict login attempts from a particular IP with rate limiting

2 - Lock user account after numerous unsuccessful login in attempts

3 - Implement CAPTCHA challenge

4 - Implement Multi-Factor Authentication

5 - Require strong password policies

