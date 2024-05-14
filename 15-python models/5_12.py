import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
headers = {
    "User-Agent":"your agent here"
}
response = requests.get(url,headers=headers).content

soup = BeautifulSoup(response,"html.parser")


ul = soup.find("ul",class_="ipc-metadata-list")                                     #find the list (ul)
li_elements = ul.find_all("li",class_="ipc-metadata-list-summary-item",limit=10)    #find all tv shows (li)
for li in li_elements:                                                              #loop throgh the shows
    title = li.find("h3",class_="ipc-title__text").text                             #get show title
    rating = li.find("span",class_="ipc-rating-star").text                          #get show rating
    print(title+" - "+rating.split()[0]+"/10")                                      #split the rating i we get 9.5 part instad of 9.5 (12k) then we take [0] first item

# print(result)