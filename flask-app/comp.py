from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("web.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    num1 = request.form['num1']
    num2 = request.form['num2']

    if num1 > num2 :
        return  '%s is greater!' % num1
    elif num1 == num2:
        return  'Both values are same!'
    else :
        return  '%s is greater!' % num2

if __name__ == '__main__':
     app.run(host="0.0.0.0",port=8080,debug=True)
