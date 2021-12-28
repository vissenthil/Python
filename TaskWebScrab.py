
from bs4 import BeautifulSoup as bs
import requests
import lxml

r = requests.get(url="https://keithgalli.github.io/web-scraping/webpage.html")
webpage = bs(r.content,features="lxml")
print(webpage.prettify())
print('Print the table')
table = webpage.body.find("table")
print(table)
# Grab all of the social link from the webpage
AllLink = webpage.find_all("a")
print('All the links')
print(AllLink)
print('Grab using class attributes')
link = webpage.find("ul", {"class":"socials"})
print(link)
print('Another way to Grab using class attributes')
link = webpage.select("ul.socials")
print(link)
print('Another way to Grab using class  attributes a href')
print('Here ul is unorder list socials ia class name and a is anchor tag')
link1 = webpage.select("ul.socials a")
for links in link1:
    print(links)

Actual_Links = [link["href"] for link in link1]
print('Print only the actual links:')
for lnk in Actual_Links:
    print(lnk)

Links = webpage.select("li.social a")
Actual_Links = [lnk["href"] for lnk in Links]
print(f'Links:{Actual_Links}')

print('Scrab only the table')
table = webpage.select("table.hockey-stats")[0]
print(table)
print('Columns ')
Columns = webpage.find("thead").find_all("th")
print(Columns)
Columns_names = [c.string for c in Columns]
print("Column Names")
print(Columns_names)
Table_Rows = table.find("tbody").find_all("tr")
print('Table rows')
print(Table_Rows)
l = []
for tr in Table_Rows:
    td = tr.find_all("td")
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)
print('Table Data')
print(l)
import  pandas as pd
print("Using pandas")
df = pd.DataFrame(l,columns=Columns_names)
print(df.head())
print( df["Team"])

print(df.loc[df["Team"] != 'Did not play'])

print('Find out facts that is included is in the sentences')
facts = webpage.select("ul.fun-facts li")
print(facts)
import re
facts_with_is = [fact.find(string=re.compile("is")) for fact in facts]
print("Below code will remove the None from the list")
facts_with_is = [ fact for fact in facts_with_is if fact]
print('Here all sentences contains is')
for fact in facts_with_is:
    print(fact)

print("To download the imae from the webpage")
imgages = webpage.select("div.row div.column img")
image_url = imgages[0]["src"]
print(image_url)
for img in imgages:
    print(img)
url="https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")
full_url = url + image_url
print(f"full url ={full_url}")
print("Down load particular image from the webpage")
image_data = requests.get(full_url).content
with open("Lake_demo.jpg","wb") as handler:
    handler.write(image_data)

files = webpage.select("div.block a")
relative_file = [f["href"] for f in files]
print(relative_file)
url="https://keithgalli.github.io/web-scraping/"
for f in relative_file:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content,features="lxml")
    secrets_word_element = bs_page.find("p",attrs={"id" : "secret-word"})
    print(secrets_word_element.string)
print(full_url)
for txt in webpage.select("div.block li"):
    print(txt.text)
