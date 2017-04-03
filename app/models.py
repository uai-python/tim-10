from app import db

class User(db.Model):
	#__tablename__='User'
	id=db.Column('User_id', db.Integer, primary_key=True)
	usia=db.Column(db.Integer)
	jenis_kelamin=db.Column(db.String(12))
	kota_kabupaten=db.Column(db.String(30))

	def __init__(self, usia, jenis_kelamin, kota_kabupaten):
		self.usia=usia
		self.jenis_kelamin=jenis_kelamin
		self.kota_kabupaten=kota_kabupaten
