from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
 return render_template('index.html', rows=8 , cols=8)

@app.route('/<int:x>')
def rows_only(x):
 return render_template('index.html', rows=x, cols=8)

if __name__ == '__main__':
 app.run(debug=True)