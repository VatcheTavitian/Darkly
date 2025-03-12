import hashlib


target="5ff9d0165b4f92b14994e5c685cdce28" 

# Note: Passwordlist.txt should contain passwords from rockyou.txt
with open("passwordlist.txt", "r",errors='ignore') as f:
    for line in f:
        md5_hash = hashlib.md5(line.strip().encode()).hexdigest()
        if (md5_hash == target):
            print("Hashmatch found")
            print(f"Password is {line.strip()}")
            exit()



    