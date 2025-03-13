import hashlib

i_am_admin_cookie="68934a3e9455fa72420237eb05902327"

md5_hash = hashlib.md5("false".encode()).hexdigest()
print(f'MD5 hash of "false" is = {md5_hash} matches the "i_am_admin" default cookie value')
if (md5_hash == i_am_admin_cookie):
    print("I am admin variable is set using weak method")
    true_md5_hash = hashlib.md5("true".encode()).hexdigest()
    print('MD5 hash of "true" is =', true_md5_hash)
    print(f"Send request with cookie 'i_am_admin={true_md5_hash}' for breach")