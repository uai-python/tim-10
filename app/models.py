from app import db

class User(db.Model):
	#__tablename__='User'
	id=db.Column('User_id', db.Integer, primary_key=True)
	usia=db.Column(db.Integer)
	jenis_kelamin=db.Column(db.String(12))
	kota_kabupaten=db.Column(db.String(30))

	def __init__(self,  usia, jenis_kelamin, kota_kabupaten):		
		self.usia=usia
		self.jenis_kelamin=jenis_kelamin
		self.kota_kabupaten=kota_kabupaten


class Soal(db.Model):
	#__tablename__='User'
	id=db.Column('soal_id', db.Integer, primary_key=True)
	soal_nya=db.Column(db.String(300))
	jawaban=db.Column(db.Integer)

	def __init__(self, soal_nya , jawaban):
		self.soal_nya=soal_nya
		self.jawaban=jawaban

class Quiz(db.Model):
	#__tablename__='User'
	id=db.Column('Quiz_id', db.Integer, primary_key=True)
	user_id=db.Column(db.Integer)
	soal_id=db.Column(db.Integer)
	jawaban_user=db.Column(db.Integer)

	def __init__(self, user_id , soal_id, jawaban_user):
		self.user_id=user_id
		self.soal_id=soal_id
		self.jawaban_user=jawaban_user
