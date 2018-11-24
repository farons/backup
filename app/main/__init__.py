#
# __init__.py
# @author yanzhilong
# @description 这里配置所有要注册的模块,模块下的所有文件都是分模块的功能
# @created Tue Nov 20 2018 20:16:34 GMT+0800 (中国标准时间)
# @last-modified Sat Nov 24 2018 12:45:56 GMT+0800 (中国标准时间)
#
from flask import Blueprint

from .views import main, main_url
from .errors import errors, errors_url



view_modules = {
    main : main_url,  # 基础模块
    errors : errors_url,  # 错误异常模块

}
errors