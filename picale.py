from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import json

def scrap_pickel_list():
   url= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
   req=requests.get(url)
   # print(req)
   soup=BeautifulSoup(req.text,"html.parser")
   # print(soup)
   main_div=soup.find("div",class_="_3RA-")
   print(main_div)
   pickle_name=main_div.find_all("div",class_="UGUy")
   # print(pickle_name)
   pickle_prise=main_div.find_all("div",class_="_1kMS")
   # print(pickle_prise)
   pickle_url=main_div.find_all("div",class_="_3WhJ")
   # print(pickle_url)
   i=0
   list=[]
   while i<len(pickle_name):
      name=pickle_name[i].get_text()
      # print(name)
      prise=pickle_prise[i].span.get_text()
      # print(prise)
      url=pickle_url[i].a["href"]
      # print(p_url)
      i+=1
      dic={"position":i,"name":name,"prise":prise,"url":url}
      list.append(dic)
   with open("us.json","w")as _data:
      json.dump(list,_data,indent=4)
   # print(list)
   return list

scrap_pickel_list()
