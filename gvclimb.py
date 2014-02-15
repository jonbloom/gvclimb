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
	all_routes = g.db.execute('select r.*, k.key from routes as r join orderkeys as k on k.rating = r.rating order by k.key')
	colors = g.db.execute('select * from colors')
	default_colors = colors.fetchone()
	routes_toprope = []
	routes_boulder = []
	sent_ids = []
	attempted_ids = []
	voted_ids = []
	status = 'Actions'
	btn_class = ''
	if 'logged_in' in session and session['logged_in']:
		attempted_ids = g.db.execute('select attempted_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		sent_ids = g.db.execute('select sent_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		voted_ids = g.db.execute('select vote_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		attempted_ids = [int(i) for i in attempted_ids if i]
		sent_ids = [int(i) for i in sent_ids if i]
		votev_ids = [int(i) for i in voted_ids if i]
	for row in all_routes:
		voted = str(False)
		if int(row[0]) in voted_ids:
			voted = str(True)
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
				tape_div=gen_tape_div(base,row[7],row[8]),sort=row[12],btn_class=btn_class, status=status, voted=voted))
		else:
			routes_boulder.append(dict(id=row[0], routeType=row[1], rating=row[2], 
				rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
				tape_div=gen_tape_div(base,row[7],row[8]),sort=row[12],btn_class=btn_class, status=status, voted=voted))
		status = "Action"
		
	return render_template('show_routes.html', topropes=routes_toprope, boulders=routes_boulder, colors=default_colors)


