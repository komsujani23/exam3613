from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit')
def submit():
    uname= request.form['f1']['uname'].text
    return render_template('greetings.html',name=uname)

if __name__=="__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)