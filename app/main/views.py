#
# views.py
# @author yanzhilong
# @description 这里系统的基础模块,组成系统的大体框架
# @created Sat Nov 24 2018 10:55:32 GMT+0800 (中国标准时间)
# @last-modified Sat Nov 24 2018 12:43:17 GMT+0800 (中国标准时间)
#

from datetime import datetime

from flask import Blueprint
from flask import render_template


main = Blueprint('/main', __name__)
main_url = '/main'

@main.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
