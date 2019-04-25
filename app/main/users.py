# -*- coding:UTF-8 -*-
# users.py
# @author yanzhilong
# @description 系统用户管理模块,包括用户的增删改查,及注册登录注销校验
# @created 20190425
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/reg', methods = ['POST'])
def reg_user():
    """
    用户注册功能
    """
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or (password is None):
        abort(400)  # 输入不合法 
    if User.query.filter_by(username = username).first() is not None:
        about(400)  # 用户已存在

    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
