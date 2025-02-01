from flask import Flask,render_template,flash,url_for,redirect,request
from flask_login import LoginManager, login_user,logout_user, login_required,current_user
import mysql.connector
import os
from dotenv import load_dotenv
from models.ModelUser import ModelUser
from models.entities.User import User
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

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
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        user=User(0,'',email,password)

        logged_user=ModelUser.login(conexion,user)
        if logged_user:
            if logged_user.password:
                return redirect(url_for('perfil'))
            else:
                return 'Contraseña incorrecta'
        else:
            return 'Email incorrecto'




@app.route('/perfil',methods=['GET'])
def perfil():
    return render_template('perfil.html')




if __name__=='__main__':
    app.run(debug=True)