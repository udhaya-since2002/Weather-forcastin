from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import datetime
import requests
from flask import redirect,url_for



app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():


    end_point = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "8c81c4a2f6b7546cac7913f74b54311c"
    weather_parmeter = {
        "lat": 9.9261153, "lon": 78.1140983, "appid": api_key,
    }
    res = requests.get(end_point, params=weather_parmeter)
    weather_data = res.json()
#------------------------------------API COLLECTION DATA ENDS--------------------------------------------------------


    twele_hour_data = weather_data["list"][:5]
    temperature = twele_hour_data[0]["main"]["temp"]
    temperature_feel = twele_hour_data[0]["main"]["feels_like"]
    celsius_temperature = round(temperature - 273.15)
    celsius_temperature_feel = round(temperature_feel - 273.15)
    weather_name = twele_hour_data[0]["weather"][0]["main"]
    city = weather_data["city"]["name"]
    hum = twele_hour_data[0]["main"]["humidity"]
    pre = twele_hour_data[0]["main"]["pressure"]
    des = twele_hour_data[0]["weather"][0]["description"]
    id_no = twele_hour_data[0]["weather"][0]["id"]
    wind = twele_hour_data[0]["wind"]["speed"]


#----------------------------------------CURRENT WEATGER DATA CLOSED--------------------------------------------------------------


    next1_temp=twele_hour_data[1]["main"]["temp"]
    next1_celsius=round(next1_temp-273.15)
    id_no1 = twele_hour_data[1]["weather"][0]["id"]
    weather_time1=twele_hour_data[1]["dt_txt"].split()[1][:2]


    next2_temp=twele_hour_data[2]["main"]["temp"]
    next2_celsius=round(next2_temp-273.15)
    id_no2 = twele_hour_data[2]["weather"][0]["id"]
    weather_time2=twele_hour_data[2]["dt_txt"].split()[1][:2]


    next3_temp=twele_hour_data[3]["main"]["temp"]
    next3_celsius=round(next3_temp-273.15)
    id_no3 = twele_hour_data[3]["weather"][0]["id"]
    weather_time3=twele_hour_data[3]["dt_txt"].split()[1][:2]



    next4_temp=twele_hour_data[4]["main"]["temp"]
    next4_celsius=round(next4_temp-273.15)
    id_no4 = twele_hour_data[4]["weather"][0]["id"]
    weather_time4=twele_hour_data[4]["dt_txt"].split()[1][:2]


#-----------------------------------------NEXT WEATHER DATA ENDS-------------------------------------------------------

    date_time = datetime.datetime.now()
    date = date_time.strftime("%d")
    month = date_time.strftime("%b")
    time = date_time.strftime("%H")
    pm_or_am = date_time.strftime("%p")
    day=date_time.strftime("%a")
   # con_time=date_time.now()
    #con_est=con_time.strftime("%I")
    a=f"{date} {month}"
    b=f"{time}"
    c=f"{pm_or_am}"
    d=city
    e=day

#---------------------------------------DATE TIME DATA ENDS---------------------------------------------------------------------

    if request.method=="POST":
        home2=request.form["search"]
        return redirect((url_for("home2",city=home2)))
    else:
        return render_template("weather.html",celsius=celsius_temperature,weather=weather_name,celsius_feel=celsius_temperature_feel,
                           date=a,time=int(b),std=c,city_name=d,day=e,humidity=hum,pressure=pre,desc=des,air=wind,id=id_no,
                           next1_t=next1_celsius,next2_t=next2_celsius,next3_t=next3_celsius,next4_t=next4_celsius,id1=id_no1,id2=id_no2,
                           id3=id_no3,id4=id_no4,up_time1=int(weather_time1),up_time2=int(weather_time2),up_time3=int(weather_time3),up_time4=int(weather_time4))





#---------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------first data ends-----------------------------------------------------------

