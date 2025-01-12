import json
import urllib.request, urllib.parse
from pathlib import Path

while True:
    url = input('Enter URL: ')
    folderName = input('Enter folder name: ')

    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')

    html = html[html.find('<script id="__NEXT_DATA__" type="application/json">'):]
    html = html.replace('<script id="__NEXT_DATA__" type="application/json">', '')
    html = html[:html.find('</script>')]
    json1 = json.loads(html)
    Path(folderName).mkdir(parents=True, exist_ok=True)
    finalJson = json1["props"]["pageProps"]["pack"]["stickers"]

    index = 0
    for a in finalJson:
        urllib.request.urlretrieve(a["url"], folderName + "/" + str(index) + ".webp")
        index += 1