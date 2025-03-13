import requests

url = "http://{IP}:{PORT}/"
error_message = "404: Not Found"
recurse = set() 

# First pass - initial directory scan
try:
    with open("directorylist.txt", 'r') as f:
        for line in f:
            path = url + (line.strip() if line.strip().endswith('/') else line.strip() + '/')
            try:
                req = requests.get(path)
                if error_message not in req.text:
                    if line.strip() not in recurse: 
                        recurse.add(line.strip())
                        print(f"Discovered: {line.strip()}")
            except requests.RequestException as e:
                print(f"Error with {path}: {str(e)}")
except Exception as e:
    print(f"Error during initial scan: {str(e)}")

# Second pass - recursion on discovered directories
try:
    for each in recurse:
        with open("directorylist.txt", 'r') as f:
            for line in f:
                path = url + each + '/' + (line.strip() if line.strip().endswith('/') else line.strip() + '/')
                try:
                    req = requests.get(path)
                    if error_message not in req.text:
                        if line.strip() not in recurse:  
                            recurse.add(line.strip())
                            print(f"Discovered: {line.strip()}")
                except requests.RequestException as e:
                    print(f"Error with {path}: {str(e)}")
except Exception as e:
    print(f"Error during recursion: {str(e)}")

print("Scan Complete")
