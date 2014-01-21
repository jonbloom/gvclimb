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
	cur = g.db.execute('select * from routes order by rating asc,rope')
	routes_toprope = [dict(id=row[0], routeType=row[1], rating=row[2], rope=row[3], name=row[4], dateSet=row[5], setter=row[6]) for row in cur.fetchall() if row[1] == 'toprope']
	routes_boulder = [dict(id=row[0], routeType=row[1], rating=row[2], rope=row[3], name=row[4], dateSet=row[5], setter=row[6]) for row in cur.fetchall() if row[1] == 'boulder']
	return render_template('show_routes.html', routes_toprope=routes_toprope, routes_boulder=routes_boulder)
if __name__ == '__main__':
		app.run()