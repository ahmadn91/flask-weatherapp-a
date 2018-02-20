import requests
import ast
def get_data(id):
    if id == "none":
        return id
    else:
        parse = requests.get("http://api.openweathermap.org/data/2.5/weather?id=" + id + "&APPID=c9335ba5c1466649b9c37a5c43a72c17")
        data = parse.text
        data_dict = ast.literal_eval(data)
        return data_dict
