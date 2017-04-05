from app import app, db
from flask import Flask, redirect, request, render_template, flash, url_for
from .forms import DataForm, JawabanForm
from .models import User, Soal, Quiz
import random
userr=0
b=0
c=0
@app.route('/')
#@app.route('/index')
def index():

	return render_template('index.html', title='Selamat datang!')

@app.route('/fillData', methods=['GET', 'POST'])
def fillData():
	form=DataForm()
	return render_template('fillData.html', title='Data diri', form=form)

@app.route('/failedInput', methods=['GET', 'POST'])
def failedInput():
	form=DataForm()
	return render_template('failedInput.html', title='Data diri', form=form)

@app.route('/simpanData', methods=['POST'])
def simpanData():
	if request.form['usia']=="":
		return redirect (url_for('failedInput'))
	else:
		usia=request.form['usia']
		jenis_kelamin=request.form['jenis_kelamin']
		kota_kabupaten=request.form['kota_kabupaten']
		user=User(usia, jenis_kelamin, kota_kabupaten)
		db.create_all()
		db.session.add(user)
		db.session.commit()
		global userr
		userr=user.id
		return redirect (url_for('play_1'))

@app.route('/play_1')
def play_1():
	#for i in range(10):
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	#b=Soal.query.filter_by(Soal.id=a),
	global b
	global c

	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	
	return render_template('play_1.html',  soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_2' , methods=['POST'])
def play_2():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_2.html',  soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_3', methods=['POST'])
def play_3():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_3.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_4', methods=['POST'])
def play_4():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_4.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_5', methods=['POST'])
def play_5():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_5.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_6', methods=['POST'])
def play_6():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_6.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_7', methods=['POST'])
def play_7():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_7.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_8', methods=['POST'])
def play_8():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_8.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/play_9', methods=['POST'])
def play_9():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_9.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)
@app.route('/play_10', methods=['POST'])
def play_10():
	global b
	global c
	soal_id=str(b).replace(",", "").replace("(","").replace(")", "")
	user_id=str(userr).replace("u", "").replace("'", "")
	jawaban_user=request.form['angka_jawaban']
	quiz=Quiz(user_id,soal_id, jawaban_user)
	db.create_all()
	db.session.add(quiz)
	db.session.commit()
	
	jwbform=JawabanForm()
	a= random.randrange(1, db.session.query(Soal.id).count())
	b=db.session.query(Soal.id)[a]	
	c=db.session.query(Soal.soal_nya)[a]
	return render_template('play_10.html', soal2=b, soal3=c, users=userr, view=False, form=jwbform)

@app.route('/dashboard', methods=['POST'])
def dashboard():
	return render_template('dashboard.html', query=db.session.query(Quiz), userid=str(userr).replace("u", "").replace("'", ""))


@app.route('/finish', methods=['POST'])
def finish():
	return render_template('finish.html')

