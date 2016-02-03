from flask import Flask, render_template, request, redirect, make_response
import os

from des import *

UPLOAD_FOLDER = 'user_uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/des/', methods=["GET", "POST"])
def des():
	if request.method == "POST":
		file = request.files['file']
		passphrase = request.form['passphrase']
		encryption = int(request.form['encryption'])
		print encryption
		try:
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		except IOError:
			os.makedirs(app.config['UPLOAD_FOLDER'])
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		return process_des(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), passphrase, encryption)
		'''
		input_file = open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		response = make_response(input_file.read())
		response.headers["Content-Disposition"] = "attachment; filename=encrypted.txt"
		response.mimetype = "text/plain"
		return response
		'''
	return render_template('des.html')

if __name__ == '__main__':
	app.run(debug = True)