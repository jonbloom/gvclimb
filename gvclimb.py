import os
import sys
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash

# configuration
DATABASE = 'gvclimb.sqlite'
DEBUG = True
SECRET_KEY = 'devkey'
USERNAME = 'jonbloom'
PASSWORD = 'jB!gv5271'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')
def show_all_routes():
	all_routes = g.db.execute('select * from routes AS r JOIN orderkeys AS k on k.rating = r.rating order by k.key')
	default_colors = g.db.execute('select * from colors')
	routes_toprope = []
	routes_boulder = []
	for row in all_routes:
		# if row[9] == "none":
		# 	base = default_colors[row[2]]
		# else:
		# 	base = row[9]
		if row[1] == "toprope":
			routes_toprope.append(dict(id=row[0], routeType=row[1], rating=row[2], rope=row[3], name=row[4], dateSet=row[5], setter=row[6],tape_div=gen_tape_div("white",row[7],row[8])))
		else:
			routes_boulder.append(dict(id=row[0], routeType=row[1], rating=row[2], rope=row[3], name=row[4], dateSet=row[5], setter=row[6],tape_div=gen_tape_div("white",row[7],row[8])))
	return render_template('show_routes.html', topropes=routes_toprope, boulders=routes_boulder)
def gen_tape_div(base_color,color_1,color_2):
	tape_div = "<div class='color " + base_color +  "' style='background-color:" + base_color + "; width:auto; \height:20px;margin:0 auto; padding:10px'>"
      	if color_1 != 'none':
      		if color_2 == 'none':
      			tape_div =  tape_div + "<div class='color " + color_1 + " fulltape' style='background-color:" + color_1 + "; width:40%; height:20px; margin:0 auto;'></div>"
      		else:
      			tape_div = tape_div +  "<div class='color " + color_1 + " halftape' style='background-color:" + color_1 + "; width:40%; height:20px; margin:0 5%; float:left;'></div><div class='color " + color_2 + " halftape' style='background-color:" + color_2 + "; width:40%; height:20px; margin:0 5%; float:left;'></div>"
      	tape_div = tape_div + "</div>"
      	return tape_div
# class Route(object):
# 	id = 0
# 	route_type = ""
# 	rating = ""
# 	rope = 0
# 	name = ""
# 	date_set = ""
# 	setter = ""
# 	base_color = "none"
# 	color_1 = "none"
# 	color_2 = "none"
# 	special_base = "none"
# 	def __init__(self,route_type,rating,rope,name,date_set,setter,base_color,color_1,color_2,special_base):
# 		self.route_type = route_type
# 		self.rating = rating
# 		self.rope = rope
# 		self.name = name
# 		self.date_set = date_set
# 		self.setter = setter
# 		self.base_color = base_color
# 		self.color_1 = color_1
# 		self.color_2 = color_2
# 		self.special_base = special_base



if __name__ == '__main__':
		app.run()
