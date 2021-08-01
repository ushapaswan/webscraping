from bs4 import BeautifulSoup
import requests
import json


def screp_top_list():   
    res="https://www.imdb.com/india/top-rated-indian-movies/"
    link2=requests.get(res)
    # print(link2)
    soup=BeautifulSoup(link2.text,"html.parser")
    
    list=[]
    div=soup.find("div",class_="lister")
    body=div.find("tbody",class_="lister-list")
    title=body.find_all("tr")
    no=0
    for i in title:
        no=no+1 
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        name=movie_name
        # print(name)
        year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        year_m=int(year)
        rating=i.find("td",class_="ratingColumn").strong.get_text()
        ratting_float=float(rating)
        url=i.find("td",class_="titleColumn").a["href"]
        link=("https://www.imdb.com")+str(url)
        link1=link
        # list.append(dict)
        dict={"position":no,"name":name,"year":year_m,"rating":ratting_float,"url":link1}
        list.append(dict)
        with open("my_file.json","w")as _data:
            json.dump(list,_data,indent=4)

    # return (list)
screp_top_list()