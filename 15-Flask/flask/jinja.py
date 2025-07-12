from flask import Flask, render_template,  request, redirect, url_for

app = Flask(__name__)

#@app.route("/")
#def welcome():
#   return "<html> <h1> Welcome to the flask course </h1> </html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

'''@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')
'''
    
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template("result.html", results = res)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp = {'score': score, 'res': res}
    return render_template("result1.html", results = exp)

@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html', results = score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html', results = score)

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['data science'])

        total_score = (science + maths + c + data_science)
    return redirect(url_for('successres', score = total_score))

@app.route('/')
def home():
    return render_template('getresult.html')


if __name__ == "__main__":
    app.run(debug=True)