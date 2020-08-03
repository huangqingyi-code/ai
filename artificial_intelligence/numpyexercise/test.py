from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎来到首页，这个世界真美好~~~'


@app.route('/score')
def score():
    return '期末考试成绩: 语文98，数学100，英语99。'


if __name__ == '__main__':
    app.run(host="192.168.2.31", port=8888)