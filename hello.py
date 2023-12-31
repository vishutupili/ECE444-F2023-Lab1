from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError
from flask import Flask, render_template, redirect, flash, session, url_for
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
bootstrap = Bootstrap(app)
moment = Moment(app)

def check_email(form, field):
    if "@" not in field.data:
        raise ValidationError(f"Please include '@' in the email address '{field.data}' is missing an '@'")
    elif "utoronto" not in field.data:
	    raise ValidationError("Please use your UofT email")

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	email = StringField('What is your UofT email address?', validators=[DataRequired(), check_email])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		prev_name = session.get('name')
		prev_email = session.get('email')
		if prev_name is not None and prev_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		session['email'] = form.email.data
		return redirect(url_for('index'))
	
	return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))