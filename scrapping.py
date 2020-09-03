import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

img_lst = []
link_lst = []

image = soup('img')
for imge in image:
    if imge in img_lst:
        continue
    else:
        img_lst.append(imge)
        img_lst.sort()

link = soup('link')
for lk in link:
    if lk in link_lst:
        continue
    else:
        link_lst.append(lk)


print('Image List- ', img_lst)
print('Link List- ', link_lst)


