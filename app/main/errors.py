#
# errors.py
# @author yanzhilong
# @description 这里是系统出现异常是给用户的返回页面 
# @created Sat Nov 24 2018 10:56:00 GMT+0800 (中国标准时间)
# @last-modified Sat Nov 24 2018 12:40:08 GMT+0800 (中国标准时间)
#

from flask import render_template
from flask import Blueprint

errors = Blueprint('errors', __name__)
errors_url = '/errors'


@errors.route('/show', methods=['GET'])
def show():
    return render_template('show.html')