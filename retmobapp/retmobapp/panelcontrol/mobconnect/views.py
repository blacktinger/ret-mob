# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, Flask
from flask import jsonify

blueprint = Blueprint('mobconnect', __name__, url_prefix='/mobconnect', static_folder='../static')

@blueprint.route('/')
def mobcon():
	return render_template('panelcontrol/mobcon.html')

@blueprint.route('/replay',methods=['POST'])
def replay():
	if request.method == 'POST':
		print "suprise motherfuck"

	return jsonify({'statu':True})