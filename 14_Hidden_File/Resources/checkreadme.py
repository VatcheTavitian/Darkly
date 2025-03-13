import requests
from bs4 import BeautifulSoup

f = open("scraped_urls.json","r")
w = open("ReadMeFileContent.txt","w")
num_lines = sum(1 for line in f)
f.seek(0)
for x in range(num_lines):
	u = f.readline().replace(',','').replace('"','').replace('\n','')		
	if "README" in u:
		try:
			req = requests.get(u)
			soup = BeautifulSoup(req.text, 'html.parser')
			content = soup.get_text()
			if len(content) > 0:
				w.write(u)
				w.write("\n")
				w.write(content)
		except:
			print('URL FAILED  = |' + u + '|')
print("Done")
w.close()
f.close()

