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
def home():
	all_routes = g.db.execute('select * from routes as r join orderkeys as k on k.rating = r.rating order by k.key')
	colors = g.db.execute('select * from colors')
	default_colors = colors.fetchone()
	routes_toprope = []
	routes_boulder = []
	sent_ids = []
	attempted_ids = []
	status = 'Actions'
	btn_class = ''
	if 'logged_in' in session and session['logged_in']:
		attempted_ids = g.db.execute('select attempted_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		sent_ids = g.db.execute('select sent_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		attempted_ids = list(set([int(i) for i in attempted_ids if i]))
		sent_ids = list(set([int(i) for i in sent_ids if i]))
	for row in all_routes:
		if row[9] == "none":
			base = default_colors[str(row[2])]
		else:  
			base = row[9]
		if int(row[0]) in sent_ids:
			btn_class = 'btn-success'
			status = "Sent"
		elif int(row[0]) in attempted_ids:
			btn_class = 'btn-warning'
			status = "Attempted"
		else:
			btn_class = 'btn-default'
		if row[1] == "toprope":
			routes_toprope.append(dict(id=row[0], routeType=row[1], rating=row[2], 
				rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
				tape_div=gen_tape_div(base,row[7],row[8]),btn_class=btn_class, status=status))
		else:
			routes_boulder.append(dict(id=row[0], routeType=row[1], rating=row[2], 
				rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
				tape_div=gen_tape_div(base,row[7],row[8]),btn_class=btn_class, status=status))
		status = "Action"
	return render_template('show_routes.html', topropes=routes_toprope, boulders=routes_boulder, colors=default_colors)

@app.route('/profile')
def profile():
	all_routes = g.db.execute('select * from routes as r join orderkeys as k on k.rating = r.rating order by k.key')
	colors = g.db.execute('select * from colors')
	default_colors = colors.fetchone()
	routes_attempted = []
	routes_sent = []
	sent_ids = []
	attempted_ids = []
	sent=0
	status = 'Actions'
	btn_class = ''
	if 'logged_in' in session and session['logged_in']:
		attempted_ids = g.db.execute('select attempted_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		sent_ids = g.db.execute('select sent_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		attempted_ids = [int(i) for i in attempted_ids if i]
		sent_ids = [int(i) for i in sent_ids if i]
		for row in all_routes:
			if row[9] == "none":
				base = default_colors[str(row[2])]
			else:  
				base = row[9]
			if row[0] in sent_ids:
				btn_class = 'btn-success'
				status = "Sent"
				routes_sent.append(dict(id=row[0], routeType=row[1], rating=row[2], 
					rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
					tape_div=gen_tape_div(base,row[7],row[8]),btn_class=btn_class, status=status))
			elif int(row[0]) in attempted_ids:
				btn_class = 'btn-warning'
				status = "Attempted"
				routes_attempted.append(dict(id=row[0], routeType=row[1], rating=row[2], 
					rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
					tape_div=gen_tape_div(base,row[7],row[8]),btn_class=btn_class, status=status))
		return render_template('profile.html', attempted=routes_attempted, sent=routes_sent, colors=default_colors)
	else:
		abort(401)



@app.route('/add', methods=['GET','POST'])
def add():
	if 'is_admin' in session and session['is_admin']:
		all_setters = g.db.execute('select * from setters order by name asc')
		setters = [dict(id=s[0],name=s[1]) for s in all_setters.fetchall()]
		all_colors = g.db.execute('select * from tapeColors')
		colors = [dict(css=c[0],real=c[1]) for c in all_colors.fetchall()]
		if request.method == 'POST':
			r_type = request.form['route_type']
			r_rating = request.form['rating']
			r_rope = request.form['rope']
			r_name = request.form['name']
			r_date = request.form['date']
			r_setter = ', '.join(request.form.getlist('setter'))
			r_color1 = request.form['color_1']
			r_color2 = request.form['color_2']
			r_special_base = request.form['special_base']
			r_updater = request.form['updater']
			if r_type is 'toprope':
				rating_string = "5." + r_rating
			else:
				rating_string = r_rating
			r_blurb = r_name + ', ' + rating_string + ', Rope ' + r_rope
			g.db.execute('insert into routes values (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
				[r_type, r_rating, r_rope, r_name, r_date, r_setter,r_color1, r_color2, r_special_base, r_blurb, r_updater])
			g.db.commit()
		return render_template('add.html',setters=setters, colors=colors)
	else:
		abort(401)


@app.route('/edit/<route_id>', methods=['GET','POST'])
def edit(route_id):
	if session.get('is_admin') == 0:
			abort(401)
	all_setters = g.db.execute('select * from setters order by name asc')
	setters = [dict(id=s[0],name=s[1]) for s in all_setters.fetchall()]
	all_colors = g.db.execute('select * from tapeColors')
	colors = [dict(css=c[0],real=c[1]) for c in all_colors.fetchall()]
	route = dict(g.db.execute('select * from routes where id = ?',[route_id]).fetchone())

	if request.method == 'POST':
		r_id = request.form['id']
		r_type = request.form['route_type']
		r_rating = request.form['rating']
		r_rope = request.form['rope']
		r_name = request.form['name']
		r_date = request.form['date']
		r_setter = ', '.join(request.form.getlist('setter'))
		r_color1 = request.form['color_1']
		r_color2 = request.form['color_2']
		r_special_base = request.form['special_base']
		r_updater = request.form['updater']
		if r_type is 'toprope':
			rating_string = "5." + r_rating
		else:
			rating_string = r_rating
		r_blurb = r_name + ', ' + rating_string + ', Rope ' + r_rope
		test_string = "update routes set type = '{1}', rating = '{2}', \
		rope = '{3}', name = '{4}', date = '{5}', setter = '{6}', color_1 = '{7}', \
		color_2 = '{8}', special_base = '{9}', blurb = '{10}', updater = '{11}'  where id = \
		'{12}'".format(r_id[:-1],r_type, r_rating, r_rope, r_name, r_date, r_setter,r_color1, 
			r_color2, r_special_base, r_blurb, r_updater, r_id[:-1])
		g.db.execute(test_string)
		g.db.commit()
		return redirect(url_for('home'))
	return render_template('edit.html',setters=setters, colors=colors,route=route)

@app.route('/attempt/<route_id>/<page>')
def attempt(route_id,page):
	if session.get('logged_in') == 0:
		abort(401)
	else:
		route_id = str(route_id) + ', '
		g.db.execute("update users set attempted_ids = (attempted_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
		g.db.commit()
	return redirect(url_for(page))


@app.route('/unattempt/<route_id>/<page>')
def unatttempt(route_id,page):
	if session.get('logged_in') == 0:
		abort(401)
	else:
		route_id = str(route_id) + ', '
		g.db.execute("update users set attempted_ids = replace(attempted_ids,'{0}','') where username = '{1}'".format(route_id, session.get('logged_in_as')))
		g.db.commit()
	return redirect(url_for(page))


@app.route('/send/<route_id>/<page>')
def send(route_id,page):
	if session.get('logged_in') == 0:
		abort(401)
	else:
		route_id = str(route_id) + ', '
		g.db.execute("update users set sent_ids = (sent_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
		g.db.execute("update users set attempted_ids = (attempted_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
		g.db.commit()
	return redirect(url_for(page))


@app.route('/unsend/<route_id>/<page>')
def unsend(route_id,page):
	if session.get('logged_in') == 0:
		abort(401)
	else:
		route_id = str(route_id) + ', '
		g.db.execute("update users set sent_ids = replace(sent_ids,'{0}','') where username = '{1}'".format(route_id, session.get('logged_in_as')))
		g.db.commit()
	return redirect(url_for(page))

@app.route('/delete/<route_id>/<page>')
def delete(route_id):
	if session.get('is_admin') == 0:
		abort(401)
	else:
		g.db.execute("delete from routes where id = ?",[route_id])
		g.db.commit()
	return redirect(url_for(page))

@app.route('/admin')
def admin():
	all_setters = g.db.execute('select * from setters order by name asc')
	setters = [dict(id=s[0],name=s[1]) for s in all_setters.fetchall()]
	return render_template('admin.html', setters=setters)
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
            return redirect(url_for('home'))
        else:
        	error = "Invalid username or password. Try again."
    return render_template('login.html', error=password)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('is_admin', None)
    return redirect(url_for('home'))

@app.errorhandler(401)
def custom_401(error):
    return render_template('401.html')

@app.errorhandler(404)
def custom_404(error):
	return render_template('404.html')
def gen_tape_div(base_color,color_1,color_2):
	tape_div = "<div class='tape color {0}' style='background-color:{0}; height:100%;width:auto;margin:0 auto; padding:10px'>".format(base_color)
      	if color_1 != 'none':
      		if color_2 == 'none':
      			tape_div =  tape_div + "<div class='color {0} fulltape' style='background-color:{0}; width:40%; height:20px; margin:0 auto;'></div>".format(color_1)
      		else:
      			tape_div = tape_div +  "<div class='color {0} halftape' style='background-color:{0}; width:40%; height:20px; margin:0 5%; float:left;'></div> \
      			<div class='color {1} halftape' style='background-color:{1}; width:40%; height:20px; margin:0 5%; float:left;'></div>".format(color_1,color_2)
      	tape_div = tape_div + "</div>"
      	return str(tape_div)


@app.route('/tape/<rating>/<special_base>/<color_1>/<color_2>')
def tape_preview(rating,special_base,color_1,color_2):
	colors = g.db.execute('select * from colors')
	default_colors = colors.fetchone()
	if special_base == "none":
		base_color = default_colors[str(rating)]
	else:  
		base_color = special_base
	return gen_tape_div(base_color,color_1,color_2)


if __name__ == '__main__':
		app.run()
