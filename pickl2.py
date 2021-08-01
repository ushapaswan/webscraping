from bs4 import BeautifulSoup
import requests
import json

def scrap_pickel_list():
    url1= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    req1=requests.get(url1)
    soup1=BeautifulSoup(req1.text,"html.parser")
    div=soup1.find("div",class_="_1gX7")
    pages=div.span.get_text()
    s_lst=pages.split(" ")
    print(s_lst)
    a=int(s_lst[1])
    # print(pages)
    # print(a)
    c=a
    print(c)
    # print(c)
    j=1
    while j<=c:
        url= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
        # print(url)
        req=requests.get(url)
        soup=BeautifulSoup(req.text,"html.parser")
        main_div=soup.find("div",class_="_3RA-")
        pickle_name=main_div.find_all("div",class_="UGUy")
        pickle_prise=main_div.find_all("div",class_="_1kMS")
        pickle_url=main_div.find_all("div",class_="_3WhJ")
        j=j+1
        i=0
        list=[]
        while i<len(pickle_name):
            name=pickle_name[i].get_text()
            # print(name)
            prise=pickle_prise[i].span.get_text()
            # print(prise)
            url=pickle_url[i].a["href"]
            # print(p_url)
            dic={"name":name,"prise":prise,"url":url}
            print(dic)
            list.append(dic.copy)
            i+=1
        with open("pickleFile3.json","w") as _data:
            json.dump(list,_data,indent=4)
        # return list
print(scrap_pickel_list())
