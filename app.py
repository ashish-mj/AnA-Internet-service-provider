from initial import app,db,mail
from flask import Flask, render_template ,request,redirect,url_for,session,flash
from flask_login import login_user,login_required,logout_user,current_user
from flask_mail import Message
from database import log_in,plans,customer,customer_plan_info
import stripe


public_key = 'pk_test_6pRNASCoBOKtIshFeQd4XMUh'
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"





##############################################################################################home page
@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')

########################################################################################################about page

@app.route('/about')
def about():
	return render_template('about.html')

##################################################################################################career page

@app.route('/careers')
def careers():
	return render_template('career.html')

###############################################################################################plan page

@app.route('/plans_info')
def plans_info():
	return render_template('plan.html')

############################################################################################contact page

@app.route('/contact',methods=['GET','POST'])
def contact():
	if request.method=='POST':
		name = request.form['name']
		mobile = request.form['mobile']
		email = request.form['email']
		subject = request.form['subject']
		msg = request.form['msg']

		info = Message(subject,sender = "ana.customer1000@gmail.com",recipients = ['akshaynashish.services@gmail.com'])
		info.body = "Name : " + str(name) + "\nMobile Number : " + str(mobile) + '\nEmail : ' + str(email) +'\n'+str(msg)
		mail.send(info)
		return redirect(url_for('contact'))
	return render_template('contact.html')

###############################################################################################login page

@app.route('/welcome')
@login_required
def welcome():
	ID = current_user.id
	cus=customer.query.filter_by(id=ID).first()
	plan=plans.query.filter_by(id=cus.customer_plan.plan_id).first()

	return render_template('welcome.html',name=cus.name,mobile=cus.phone,email=cus.email,plan_name=plan.name,status=cus.customer_plan.status,expiry=cus.customer_plan.expiry,public_key=public_key)

@app.route('/complaint',methods=['GET','POST'])
@login_required
def complaint():
	if request.method=="POST":
		 ID = current_user.id
		 cus = customer.query.filter_by(id=ID).first()

		 subject=request.form['subject']
		 msg = request.form['msg']

		 info = Message(subject,sender = "ana.customer1000@gmail.com",recipients = ['akshaynashish.services@gmail.com'])
		 info.body = 'Name : '+str(cus.name)+'\nUsername : '+str(cus.login.username)+'\nMobile : '+str(cus.phone)+'\nEmail : '+str(cus.email)+'\n'+str(msg)

		 mail.send(info)
		 return redirect(url_for('complaint'))


	return render_template('complaint.html')





@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/payment', methods=['POST'])
@login_required
def payment():

    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=99900,
        currency='INR',
        description='Payment'
    )

    return redirect(url_for('welcome'))




@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		user=log_in.query.filter_by(username=request.form['username']).first()
		
		if user.check_password(request.form['password']) and user is not None:

			login_user(user)

			next = request.args.get('next')

			if next==None or not next[0]=='/':

				next = url_for('welcome')

			return redirect(next)



	return render_template('login.html')



######################################################################################################main function
if __name__ == '__main__':
	app.run(debug=False)
