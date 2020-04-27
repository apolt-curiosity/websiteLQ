from flask import Blueprint,render_template

en = Blueprint('en', __name__,url_prefix='/en')

@en.route('/')
def index():
    return render_template('en/home.html')

@en.route('/product/')
def product():
    return render_template('en/product.html')