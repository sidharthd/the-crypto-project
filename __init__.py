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
		if not (file.content_type == 'text/plain' or file.content_type == 'application/pdf'):
			return render_template('des.html', error='Filetype not supported. Please upload a text file or PDF file.')
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

		# Delete the file from server.
		os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

		# Check if file empty error is set.
		if encoded_text == 'file_empty_error':
			return render_template('des.html', error = 'The file was empty. Please upload a non-empty file.')

		# Return error if file was not a properly encrypted file.
		if encoded_text == 'not_encrypted_file':
			return render_template('des.html', error = 'Oops! The file you uploaded does not seem to be a properly encrypted one.')

		# Make a response to send the output file for download by the user.
		response = make_response(encoded_text)
		if encryption:
			filename = 'encrypted_' + file.filename
		else:
			filename = 'decrypted_' + file.filename
		response.headers["Content-Disposition"] = "attachment; filename="+filename
		response.mimetype = "text/plain"
		
		return response

	return render_template('des.html', error=None)

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0')