@app.route('/<city>')
def home2(city):
    loc = Nominatim(user_agent="GetLoc")
    ci = city
    getLoc = loc.geocode(ci)
    data = getLoc.address
    lat = getLoc.latitude
    lon = getLoc.longitude



    end_point = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "8c81c4a2f6b7546cac7913f74b54311c"
    weather_parmeter = {
        "lat": lat, "lon": lon, "appid": api_key,
    }
    res = requests.get(end_point, params=weather_parmeter)
    weather_data = res.json()

    twele_hour_data = weather_data["list"][:5]
    temperature = twele_hour_data[0]["main"]["temp"]
    temperature_feel = twele_hour_data[0]["main"]["feels_like"]
    celsius_temperature = round(temperature - 273.15)
    celsius_temperature_feel = round(temperature_feel - 273.15)
    weather_name = twele_hour_data[0]["weather"][0]["main"]
    city = weather_data["city"]["name"]
    hum = twele_hour_data[0]["main"]["humidity"]
    pre = twele_hour_data[0]["main"]["pressure"]
    des = twele_hour_data[0]["weather"][0]["description"]
    id_no = twele_hour_data[0]["weather"][0]["id"]
    wind = twele_hour_data[0]["wind"]["speed"]

    # ---------------------------------------- SECOND CURRENT WEATGER DATA CLOSED--------------------------------------------------------------

    next1_temp = twele_hour_data[1]["main"]["temp"]
    next1_celsius = round(next1_temp - 273.15)
    id_no1 = twele_hour_data[1]["weather"][0]["id"]
    weather_time1 = twele_hour_data[1]["dt_txt"].split()[1][:2]

    next2_temp = twele_hour_data[2]["main"]["temp"]
    next2_celsius = round(next2_temp - 273.15)
    id_no2 = twele_hour_data[2]["weather"][0]["id"]
    weather_time2 = twele_hour_data[2]["dt_txt"].split()[1][:2]

    next3_temp = twele_hour_data[3]["main"]["temp"]
    next3_celsius = round(next3_temp - 273.15)
    id_no3 = twele_hour_data[3]["weather"][0]["id"]
    weather_time3 = twele_hour_data[3]["dt_txt"].split()[1][:2]

    next4_temp = twele_hour_data[4]["main"]["temp"]
    next4_celsius = round(next4_temp - 273.15)
    id_no4 = twele_hour_data[4]["weather"][0]["id"]
    weather_time4 = twele_hour_data[4]["dt_txt"].split()[1][:2]

    # -----------------------------------------SECOND NEXT WEATHER DATA ENDS-------------------------------------------------------

    date_time = datetime.datetime.now()
    date = date_time.strftime("%d")
    month = date_time.strftime("%b")
    time = date_time.strftime("%H")
    pm_or_am = date_time.strftime("%p")
    day = date_time.strftime("%a")
    # con_time=date_time.now()
    # con_est=con_time.strftime("%I")
    a = f"{date} {month}"
    b = f"{time}"
    c = f"{pm_or_am}"
    d = city
    e = day

# ---------------------------------------SECOND DATE TIME DATA ENDS---------------------------------------------------------------------
    return render_template("search.html", celsius=celsius_temperature, weather=weather_name,
                           celsius_feel=celsius_temperature_feel,
                           date=a, time=int(b), std=c, city_name=d, day=e, humidity=hum, pressure=pre, desc=des,
                           air=wind, id=id_no,
                           next1_t=next1_celsius, next2_t=next2_celsius, next3_t=next3_celsius, next4_t=next4_celsius,
                           id1=id_no1, id2=id_no2,
                           id3=id_no3, id4=id_no4, up_time1=int(weather_time1), up_time2=int(weather_time2),
                           up_time3=int(weather_time3), up_time4=int(weather_time4))


if __name__=="__main__":
    app.run(debug=True)
    #time>7 and time<17:
    #time>4 and time<8 or time>16 and time<19:

    #time>4 and time<8 or time>16 and time<19:

    #    <link rel="stylesheet" href="static/mystyle.css">
