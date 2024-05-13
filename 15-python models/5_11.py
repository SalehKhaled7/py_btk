html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>py | btk academy</title>
</head>
<body>
    <h1>python course 40 hrs | sadik turan</h1>
    <div class="section1">
        <h2>section 1</h2>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
          </ul>
    </div>
 
    <div class="section2">
        <h2>section 2</h2>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
          </ul>
    </div>
 
    <div class="section3">
            <h2>section 3</h2>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
          </ul>
    </div>
    <a class="sister" href="http://example1.com/tillie" id="link3">Tillie</a>
    <a class="sister" href="http://example2.com/tillie" id="link3">Tillie</a>
    <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>
   <footer>
   <!--js ,scripts here-->
   </footer>
</body>
</html>

"""

from bs4 import BeautifulSoup


soup = BeautifulSoup(html_doc ,"html.parser") 

result = soup.prettify()            #fix the indentation
result = soup.title                 #get everything in between <title>.....<title>
result = soup.head                  #get everything in between <head>.....<head>
result = soup.body                  #get everything in between <body>.....<body>
result = soup.footer                #get everything in between <footer>.....<footer>

result = soup.title.name            #get title tage
result = soup.title.string          #get title text 

result = soup.h1                    #get h1 tag
result = soup.h2                    #get h2 tag - if more than 1 return the first one only
result = soup.h2.string             #get h2 tag text - if more than 1 return the first one only
result = soup.div             #get h2 tag text - if more than 1 return the first one only

result = soup.find_all("h2")                        #get all h2 in the page (list)
result = soup.find_all("h2")[0]                     #get the first h2 from the list (list)
result = soup.find_all("div")[0].ul                 #get the first ul from the div in index 0
result = soup.find_all("div")[0].ul.li              #get the first ul from the div in index 0
result = soup.find_all("div")[0].ul.find_all('li')  #get the first ul from the div in index 0

result = soup.div.findChildren()                            #the children of first div
result = soup.div.find_next_sibling()                       #find element's next sipling (div 2)
result = soup.div.find_next_sibling().find_next_sibling()   #find element's next next sipling (div 3)
result = soup.div.find_next_siblings()                      #find element's next siplings
result = soup.div.find_previous_sibling()                   #find element's neprevious sipling/s

result = soup.find_all("a")             #get all links in the page

# for link in result:
    # print(link.get('href'))           #get link href  
    # print(link.get('class'))          #get link class
    #print(link.get('id'))              #get link id
    #print(link.string)                 #get link text

    

print(result)