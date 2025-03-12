import hashlib

target="1928e8083cf461a51303633093573c46"

# Note: Passwordlist.txt should contain passwords from rockyou.txt
with open("passwordlist.txt", "r",errors='ignore') as f:
    for line in f:
        md5_hash = hashlib.md5(line.strip().encode()).hexdigest()
        if (md5_hash == target):
            print("Hashmatch found")
            print(f"Password is {line.strip()}")
            exit()



    