@app.route('/profile')
def profile():
	require_logged_in()
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
	attempted_ids = g.db.execute('select attempted_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
	sent_ids = g.db.execute('select sent_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
	voted_ids = g.db.execute('select vote_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
	attempted_ids = [int(i) for i in attempted_ids if i]
	sent_ids = [int(i) for i in sent_ids if i]
	voted_ids = [int(i) for i in voted_ids if i]
	for row in all_routes:
		voted = str(False)
		if int(row[0]) in voted_ids:
			voted = str(True)
		if row[9] == "none":
			base = default_colors[str(row[2])]
		else:  
			base = row[9]
		if row[0] in sent_ids:
			btn_class = 'btn-success'
			status = "Sent"
			routes_sent.append(dict(id=row[0], routeType=row[1], rating=row[2], 
				rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
				tape_div=gen_tape_div(base,row[7],row[8]),btn_class=btn_class, status=status, voted=voted))
		elif int(row[0]) in attempted_ids:
			btn_class = 'btn-warning'
			status = "Attempted"
			routes_attempted.append(dict(id=row[0], routeType=row[1], rating=row[2], 
				rope=row[3], name=row[4], dateSet=row[5], setter=row[6],
				tape_div=gen_tape_div(base,row[7],row[8]),btn_class=btn_class, status=status, voted=voted))
		
	return render_template('profile.html', attempted=routes_attempted, sent=routes_sent, colors=default_colors)

@app.route('/comm')
def comm():
	voted_routes = g.db.execute("select r.*, c.num_votes from routes r, route_comm c where r.id = c.route_id;").fetchall()
	routes = []
	colors = g.db.execute('select * from colors')
	default_colors = colors.fetchone()
	sent_ids = []
	attempted_ids = []
	voted_ids = []
	status = 'Actions'
	btn_class = ''
	if 'logged_in' in session and session['logged_in']:
		attempted_ids = g.db.execute('select attempted_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		sent_ids = g.db.execute('select sent_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		voted_ids = g.db.execute('select vote_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
		voted_ids = [int(i) for i in voted_ids if i]
		attempted_ids = list(set([int(i) for i in attempted_ids if i]))
		sent_ids = list(set([int(i) for i in sent_ids if i]))

	for v_route in voted_routes:
		voted = str(False)
		if v_route[12] > 0:
			if int(v_route[0]) in voted_ids:
				voted = str(True)
			if v_route[9] == "none":
				base = default_colors[str(v_route[2])]
			else:  
				base = v_route[9]
			if int(v_route[0]) in sent_ids:
				btn_class = 'btn-success'
				status = "Sent"
			elif int(v_route[0]) in attempted_ids:
				btn_class = 'btn-warning'
				status = "Attempted"
			else:
				btn_class = 'btn-default'
			routes.append(dict(id=v_route[0], routeType=v_route[1], rating=v_route[2], 
				rope=v_route[3], name=v_route[4], dateSet=v_route[5], setter=v_route[6],
				tape_div=gen_tape_div(base,v_route[7],v_route[8]), votes=v_route[12],btn_class=btn_class, status=status, voted=voted))
			status = "Action"
			
	return render_template('comm.html', routes=routes)

@app.route('/admin')
def admin():
	require_logged_in()
	require_admin()
	all_setters = g.db.execute('select * from setters order by name asc')
	setters = [dict(id=s[0],name=s[1]) for s in all_setters.fetchall()]
	split = len(setters)/4+1
	setters1 = setters[:split]
	setters2 = setters[split:split*2]
	setters3 = setters[split*2:split*3]
	setters4 = setters[split*3:]
	default_colors = g.db.execute('select * from colors')
	default_colors = dict(default_colors.fetchone())
	tape_colors = g.db.execute('select * from tapeColors')
	tape_colors = [dict(css=c[0],real=c[1]) for c in tape_colors.fetchall()]
	return render_template('admin.html', setters1=setters1, setters2=setters2, setters3=setters3, setters4=setters4, default_colors=default_colors, tape_colors=tape_colors)

@app.route('/add', methods=['GET','POST'])
def add():
	require_logged_in()
	require_admin()
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


@app.route('/edit/<route_id>', methods=['GET','POST'])
def edit(route_id):
	require_logged_in()
	require_admin()
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
	require_logged_in()
	route_id = str(route_id) + ', '
	g.db.execute("update users set attempted_ids = (attempted_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
	g.db.commit()
	return redirect(url_for(page))


@app.route('/unattempt/<route_id>/<page>')
def unatttempt(route_id,page):
	require_logged_in()
	route_id = str(route_id) + ', '
	g.db.execute("update users set attempted_ids = replace(attempted_ids,'{0}','') where username = '{1}'".format(route_id, session.get('logged_in_as')))
	g.db.commit()
	return redirect(url_for(page))


@app.route('/send/<route_id>/<page>')
def send(route_id,page):
	require_logged_in()
	route_id = str(route_id) + ', '
	g.db.execute("update users set sent_ids = (sent_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
	g.db.execute("update users set attempted_ids = (attempted_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
	g.db.commit()
	return redirect(url_for(page))


@app.route('/unsend/<route_id>/<page>')
def unsend(route_id,page):
	require_logged_in()
	route_id = str(route_id) + ', '
	g.db.execute("update users set sent_ids = replace(sent_ids,'{0}','') where username = '{1}'".format(route_id, session.get('logged_in_as')))
	g.db.commit()
	return redirect(url_for(page))

@app.route('/delete/<route_id>/<page>')
def delete(route_id):
	require_logged_in()
	require_admin()
	g.db.execute("delete from routes where id = ?",[route_id])
	g.db.commit()
	return redirect(url_for(page))

@app.route('/comm/vote/<route_id>/<page>')
def comm_vote(route_id,page):
	require_logged_in()
	route_info = g.db.execute("select * from route_comm where route_id = ?;",[route_id]).fetchall();
	voted_ids = g.db.execute('select vote_ids from users where username = ?', [session['logged_in_as']]).fetchone()[0].split(', ')
	voted_ids = [int(i) for i in voted_ids if i]
	if not len(route_info) > 0:
		g.db.execute("insert into route_comm values(?, 1);",[route_id])
	if int(route_id) in voted_ids:
		g.db.execute("update route_comm set num_votes = num_votes - 1 where route_id = ?;",[route_id])
		route_id = str(route_id) + ', '
		g.db.execute("update users set vote_ids = replace(vote_ids,'{0}','') where username = '{1}'".format(route_id, session.get('logged_in_as')))
	else:
		g.db.execute("update route_comm set num_votes = num_votes + 1 where route_id = ?;",[route_id])
		route_id = str(route_id) + ', '
		g.db.execute("update users set vote_ids = (vote_ids || '{0}') where username = '{1}'".format(route_id,session.get('logged_in_as')))
		
	g.db.commit()
	return redirect(url_for(page))
@app.route('/comm/reset/<route_id>')
def comm_reset(route_id):
	require_admin()
	route_info = g.db.execute("select * from route_comm where route_id = ?;",[route_id]).fetchall();
	if len(route_info) > 0:
		g.db.execute("update route_comm set num_votes = 0 where route_id = ?;",[route_id])
		g.db.commit()
	else:
		g.db.execute("insert into route_comm values(?, 0);",[route_id])
		g.db.commit()
	return redirect(url_for('comm'))



@app.route('/update_colors', methods=['GET', 'POST'])
def update_colors():
	require_logged_in()
	require_admin()
	default_colors = g.db.execute('select * from colors')
	default_colors = dict(default_colors.fetchone())
	c_V0 = request.form['V0']
	c_V1 = request.form['V1']
	c_V2 = request.form['V2']
	c_V3 = request.form['V3']
	c_V4 = request.form['V4']
	c_V5 = request.form['V5']
	c_V6 = request.form['V6']
	c_V7 = request.form['V7']
	c_V8 = request.form['V8']

	g.db.execute("update colors set '7' = '{}', '8' = '{}', '9' = '{}', '10a' = '{}', '10b' = '{}', '10c' = '{}', '10d' = '{}',  \
		'11a' = '{}', '11b' = '{}', '11c' = '{}', '12d' = '{}', \
		'12a' = '{}', '12b' = '{}', '12c' = '{}', '12d' = '{}', \
		'V0' = '{}', 'V1' = '{}', 'V2' = '{}', 'V3' = '{}', 'V4' = '{}', \
		'V5' = '{}', 'V6' = '{}', 'V7' = '{}', 'V8' = '{}'".format(
		c_V0, c_V1, c_V2, c_V3, c_V3, c_V4, c_V4, c_V5, c_V5, c_V6, c_V6, c_V7, c_V7, c_V8, c_V8, 
		c_V0, c_V1, c_V2, c_V3, c_V4, c_V5, c_V6, c_V7, c_V8))
	g.db.commit()
	return redirect(url_for('admin'))


@app.route('/add_setter', methods=['POST'])
def add_setter():
	require_logged_in()
	require_admin()
	setter_name = request.form['name']
	g.db.execute("insert into setters values (NULL, ?)",[setter_name])
	g.db.commit()
	return redirect(url_for('admin'))

@app.route('/delete_setter/<id>')
def delete_setter(id):
	require_logged_in()
	require_admin()
	g.db.execute("delete from setters where id = ?",[id])
	g.db.commit()
	return redirect(url_for('admin'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    password = None
    if request.method == 'POST':
    	username = request.form['username']
    	password = hashlib.md5(request.form['password']).hexdigest()
        checker = g.db.execute("select * from users where username = ? and password = ?", [username,password])
        checker = checker.fetchone()
        if checker is None:
        	error = "Invalid username or password. Try again."
        	return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            session['logged_in_as'] = username
            session['is_admin'] = checker['is_admin']
            return redirect(url_for('home'))
    else:
    	return render_template('login.html')
        	
    
@app.route('/register', methods=['GET', 'POST'])
def register():
	error = None
	which_error = None
	password = None
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		comfirm_password = request.form['confirm_password']
		if password != comfirm_password:
			error = "Paswords do not match, please try again."
			which_error = "p"
			return render_template('register.html',error=error, which_error=which_error)
		checker = g.db.execute("select * from users where username = ?", [username])
		checker = checker.fetchone()

		if checker is not None:
			error = "This username already exists. Please select another."
			which_error = "u"
			return render_template('register.html',error=error, which_error=which_error)
		elif len(password) < 6:
			error = "Please use a longer password. Minimum length is 6 characters."
			which_error = "p"
			return render_template('register.html',error=error, which_error=which_error,username=username)
		else:
			password = hashlib.md5(request.form['password']).hexdigest()
			g.db.execute("insert into users values (NULL, ?, ?, 0, '','')", [username,password])
			g.db.commit()
			session['logged_in'] = True
			session['logged_in_as'] = username
			session['is_admin'] = 0
			return redirect(url_for('home'))
	return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('is_admin', None)
    return redirect(url_for('home'))

@app.errorhandler(401)
def custom_401(error):
	message = "You are attempting to access a restricted area."
	return render_template('error.html',error=error,message=message,code=401), 401
@app.errorhandler(404)
def custom_404(error):
	message = "WHatever you were looking for does not exist."
	return render_template('error.html',error=error, message=message,code=404), 404
@app.errorhandler(405)
def custom_405(error):
	message = "There's really no reason for you to see this page."
	return render_template('error.html',error=error, message=message,code=405), 405

def require_logged_in():
	if not 'logged_in' in session:
		abort(401)

def require_admin():
	if session.get('is_admin') == 0:
		abort(401)


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

@app.route('/test')
def chart_data():
	username = session['logged_in_as']
	total_amounts = dict(g.db.execute("select r.rating, count(*) from routes as r join orderkeys as k on k.rating = r.rating group by r.rating order by k.key;").fetchall())
	return str(total_amounts)


if __name__ == '__main__':
		app.run()
