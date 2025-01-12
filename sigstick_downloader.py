import os
import urllib.request, urllib.parse
from bs4 import BeautifulSoup as bs

url = input('Enter URL: ')
folderName = input('Enter folder name: ')

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')
html = bs(webContent).prettify()

html = html[html.find('<link as="image" href="/assets/icon/imessage256_icon.png'):]
html = (((((html[:html.find('<link as="image" href="/assets/img/appstore.svg')]
        .replace('<link as="image" href="', ""))
        .replace('/assets/icon/imessage256_icon.png', ""))
        .replace('" rel="preload"/>', ""))
        .replace('.thumb128', ""))
        .replace('  ', ""))
urlList = [line for line in html.splitlines() if line.strip()]

index1 = (urlList[0]
          .replace('https://imgcdn.sigstick.com/', "")
          .replace('/0.webp', ""))

os.mkdir(folderName)
for line in urlList:
    if index1 in line:
        a = line.replace("https://imgcdn.sigstick.com/" + index1 + "/", "")
        urllib.request.urlretrieve(line, folderName + "/" + a)