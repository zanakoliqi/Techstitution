from flask import Blueprint,render_template

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
	return render_template("index.html")

@mod_main.route('/form')
def form():
	name="Techstitution"
	return render_template("form.html",name=name)
