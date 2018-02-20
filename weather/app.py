from flask import Flask, render_template, request, url_for, redirect
import datetime
from getdata import get_data
from cityid import get_id





app = Flask(__name__)



@app.route("/home/",methods=["GET","POST"])
def index():
    def_id = "98182"
    if request.method == "POST":
        def_id = get_id(request.form["cityname"])
        if def_id == "none":
            def_id ="98182"
    data_dict = get_data(str(def_id))
    time = datetime.datetime.now().strftime("%I:%M")
    date = datetime.date.today().strftime("%B %d, %Y")
    city_name = data_dict["name"]
    country_name = data_dict["sys"].get("country")
    temp = int(data_dict["main"].get("temp") - 273.15)
    temp_min = int(data_dict["main"].get("temp_min") - 273.15)
    temp_max = int(data_dict["main"].get("temp_max") - 273.15)
    condition = data_dict["weather"][0].get("main")
    icon_url = data_dict["weather"][0].get("icon") + ".png"
    hum = data_dict["main"].get("humidity")
    suns = datetime.datetime.fromtimestamp(data_dict["sys"].get("sunset")).strftime('%H:%M')
    sunr = datetime.datetime.fromtimestamp(data_dict["sys"].get("sunrise")).strftime('%H:%M')
    pres = data_dict["main"].get("pressure")
    wind = data_dict["wind"].get("speed")
    windd = data_dict["wind"].get("deg")

    return render_template("home.html",time=time,date=date,city_name=city_name,country_name = country_name,temp = temp,temp_min = temp_min,temp_max = temp_max,icon_url = icon_url,hum=hum,suns = suns,sunr = sunr,pres = pres,wind = wind,windd = windd)












if __name__ == "__main__":
    app.run(debug = True)
