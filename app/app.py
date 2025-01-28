import flask


app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/test')
def test():
    return "Test route"
