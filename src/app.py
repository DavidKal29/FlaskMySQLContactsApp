from flask import Flask,render_template,flash,url_for,redirect
from flask_login import LoginManager, login_user,logout_user, login_required,current_user


app=Flask(__name__)


@app.route('/')#ruta que enviará directamente al login
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')




if __name__=='__main__':
    app.run(debug=True)