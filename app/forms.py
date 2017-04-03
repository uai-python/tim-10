from flask_wtf import Form
from wtforms import StringField, IntegerField, widgets, FieldList, RadioField, SelectField
from wtforms.validators import DataRequired


class DataForm(Form):
	usia = IntegerField('usia')
	jenis_kelamin = RadioField('jenis_kelamin', choices=[('Laki- laki', 'Laki- laki'),('Perempuan', 'Perempuan')], default='Laki- laki')
	list_of_kotakab=['Jakarta Selatan', 'Jakarta Utara', 'Jakarta Barat', 'Jakarta Timur', 'Jakarta Pusat']
	kotakab=[(x,x) for x in list_of_kotakab]
	kota_kabupaten = SelectField('kota_kabupaten', choices=kotakab)
