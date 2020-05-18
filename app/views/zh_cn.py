from flask import Blueprint
from flask import render_template
from flask import request

zh_cn = Blueprint('zh_cn', __name__)

@zh_cn.route('/')
def index():
    content = {
        'host_url': request.host_url
    }
    return render_template('zh_cn/home.html', **content)

@zh_cn.route('/product/')
def product():
    return render_template('zh_cn/product.html')