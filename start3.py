from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost/py_sweater'
db = SQLAlchemy(app)

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)
    return app.config


@app.route('/otzivi', methods=['GET'])
def main1():
    return render_template('main1.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))
    return redirect(url_for('main1'))
    return app.config.clear()


if __name__ == '__main__':
    app.run()