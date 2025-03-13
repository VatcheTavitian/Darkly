import hashlib

target="437394baff5aa33daa618be47b75cb49" # This is the hash found in htpassword file

# Note: Passwordlist.txt should contain passwords from rockyou.txt
with open("passwordlist.txt", "r",errors='ignore') as f:
    for line in f:
        md5_hash = hashlib.md5(line.strip().encode()).hexdigest()
        if (md5_hash == target):
            print("Hashmatch found")
            print(f"Password is {line.strip()}")
            exit()



    