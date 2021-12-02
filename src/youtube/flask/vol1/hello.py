from flask import Flask

app = Flask(__name__)

# @app.route("/japan")
# def japan():
#     return "<p>Hello, Japan!</p>" 

# @app.route("/america")
# def america():
#     return "<p>Hello, America!</p>" 

# @app.route("/world")
# def hello_world():
#     return "<p>Hello, World!</p>" 

# #可変式のルーティング
# @app.route("/japan/<city>")
# def japan(city):
#     return f'Hello, {city} in Japan'

#htmlを変数として定義してreturnに書く
# html = '''
# <h1>sample HTML</h1>
# <ul>
#     <li>list1</li>
#     <li>list2</li>
#     <li>list3</li>
# </ul>
# '''

# @app.route("/")
# def hello():
#     return html

#HTMLを中にもかける
# @app.route("/")
# def hello():
#     return '<h1>Hello world!</h1>'
 
from flask import render_template

bullets = [
    '箇条書き1',
    '箇条書き2',
    '箇条書き3',
    '箇条書き4',
    '箇条書き5',
    '箇条書き6'
]


@app.route("/")
def hello():
    return render_template('hello.html', bullets=bullets)

