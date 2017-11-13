# -*- coding: utf-8 -*-
"""Panel views."""
from flask import Blueprint, render_template, request,Flask,current_app
from werkzeug.utils import secure_filename
import os
from forms import PanelForms,UFileForms
from flask import jsonify
from flask_wtf.csrf import CSRFProtect

blueprint = Blueprint('upload_task', __name__, url_prefix='/upload_task', static_folder='../static')


@blueprint.route('/')
def upload_task():
    """List members."""
    form = PanelForms(request.form)
    return render_template('panelcontrol/upload_task.html',form=form)

# 上传文件
@blueprint.route('/upload', methods=['POST'])
def upload():
    ufile = UFileForms(request)
    return ufile.validate()

# 创建task
# @blueprint.route('/create_task')
	