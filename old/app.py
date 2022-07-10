from scraper import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    city = request.form.get('')
    w = Weather()
    forecast = w.forecast()
    return render_template('index.html', forecast=forecast, city=city)

if __name__ == "__main__":
    app.run(debug=True)
