from flask import Flask,render_template,flash,url_for,redirect
from flask_login import LoginManager, login_user,logout_user, login_required,current_user
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


app=Flask(__name__)
conexion=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    db=os.getenv('DATABASE')
)

print(conexion)

@app.route('/')#ruta que enviará directamente al login
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/perfil',methods=['GET'])
def perfil():
    return render_template('perfil.html')




if __name__=='__main__':
    app.run(debug=True)