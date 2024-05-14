import requests
from bs4 import BeautifulSoup


url = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
headers = {
    "User-Agent":"your agent here"
}

response = requests.get(url,headers=headers).content
soup = BeautifulSoup(response,"html.parser")
product_elemnts = soup.find("ul",class_="productListContent-frGrtf5XrVXRwJ05HUfU")

product_list = product_elemnts.find_all("li",class_="productListContent-zAP0Y5msy8OHn5z7T_K_",limit=1)

for index,li in enumerate(product_list):
    name = li.h3.text
    price = li.find("div", {"data-test-id": "price-current-price"}).text    # if unique id use id= "element id" if not use{"data-test-id": "elements id"}
    print(index+1 ,price,name)
    

    imges = li.img.get("src")
    print(imges)
