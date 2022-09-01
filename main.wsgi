import os
import sys
from flask import Flask, redirect, url_for, request


sys.path.append('/home/c/ci79723/venv/lib/python3.6/site-packages/')
app = Flask(__name__)
application = app


@app.route('/', methods=['GET'])
def get_message():
    args = request.args
    if not args:
        return redirect(url_for('get_message', name='Rekruto', message='Давай дружить!'))
    name = args.get('name')
    message = args.get('message')
    if not (name and message) or len(args) > 2 or '/' in message:
        return redirect(url_for('wrongURL'))
    return f"Hello {name}! {message}!"


@app.route('/wrongURL')
def wrongURL():
    return 'Received wrong URL'


if __name__ == '__main__':
    app.run(debug=True)
