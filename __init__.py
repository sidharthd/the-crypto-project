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

		try:
			# Save uploaded file.
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		except IOError:
			# Create the upload directory if it doesn't exist and then save the file.
			os.makedirs(app.config['UPLOAD_FOLDER'])
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

		encoded_text = process_des(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), passphrase, encryption)

		# Make a response to send the output file for download by the user.
		response = make_response(encoded_text)
		if encryption:
			filename = 'encrypted_' + file.filename
		else:
			filename = 'decrypted_' + file.filename
		response.headers["Content-Disposition"] = "attachment; filename="+filename
		response.mimetype = "text/plain"
		
		return response

	return render_template('des.html')

if __name__ == '__main__':
	app.run(debug = True)