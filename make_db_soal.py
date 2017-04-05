from app import db
from app.models import Soal

f= open('soal.txt')
line_no = int(f.readline())
for line in range(line_no):
	soal_nya = f.readline()
	jawaban = f.readline()
	soal=Soal( soal_nya, jawaban)
	db.create_all()
	db.session.add(soal)
	db.session.commit()
