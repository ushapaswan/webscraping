from task1 import screp_top_list
import json
import pprint

list_of_movies=screp_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    years.sort()
    dict={i:[]for i in years}
    for i in movies:
        year=i["year"]
        for j in dict:
            if str(j)==str(year):
                dict[j].append(i)
                with open("usha's_file.json","w") as _data:
                    json.dump(dict,_data,indent=4)
    return dict
group_by_year(list_of_movies)