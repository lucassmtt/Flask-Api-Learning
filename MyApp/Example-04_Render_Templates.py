from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('Example_04_part2.html', name=name)


@app.route('/helloworld/')
@app.route('/helloworld/<name>')
def helloWorld(name=None):
    return render_template('Example_04_hello.html', name=name)
