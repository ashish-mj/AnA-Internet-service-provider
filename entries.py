from app import db
from database import customer,log_in,customer_plan_info,plans

db.create_all()
################################################
basic = plans('Basic','10 Mbps',599,'250 GB')
premium = plans('Premium','25 Mbps',799,'500 GB')                    #Plans entries
elite = plans('Elite','50 Mbps',999,'750 GB')

db.session.add_all([basic,premium,elite])
db.session.commit()

###################################################

ashish = customer('Ashish M J','#41 KD road Shantinagar,Mysuru-15',9898989898,'ashm.jagadeesh@gmail.com')
akshay = customer('Akshay Kumar','#107/A 7th main Ullasnagar,Mysuru-27',9797979797,'akshaydhage35@gmail.com')      #Customers entries
mithun = customer('Mithun H R','#4 11th street NNpuram,Mysuru-04',8989898989,'mithunhr201@gmail.com')
pavan = customer('Pavan Hatwar','#92 Subashnagar TK layout,Mysuru-11',7676767676,'pavanhatwar65@gmail.com')

db.session.add_all([ashish,akshay,mithun,pavan])
db.session.commit()

###################################################

basic = plans.query.filter_by(name='Basic').first()
premium = plans.query.filter_by(name='Premium').first()                   #queries for login and customers
elite = plans.query.filter_by(name='Elite').first()


ashish = customer.query.filter_by(name='Ashish M J').first()
akshay = customer.query.filter_by(name='Akshay Kumar').first()
mithun = customer.query.filter_by(name='Mithun H R').first()
pavan = customer.query.filter_by(name='Pavan Hatwar').first()
 

###########################################################

ashish_plan = customer_plan_info(ashish.id, elite.id, 'Active', '15 June 2020')
akshay_plan = customer_plan_info(akshay.id, premium.id, 'Active', '22 June 2020')       #customers plan information entries
mithun_plan = customer_plan_info(mithun.id, basic.id, 'Active', '10 June 2020')
pavan_plan = customer_plan_info(pavan.id, basic.id, 'Active', '25 June 2020')

db.session.add_all([ashish_plan,akshay_plan,mithun_plan,pavan_plan])
db.session.commit()


###########################################################


ashish_login = log_in(ashish.id,'MYS001','pbkdf2:sha256:150000$CZZ5tOrf$ac64fadbbdaa2213e1c9e9d27e87c4cffe245daa6d2e0657395536246c1ad2ed')
akshay_login = log_in(akshay.id,'MYS002','pbkdf2:sha256:150000$CZZ5tOrf$ac64fadbbdaa2213e1c9e9d27e87c4cffe245daa6d2e0657395536246c1ad2ed')                                             #login entries
mithun_login = log_in(mithun.id,'MYS003','pbkdf2:sha256:150000$CZZ5tOrf$ac64fadbbdaa2213e1c9e9d27e87c4cffe245daa6d2e0657395536246c1ad2ed')
pavan_login = log_in(pavan.id,'MYS004','pbkdf2:sha256:150000$CZZ5tOrf$ac64fadbbdaa2213e1c9e9d27e87c4cffe245daa6d2e0657395536246c1ad2ed')

db.session.add_all([ashish_login,akshay_login,mithun_login,pavan_login])
db.session.commit()

##########################################################