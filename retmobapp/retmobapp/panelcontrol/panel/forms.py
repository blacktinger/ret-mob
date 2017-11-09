# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from flask import render_template, request,Flask,current_app, jsonify
from . import models
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/retmobapp/static/uploads'

class PanelForms(FlaskForm):
	"""docstring for PanelForms"""
	def __init__(self, arg):
		super(PanelForms, self).__init__()
		self.arg = arg
		
class UFileForms(FlaskForm):
	"""docstring for UFileFormsFlaskForm"""
	m_request = request
	def __init__(self, request):
		super(UFileForms,self).__init__()
		self.m_request = request

  	def validate(self):
		if request.method == 'POST':
			file = request.files['kartik-input-705']
			if file and self.allowed_file(file.filename):
				filename = secure_filename(file.filename)
				# 进行散列
				# generate_auth_key
				# save and rename 
				# Databases filter
				# print os.path.join(app.config['UPLOAD_FOLDER'], filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				# print "upload ok"
				return jsonify({'ok':True})
		return abort(403)

	def allowed_file(self,filename):
		ALLOWED_EXTENSIONS=set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 		return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

 	def generate_auth_key():
		return ''.join(random.sample(string.ascii_letters + string.digits, 16))


		