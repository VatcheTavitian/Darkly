import hashlib

i_am_admin_variable="68934a3e9455fa72420237eb05902327"


md5_hash = hashlib.md5("false".encode()).hexdigest()
print(md5_hash)
if (md5_hash == i_am_admin_variable):
    print("I am admin variable is set using weak method")
    true_md5_hash = hashlib.md5("true".encode()).hexdigest()
    print(f"Send request with cookie i_am_admin={true_md5_hash} for breach")