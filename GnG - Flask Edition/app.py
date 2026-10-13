from flask import Flask, session, render_template, request, redirect
import random
app = Flask(__name__)

app.secret_key = "it's a secret"


@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    number = session['number']
    if guess < number:
        session['result'] = 'Too low!'
    elif guess > number:
        session['result'] = 'Too high!'
    else:
        session['result'] = f'{number} was the number!'
        session['won'] = True
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
 app.run(debug=True)