from bs4 import BeautifulSoup
import urllib3

test_url=urllib3.urlopen("http://reddit.com")
readhtml=test_url.read()
test_url.close()

soup=BeautifulSoup(readhtml)
all_tag_a=soup.find_all("a",limit=10)
for links in all_tag_a:
    print(links.get('href'))