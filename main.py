from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail

with open("config.json","r") as c:
    para= json.load(c)
    params = para["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL='True',
    MAIL_USERNAME =params['gmail_id'],
    MAIL_PASSWORD =params['gmail_password']

)
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = params["local_server"]
db = SQLAlchemy(app)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)

@app.route('/layout')
def layout():
    return render_template('layout.html',params=params)
@app.route('/portfolio_details')
def portfolio_details():
    return render_template('portfolio_details.html',params=params)
@app.route('/blog_single')
def blog_single():
    return render_template('blog_single.html',params=params)
@app.route('/',methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        print('Your Name is: ', name)
        print('Your email is: ', email)
        print('Your phone is: ', phone)
        print('Your message is: ', message)

        entry = Contacts(name=name, email=email, phone=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message(
            "New Message from " + name,
            sender=email,
            recipients=[params['gmail_id']],
            body=message + '\n' + phone
        )


    else:
        print("ERROR........")

    return render_template('index.html',params=params)
app.run(debug=True)