from flask import Flask, render_template, request, jsonify
import bcrypt

app = Flask(__name__)

# 模拟用户数据库
users = {
    "admin": {
        "password": bcrypt.hashpw("123456".encode('utf-8'), bcrypt.gensalt())
    }
}

# 首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 登录接口
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # 验证逻辑
    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]["password"]):
        return jsonify({'success': True, 'message': '登录成功'})
    else:
        return jsonify({'success': False, 'message': '用户名或密码错误'})

# 注册接口
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # 密码加密存储
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = {"password": hashed_password, "email": email}
    
    return jsonify({'success': True, 'message': '注册成功', 'data': {'username': username, 'email': email}})

if __name__ == '__main__':
    app.run(debug=True)