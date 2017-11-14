# -*- coding: utf-8 -*-
"""Tasks models."""
import datetime as dt

from retmobapp.database import Column, Model, SurrogatePK, db, reference_col, relationship
from retmobapp.extensions import bcrypt
from retmobapp.panelcontrol.upload_task import models

class Tasks(SurrogatePK, Model):
	"""docstring for Tasks"""
	__tablename__ = 'tasks'
	task_plantform = Column(db.String(30), nullable=False)
	task_type = Column(db.String(30), nullable=False)
	# task_uploads_url = Column(db.String(128),nullable=False)
	filemap_id = reference_col('filemap',nullable=False)
	filemap = relationship('FileMap',backref='tasks')
	task_create_time = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
	task_status = Column(db.Integer, nullable=False, default=0)

	# def __init__(self, arg):
	# 	super(Tasks, self).__init__()
	# 	pass
	def __init__(self, task_plantform, task_type,  filemap_id,**kwargs):
		"""Create instance."""
		db.Model.__init__(self, task_plantform=task_plantform, task_type=task_type, filemap_id=filemap_id ,**kwargs)
        # super(Tasks, self).__init__()
 #        # self.arg = arg

class Appinfo(SurrogatePK, Model):
	"""docstring for Appinfo"""
	__tablename__ = 'appinfo'
	task_id = reference_col('tasks',nullable=False)
	task = relationship('Tasks',backref='appinfo')
	file_name = Column(db.String(128),nullable=False)
	file_size = Column(db.Integer,nullable=False)
	file_create_time = Column(db.DateTime, nullable=False)
	file_md5 = Column(db.String(60),nullable=False)
	file_sha256 = Column(db.String(60),nullable=False)
	app_name = Column(db.String(30),nullable=True)
	app_executable_file = Column(db.String(30),nullable=True)
	app_packid = Column(db.String(30),nullable=True)
	app_miniosversion = Column(db.String(30),nullable=True)
	is_encrypted = Column(db.Boolean,nullable=True,default=False)
	file_hierachy = Column(db.String(128),nullable=True)

	def __init__(self, file_name, file_size, file_md5, file_sha256, app_name, app_executable_file, app_packid,**kwargs):
		"""Create instance."""
		db.Model.__init__(self, file_name=file_name, file_size=file_size, file_md5=file_md5, file_sha256=file_sha256, app_name=app_name, app_executable_file=app_executable_file, app_packid=app_packid,**kwargs)
				