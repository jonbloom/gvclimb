import sqlite3
import hashlib
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash

# configuration
DATABASE = 'gvclimb.sqlite'
DEBUG = True
SECRET_KEY = 'devkey'
USERNAME = 'jonbloom'
PASSWORD = 'jb!gv5271'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
	g.db = connect_db()
	g.db.row_factory = sqlite3.Row
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')
def show_all_routes():
	all_routes = g.db.execute('select * from routes as r join orderkeys as k on k.rating = r.rating order by k.key')
	colors = g.db.execute('select * from colors')
	default_colors = colors.fetchone()
	routes_toprope = []
	routes_boulder = []
	for row in all_routes:
		if row[9] == "none":
			base = default_colors[str(row[2])]
		else:
			base = row[9]
		if row[1] == "toprope":
			routes_toprope.append(dict(id=row[0], routeType=row[1], rating=row[2], rope=row[3], name=row[4], dateSet=row[5], setter=row[6],tape_div=gen_tape_div(base,row[7],row[8])))
		else:
			routes_boulder.append(dict(id=row[0], routeType=row[1], rating=row[2], rope=row[3], name=row[4], dateSet=row[5], setter=row[6],tape_div=gen_tape_div(base,row[7],row[8])))
	return render_template('show_routes.html', topropes=routes_toprope, boulders=routes_boulder, colors=default_colors)


@app.route('/add', methods=['GET','POST'])
def add_route():
	if not session.get('logged_in'):
			abort(401)
	all_setters = g.db.execute('select * from setters order by name asc')
	setters = [dict(id=s[0],name=s[1]) for s in all_setters.fetchall()]
	all_colors = g.db.execute('select * from tapeColors')
	colors = [dict(css=c[0],real=c[1]) for c in all_colors.fetchall()]
	if request.method == 'POST':
		g.db.execute('insert into routes values (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', request.form)
		g.db.commit()
	return render_template('add.html',setters=setters, colors=colors)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    password = None
    if request.method == 'POST':
    	username = request.form['username']
    	password = hashlib.md5(request.form['password']).hexdigest()
        checker = g.db.execute("select * from users where username = ?", [username])
        checker = checker.fetchone()

        if checker[2] == password:
            session['logged_in'] = True
            session['logged_in_as'] = username
            session['is_admin'] = checker['is_admin']
            return redirect(url_for('show_all_routes'))
        else:
        	error = "Invalid username or password. Try again."
    return render_template('login.html', error=password)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_all_routes'))

@app.errorhandler(401)
def custom_401(error):
    return render_template('401.html')

def gen_tape_div(base_color,color_1,color_2):
	tape_div = "<div class='color " + base_color +  "' style='background-color:" + base_color + "; height:40px;width:auto;margin:0 auto; padding:10px'>"
      	if color_1 != 'none':
      		if color_2 == 'none':
      			tape_div =  tape_div + "<div class='color " + color_1 + " fulltape' style='background-color:" + color_1 + "; width:40%; height:20px; margin:0 auto;'></div>"
      		else:
      			tape_div = tape_div +  "<div class='color " + color_1 + " halftape' style='background-color:" + color_1 + "; width:40%; height:20px; margin:0 5%; float:left;'></div><div class='color " + color_2 + " halftape' style='background-color:" + color_2 + "; width:40%; height:20px; margin:0 5%; float:left;'></div>"
      	tape_div = tape_div + "</div>"
      	return str(tape_div)

if __name__ == '__main__':
		app.run()
