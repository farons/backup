# coding=utf-8


@app.route('/api/users', methods = ['POST'])
def reg_user():
    """
    
    """
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password id None:
        abort(400)  # 输入不合法 
    if User.query.filter_by(username = username).first() is not None:
        about(400)  # 用户已存在

    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
