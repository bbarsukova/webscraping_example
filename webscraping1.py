
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve the span the anchor tags/
#tags = soup('a')

#url = 'http://url'
count = 0
while count < 7:
    taglist = []
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        taglist.append(tag)
    url = taglist[17].get("href", None)
    count = count + 1
    print(url)
