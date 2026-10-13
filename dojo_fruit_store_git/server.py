from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html", first_name=request.form['first_name'], 
                           last_name=request.form['last_name'],
                           student_id=request.form['student_id'],
                           apple=request.form['apple'],
                           strawberry=request.form['strawberry'],
                           raspberry=request.form['raspberry'],
                           charger=request.form['first_name'],
                           count=int(request.form['apple'])+int(request.form['strawberry'])+int(request.form['raspberry'])
                           )
                           
                           
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    