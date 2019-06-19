from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *


@app.route("/")
def ping():
	return "ping resp"
#register and login
@app.route("/register",methods=['POST'])
def register():
	email_ = request.form['email']
	password_ = request.form['password']
	name_ = request.form['name']
	location_ = request.form['location']
	gender_ = request.form['gender']
	interest_ = request.form['interest']
	college_ = request.form['college']
	print(email_)
	print(password_)
	try:
		credentials = Credentials(email = email_, password = password_)
		db.session.add(credentials)
		db.session.commit()
		profile = User_Profile(email = email_,name = name_,location = location_,gender = gender_,interest = interest_,college = college_)
		db.session.add(profile)
		db.session.commit()
		return"ok"
		
	except Exception as e:
		return str(e)

@app.route("/login")
def login():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			return "True"
		else:
			return "False"
	except Exception as e:
		print(str(e))
		return "False"
#setter functions

@app.route("/enroll", methods=['POST'])
def enroll():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			enrollment = Enrollment(
					mentee = email,
					mentor = request.form['mentor'],
					status = False,
					topic_name = request.form['topic_name']
				)
			notif = Notification(
					sender = email,
					recipient = request.form['mentor'],
					request = False,
					topic_name = request.form['topic_name']
				)
			db.session.add(enrollment)
			db.session.commit()
			db.session.add(notif)
			db.session.commit()
			return "Ture"
		else:
			return "False"
	except Exception as e:
		print(str(e))
		return "False"
@app.route("/add_timeline", methods=['POST'])
def add_timeline():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			timeline = Timeline(
					topic_name = request.form['topic_name'],
					day = request.form['day'],
					goal = request.form['goal'],
					mentor = request.form['email']
				)
			db.session.add(timeline)
			db.session.commit()
			return 'True'
		else:
			return 'False'
	except Exception as e:
		print(str(e))
		return 'False'
@app.route("/add_mentor", methods=['POST'])
def add_mentor():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			mentor = Mentor_list(
					topic_name = request.form['topic_name'],
					email = request.form['email']
				)
			db.session.add(mentor)
			db.session.commit()
			return 'True'
		else:
			return 'False'
	except Exception as e:
		print(str(e))
		return 'False'
@app.route("/add_topics", methods=['POST'])
def new_topic():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			topic = Topics(
					topic_name = request.form['topic_name']
				)
			db.session.add(topic)
			db.session.commit()
			return "True"
		else:
			return "False"
	except Exception as e:
		print(str(e))
		return "False"
@app.route("/add_request", methods=['POST'])
def new_request():
	email = request.form['email']
	password = request.form['password']
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			req = New_requests(
					topic_name = request.form['topic_name'],
					requester =  email
				)
			db.session.add(req)
			db.session.commit()
			return "True"
		else:
			return "False"
	except Exception as e:
		return(str(e))
#getter functions

@app.route("/profile")
def profile():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			profile = User_Profile.query.filter_by(email = email).first()
			print(str(profile))
			dict={
					"email": str(profile.email),
					"name": str(profile.name),
					"interest": str(profile.interest),
					"location": str(profile.location),
					"gender" :str(profile.gender),
					"college": str(profile.college)
				}
			return jsonify(dict)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)
@app.route("/get_topics")
def topic_list():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			topics = Topics.query.all()
			topic_list={}
			i=0
			for topic in topics:
				print(str(topic.topic_name))
				topic_list.update({str(i):str(topic.topic_name)})
				i+=1
			return jsonify(topic_list)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)
@app.route("/get_mentor_details")
def mentor_details():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			details = Enrollment.query.filter_by(mentor= email).all()
			print(str(details))
			detail_list={}
			i=0
			for detail in details:
				print(str(detail))
				detail_list.update({str(i):{"mentee":str(detail.mentee),"topic":str(detail.topic_name),"status":str(detail.status)}})
				i+=1
			return jsonify(detail_list)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)
@app.route("/get_mentee_details")
def mentee_details():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			details = Enrollment.query.filter_by(mentee= email).all()
			print(str(details))
			detail_list={}
			i=0
			for detail in details:
				print(str(detail))
				detail_list.update({str(i):{"mentee":str(detail.mentor),"topic":str(detail.topic_name),"status":str(detail.status)}})
				i+=1
			return jsonify(detail_list)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)

@app.route("/get_timeline")
def get_timeline():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			details = Timeline.query.filter_by(mentor= request.form['mentor']).filter_by(topic_name =request.form['topic_name'] ).all()
			print(str(details))
			detail_list={}
			i=0
			for detail in details:
				print(str(detail))
				detail_list.update({str(i):{"day":str(detail.day),"goal":str(detail.goal),"topic":str(detail.topic_name)}})
				i+=1
			return jsonify(detail_list)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)
@app.route("/get_notifications")
def get_notifications():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			details = Notification.query.filter_by(recipient= request.form['email']).all()
			print(str(details))
			detail_list={}
			i=0
			for detail in details:
				print(str(detail))
				detail_list.update({str(i):{"sender":str(detail.sender),"details":str(detail.topic_name)}})
				i+=1
			return jsonify(detail_list)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)
@app.route("/get_mentors")
def get_mentors():
	email = request.form['email']
	password = request.form['password']
	print(email, password)
	try:
		credentials=Credentials.query.filter_by(email = email).first()
		if password == str(credentials.password):
			details = Mentor_list.query.all()
			print(str(details))
			detail_list={}
			i=0
			for detail in details:
				print(str(detail))
				detail_list.update({str(i):{"mentor":str(detail.email),"topic_name":str(detail.topic_name)}})
				i+=1
			return jsonify(detail_list)
		else:
			return "failed"
	except Exception as e:
		print(str(e))
		return str(e)

# change status, get request list ,add request, remove request
migrate = Migrate(app, db)
if __name__ == '__main__':
	app.run()
#localhost:5000/register?email="root"&password="root"&name="qwerty"&location="qwerty"&gender="male"&interest="qwerty"&college="qwerty"
#curl -v -H "Content-Type: application/json" -X POST \ -d '{"email":"root","password":"root","name":"qwerty","location":"qwerty","gender":"male","interest":"qwerty","college":"qwerty"}' http://127.0.0.1:5000/register