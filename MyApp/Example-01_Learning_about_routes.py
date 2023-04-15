from flask import Flask
from flask import escape

app = Flask(__name__)


@app.route('/')
def hello_word():
    return '<p>Hello world<p>'


@app.route('/home')
def hello_in_home():
    return '<h1>Welcome the my WebSite with FlaskAPI<h1>'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>User: {escape(username)}<h1>'


@app.route('/post/<int:post_int>')
def show_post(post_id):
    # show the post with the given id, the id is an int
    return f'<h1>Post: {post_id}<h1>'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'<h1> Your Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return f'Info about page...'
