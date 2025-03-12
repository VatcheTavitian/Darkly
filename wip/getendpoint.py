results = open("checkendpoint","w")
with open("readmelist.txt","r") as f:
    for u in f: 
        if not u.strip().endswith('/",'):
            results.write(u)

results.close()