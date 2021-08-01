from os import name
from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import json

def scrap_ecommerce():
   url= "https://webscraper.io/test-sites"
   req=requests.get(url)
#    print(req)
   soup=BeautifulSoup(req.text,"html.parser")
   # print(soup)
   names=soup.find_all("h2",class_="site-heading")
   # print(names)
   
   i=0
   list=[]
   while i <len(names):
    
      name=names[i].find("a").get_text()
      # print(name)
      url=names[i].find("a")["href"]
      # print(url)
      i=i+1
      dic={"postion":i,"names":name,"links":url}
      # print(dic)
      list.append(dic)

   with open("parants_data.json","w")as _data:
      json.dump(list,_data,indent=4)
scrap_ecommerce()