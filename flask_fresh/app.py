from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world!"


@app.route('/champion')
def champion():
    return "Champion!"

@app.route('/users/<name>')
def profile(name):
    return f"Hi {name}"

@app.route('/repeat/<count>/<word>')
def repeat(count, word):
    return (word + " ") * int(count)

if __name__ == "__main__":
    app.run(debug=True)