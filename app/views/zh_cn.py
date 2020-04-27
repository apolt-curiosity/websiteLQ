from flask import Blueprint,render_template

zh_cn = Blueprint('zh_cn', __name__)

@zh_cn.route('/')
def index():
    return render_template('zh_cn/home.html')

@zh_cn.route('/product/')
def product():
    return render_template('zh_cn/product.html')