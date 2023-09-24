from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
	return render_template('index.html', curr_time=datetime.utcnow())

# activity 3
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name, curr_time=datetime.utcnow())