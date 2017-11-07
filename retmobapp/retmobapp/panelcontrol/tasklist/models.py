# -*- coding: utf-8 -*-
"""Tasks models."""
import datetime as dt

from retmobapp.database import Column, Model, SurrogatePK, db, reference_col, relationship
from retmobapp.extensions import bcrypt

class Tasks(SurrogatePK, Model):
	"""docstring for Tasks"""
	__tablename__ = 'tasks'
	task_plantform = Column(db.String(30), nullable=False)
	task_type = Column(db.String(30), nullable=False)
	task_uploads_url = Column(db.String(128),nullable=False)
	task_create_time = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
	task_status = Column(db.Integer, nullable=False, default=0)

	def __init__(self, arg):
		super(Tasks, self).__init__()
		pass
	# def __init__(self, task_plantform, task_type, task_uploads_url ,**kwargs):
	# 	"""Create instance."""
 #        db.Model.__init__(self, task_plantform=task_plantform, task_type=task_type, task_uploads_url=task_uploads_url ,**kwargs)
 #        # super(Tasks, self).__init__()
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
	app_name = Column(db.String(30),nullable=False)
	app_executable_file = Column(db.String(30),nullable=False)
	app_packid = Column(db.String(30),nullable=True)
	app_miniosversion = Column(db.String(30),nullable=True)
	is_encrypted = Column(db.Integer,nullable=False)
	file_hierachy = Column(db.String(128),nullable=True)

	def __init__(self, arg):
		super(Appinfo, self).__init__()
		self.arg = arg
		