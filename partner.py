import requests
import json

partner_url="http://join.navgurukul.org/api/partners"
data=requests.get(partner_url)
file=data.json()
with open ("data.json","w") as f:
    json.dump(file,f,indent=2)

i=0
serial=1
while i<len(file["data"]):
    print(i,file["data"][i]["name"],":",file["data"][i]["id"])
    i+=1

    Data=(i,file["data"][i]["id"])
    num=input("what you want assending or dessending, a or d")

    list=[]
    for i in Data:
        if num=="a":
            sorted_data=sorted(file["data"],key=lambda x:x["id"])
            list.append(sorted_data)
            # print(list)

            with open ("partner.json","w") as f2:
                json.dump(list,f2,indent=3)
           

