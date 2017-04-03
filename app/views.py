from app import app
from flask import Flask, redirect, request, render_template, flash, url_for
from .forms import DataForm

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
		
		return redirect (url_for('play'))

@app.route('/play')
def play():
	return render_template('play.html')

