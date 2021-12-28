from bs4 import  BeautifulSoup as bs
import requests
import  lxml
# Webscrapping an imge from the websit
r = requests.get(url='https://likeitviral.com/hollywood/celebrities-who-aged-flawlessly-with-time-vc-tb?utm_source=taboola&utm_medium=msn-anaheim-malaysia&utm_campaign=13091401&utm_term=Remember+Her%3F+She+Was+An+Icon+But+Today+She+Looks+Like+This&utm_content=http%3A%2F%2Fcdn.taboola.com%2Flibtrc%2Fstatic%2Fthumbnails%2F300d765093b4540b51caa740ac8bf8e0.jpg&ts=2021-12-27+01%3A08%3A26&tbv=JcKQE5UpEZ90cFUlQdoYlrK_TF-92txBkqJu99mFbkg%3D')

webcontext = bs(r.content,'lxml')
print(webcontext.prettify())
# to get from img tag and particular class attribute values
images =webcontext.find_all("img",{"class": "alignnone size-full wp-image-17700"})
print('print only the image tab')
print(images)
print('Print only the src tag')
for img in images:
    imgurl = img.get("src")
    response = requests.get(url=imgurl).content # to get the image byte code
    imgname = img.get("src").split('/')[-1]
    print(imgname)
f = open(imgname, "wb")
f.write(response,)


