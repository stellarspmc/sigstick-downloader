import os
import urllib.request, urllib.parse
from bs4 import BeautifulSoup as bs

# url = input('Enter URL: ')
url = "https://www.sigstick.com/pack/vSLNeemOBn9dEADQi1Z5"

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')
html = bs(webContent).prettify()

html = html[html.find('<link as="image" href="/assets/icon/imessage256_icon.png'):]
html = html[:html.find('<link as="image" href="/assets/img/appstore.svg')]
html = html.replace('<link as="image" href="', "")
html = html.replace('/assets/icon/imessage256_icon.png', "")
html = html.replace('" rel="preload"/>', "")
html = html.replace('.thumb128', "")
html = html.replace('  ', "")
urlList = html.splitlines()
urlList = [line for line in urlList if line.strip()]

index1 = urlList[0]
index1 = index1.replace('https://imgcdn.sigstick.com/', "")
index1 = index1.replace('/0.webp', "")

os.mkdir(index1)
for line in urlList:
    if index1 in line:
        a = line.replace("https://imgcdn.sigstick.com/" + index1 + "/", "")
        urllib.request.urlretrieve(line, index1 + "/" + a)