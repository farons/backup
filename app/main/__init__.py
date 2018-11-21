#
# __init__.py
# @author yanzhilong
# @description 
# @created Tue Nov 20 2018 20:16:34 GMT+0800 (中国标准时间)
# @last-modified Tue Nov 20 2018 20:18:43 GMT+0800 (中国标准时间)
#
from flask import Blueprint


main = Blueprint('main', __name__)


from . import views, errors