from flask import Flask, request, render_template
from Calculator import syntaxOkay, calc
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Client.html', answer_text='')

@app.route('/',methods=['POST'])
def result():
    string = request.form['exp']
    synOkay, msg = syntaxOkay(string)
    if synOkay:
        answer = calc(string)
    else:
        answer = msg
    return render_template('Client.html', answer_text=answer)