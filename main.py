from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail


with open("config.json","r") as c:
    para= json.load(c)
    params = para["params"]

app = Flask(__name__)
   



@app.route('/layout')
def layout():
    return render_template('layout.html',params=params)
@app.route('/portfolio_details')
def portfolio_details():
    return render_template('portfolio_details.html',params=params)
@app.route('/blog_single')
def blog_single():
    return render_template('blog_single.html',params=params)
@app.route('/')
def index():
    return render_template('index.html',params=params)
app.run()
