from initial import db,login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash

####################

@login_manager.user_loader
def load_user(user_id):
	return log_in.query.get(user_id)




#####################
class customer(db.Model):                                      #customer table
	
	__tablename__ = "customer"

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.Text)
	address = db.Column(db.Text)
	phone = db.Column(db.Integer)
	email = db.Column(db.Text,unique=True)

	login = db.relationship('log_in', backref='customer',uselist=False)
	customer_plan = db.relationship('customer_plan_info', backref='customer',uselist=False)


	def __init__(self, name, address, phone, email):

		self.name = name
		self.address = address
		self.phone = phone
		self.email = email


class log_in(db.Model,UserMixin):                                         #log_in table
	
	__tablename__ = "log_in"

	id = db.Column(db.Integer,db.ForeignKey('customer.id'),primary_key=True)
	username = db.Column(db.Text,unique=True)
	password = db.Column(db.Text)

	def __init__(self, customer_id,username, password):

		self.id = customer_id
		self.username = username
		self.password = password

	def check_password(self,password):
		return check_password_hash(self.password,password)

class customer_plan_info(db.Model):                                  #Customer's plan information
	
    __tablename__ = "customer_plan_info"

    id = db.Column(db.Integer,db.ForeignKey('customer.id'),primary_key=True)
    plan_id = db.Column(db.Integer,db.ForeignKey('plans.id'))
    status =  db.Column(db.Text)
    expiry = db.Column(db.Text)

    def __init__(self,customer_id,plan_id,status,expiry):

        self.id = customer_id
        self.plan_id = plan_id
        self.status = status
        self.expiry = expiry
		

class plans(db.Model):                                               #plans information
	
    __tablename__ = "plans"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    speed = db.Column(db.Text)
    cost = db.Column(db.Integer)
    limit = db.Column(db.Text)

    customer_plan = db.relationship('customer_plan_info', backref='plans',lazy='dynamic')


    def __init__(self, name, speed, cost, limit):

    	self.name=name
    	self.speed=speed
    	self.cost=cost
    	self.limit=limit
		