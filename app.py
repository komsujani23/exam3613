from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    name= request.form['name']
    dob = request.form['dob']
    gender = request.form.get('gender')
    return render_template('greetings.html',name=name,dob=dob,gender=gender)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)