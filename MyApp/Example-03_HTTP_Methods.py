from flask import Flask, request

app = Flask(__name__)

def do_the_login():
    return '<p>Do the login in WebSite, please<p>'


def show_the_login_form():
    return '<p>Please, create a login in the WebSite<p>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '<p>Method: Post<p>'
    else:
        return '<p>Method: Get<p>'


@app.get('/login')
def login_get():
    return show_the_login_form()


@app.post('/login')
def login_post():
    return do_the_login()