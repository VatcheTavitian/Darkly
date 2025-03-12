# import requests

# url = "http://10.18.125.219:8000/"
# error_message = "404: Not Found"

# try:
#     with open("directorylist.txt", 'r') as f:
#         for line in f:
#             # print(f"Trying {line}")
#             path = url + (line.strip() if line.strip().endswith('/') else line.strip() + '/')
#             # print(path)
#             try:
#                 req = requests.get(path)
#                 if error_message not in req.text:
#                     print(line.strip())
#             except Exception as e:
#                 print(str(e))
#     f.close()
# except:
#     print("Error")

# print("Scan Complete")

# import requests

# url = "http://10.18.125.219:8000"
# error_message = "404: Not Found"

# try:
#     with open("discovery.txt", 'r') as f:
#         with open("directorylist.txt", 'r') as x:
#             for line in f:
#                     for each in x:
#                     # print(f"Trying {line}")
#                         path = f"{url}/{line.strip()}/{each.strip()}"
#                         # print(path)
#                         try:
#                             req = requests.get(path)
#                             if error_message not in req.text:
#                                 print(line.strip())
#                         except requests.RequestException as e:
#                             pass
#                             # print(f"Error with {path}: {str(e)}")
#                         except Exception as e:
#                             pass
#                             # print(str(e))
    
# except:
#     print("Error")

# print("Scan Complete")


import requests

url = "http://10.18.125.219:8000"
error_message = "404: Not Found"

try:
    with open("discovery.txt", 'r') as f:
        # Read the lines of discovery.txt
        discovery_lines = f.readlines()
        
    with open("directorylist.txt", 'r') as x:
        # Read the lines of directorylist.txt
        directory_list = x.readlines()
    
    # Now iterate over each line in discovery.txt
    for line in discovery_lines:
        line = line.strip()  # Remove extra spaces or newlines
        for each in directory_list:
            each = each.strip()  # Remove extra spaces or newlines
            path = f"{url}/{line}/{each}"
            # print(f"Trying {path}")  # Uncomment this if you want to debug the path
            try:
                req = requests.get(path)
                if error_message not in req.text:
                    print(f"Found: {path}")
            except requests.RequestException as e:
                # Handle request exceptions (timeouts, connection errors, etc.)
                pass
            except Exception as e:
                # Handle any other unexpected exceptions
                pass

except Exception as e:
    print(f"Error: {str(e)}")

print("Scan Complete")
