from flask import Flask,jsonify
from flask_cors import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
#跨域支持
CORS(app, supports_credentials=True)

health_dict = {'status': 'UP'}
index_dict = {'index': '欢迎来到首页'}


@app.route('/health.json')
def health():
    return jsonify(health_dict)


@app.route('/')
def index():
    return jsonify(index_dict)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8060,
    )