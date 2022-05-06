import urllib2
from bs4 import BeautifulSoup

url = "http://dofollow.netsons.org/table1.htm"  # change to whatever your url is

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)

for i in soup.find_all('form'):
    print(i.attrs['class'])
