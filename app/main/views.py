# -*- coding:UTF-8 -*-
# views.py
# @author yanzhilong
# @description 这里系统的基础模块,组成系统的大体框架
# @created 20181024

from datetime import datetime

from flask import Blueprint
from flask import render_template


main = Blueprint('/', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
