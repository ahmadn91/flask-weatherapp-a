import json


def get_id(cityname):
    json_data=open(r'C:\Users\Ahmed\Desktop\weather\city.list.json',encoding="utf8").read()
    data = json.loads(json_data)
    for i in data:
        if i["name"] == cityname:
            id = i["id"]
            return id
        elif i["name"] == "None":
            return "none"
