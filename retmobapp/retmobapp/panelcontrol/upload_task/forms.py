# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from flask import render_template, request,Flask,current_app, jsonify,abort
from retmobapp.panelcontrol.tasklist.models import Tasks
from models import FileMap
from werkzeug.utils import secure_filename
from retmobapp.panelcontrol.tasklist import models
import os
import hashlib,random,string

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
				# 使用read()后，文件指针不会回来，要自己seek :https://segmentfault.com/q/1010000008765526
				md5 = hashlib.md5(file.read()).hexdigest()
				file.seek(0, 0)
				# 获取文件后缀
				file_suffix = os.path.splitext(filename)[-1]
				file_url = os.path.join(app.config['UPLOAD_FOLDER'], md5+file_suffix)
				auth_key = self.generate_auth_key()
				file.save(file_url)
				FileMap.create(file_url=file_url, auth_key=auth_key, file_orig_name=filename)
				# print "upload ok"
				return jsonify({'ok':True,
								'auth_key':auth_key})
		return abort(403)

	def allowed_file(self,filename):
		ALLOWED_EXTENSIONS=set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 		return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

 	def generate_auth_key(self):
		return ''.join(random.sample(string.ascii_letters + string.digits, 16))

class CreateTask(FlaskForm):

	def __init__(self,arg):
		super(CreateTask,self).__init__()
		self.arg = arg

	def validate(self):
		# print "===============this is form"
		try:
			task_dic = ['ZIP','IPA','APK']
			plantform_dic = ['Sources', 'iOS', 'Android']
			task_type_str = request.form['task_type']
			if task_type_str.isdigit() == False:
				return abort(403)
			task_type = task_dic[int(task_type_str)]
			task_plantform = plantform_dic[int(task_type_str)]
			auth_key = request.form['auth_key']
			print auth_key,task_type
			filemap = FileMap.query.filter_by(auth_key=auth_key).first()
			if filemap:
				print filemap.file_url, filemap
				Tasks.create(task_plantform=task_plantform, task_type=task_type, filemap_id=filemap.id)
				return jsonify({'ok':True})
			# def __init__(self, task_plantform, task_type,  filemap_id,**kwargs):
		except Exception,e:
			print e
			return abort(403)
		# print "===============this is form"
		return abort(403)





		