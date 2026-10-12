from flask import Flask, render_template, session, redirect, request
import random

from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "gold"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template("index.html", gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        amount = random.randint(10, 20)
    elif building == 'cave':
        amount = random.randint(5, 10)
    elif building == 'house':
        amount = random.randint(2, 5)
    elif building == 'casino':
        amount = random.randint(-50, 50)
    session['gold'] += amount
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)