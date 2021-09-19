import flask

app = flask.Flask('My Test Project')

#first method
@app.route('/')
def hello():
    return 'Welcome to this amazing App'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)