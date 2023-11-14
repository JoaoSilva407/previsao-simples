from flask import Flask, render_template, request
import requests

apiKey = '957cbb2d77eed6cb164b9bcd3edfe80d'

app = Flask(__name__)

@app.route("/")
def homepage() :
    return render_template("homepage.html", class_div="hide")

@app.route("/mostrar", methods=["POST", "GET"])
def mostrar() :
    city_name = request.form['city-name']
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={apiKey}&lang=pt_br"

    resp = requests.get(link)
    data = resp.json()

    if resp.status_code == 200 :

        city = data['name']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        icon_temp = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
        humidity= data['main']['humidity']
        speed = data['wind']['speed']
        country = f"https://flagsapi.com/{data['sys']['country']}/flat/64.png"

        return render_template("homepage.html",
                           city=city,
                           country=country,
                           temperatura=int(temp),
                           description=description,
                           icon_temp=icon_temp,
                           humidity=humidity,
                           speed=int(speed*3.6),
                           class_div=''
                           )
    else :
        return render_template("homepage.html", class_div='hide')

if __name__ == "__main__" :
    app.run(debug=True)


