import requests
from bs4 import BeautifulSoup as bs


#Load the webpage contents
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
# Convert a Beautiful soup objects
soup = bs(r.content,features="lxml")
#  ,features="lxml" this is used to avoid the below warrning
# GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system
#printout the html data
print(soup.prettify())

first_header = soup.find('h2')
print('Disply the content of h2 tag')
print(first_header)
print(''' To find all the headers of h2 tag in the webpage
          it will show in the list ''')

headers = soup.find_all('h2')
print(headers)

# pass in a list to look for
headers = soup.find_all(['h1','h2'])
print('Find the data using list ')
print(headers)
# You can pass attributes to find/findall  funtion
paragrah = soup.find_all('p', attrs={"id" : "paragraph-id"})
print('find all the paragraph tag in the webpage')
print(paragrah)

# you can nest find / find_all calls

body = soup.find('body')
print('Disply body of the html page')
print(body)
div = body.find('div')
print('Disply only the div content from the inside the body tag')
print(div)
headerInsideDiv = div.find('h1')
print('Display header inside div tag')
print(headerInsideDiv)

# We can search specific string in our find and find_all calls
import re
a = input('Please enter a string to search =:')
paragrahs = soup.find_all('p',string=re.compile(a))
print('Searched string is :')
print(paragrahs)
print('To search with lower or capital letters (H|h) ')
Headers = soup.find_all('h2',string=re.compile("(H|h)eader"))
print(Headers)

# select the CSS Selector
print('Using select function to select CSS Selectors')
content = soup.select('p')
print(content)

print('To select paragraph inside div tag soup.select("div p")')
content = soup.select('div p')
print(content)
print('To select paragraph after the h2 tag')
paragrahs = soup.select('h2 ~ p')
print(paragrahs)

bold_Text = soup.select("p#paragraph-id b")
print(f'Bold_text is {bold_Text}')
paragrahs = soup.select("body > p")
print('select paragraph tag inside body tag')
print(paragrahs)
print('From Loop')
for paragraph in paragrahs:
    print(paragraph.select("i"))

# scrab by element with specific property
webscrap = soup.select("[align=middle]")
print(webscrap)

header = soup.find("h2")
print('Printing only text inside the h2 tag')
print(header.string)

div = soup.find("div")
print(div.prettify())
print('Print only the context inside Div tag')
print(div.get_text())

#get a specific property from an element
print('Get specific property from an element')
link = soup.find("a")
print(link)
print('To get only the link')
href =  link["href"]
print(href)
print('get only the text')
print(link.text)
#path syntax:
print('Path syntax:')
print(soup.body.div.h1.string)
# Know the terms : parent,child,siblings
print('sibling means in the same level after the dive')
siblings = soup.body.find("div").find_next_siblings()
print(siblings)