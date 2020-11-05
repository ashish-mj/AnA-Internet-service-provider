import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager







basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

#############################################################################################configurations
app.config['SECRET_KEY']='mykey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='ana.customer1000@gmail.com'
app.config['MAIL_PASSWORD']='sooleinchara'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['TESTING']=False

###################################################################################################
db=SQLAlchemy(app)
Migrate(app,db)
mail=Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)




