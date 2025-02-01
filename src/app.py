from flask import Flask,render_template,flash,url_for,redirect,request
from flask_login import LoginManager, login_user,logout_user, login_required,current_user
import mysql.connector
import os
from dotenv import load_dotenv
from models.ModelUser import ModelUser
from models.entities.User import User
import sys

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

load_dotenv()

app=Flask(__name__)
app.secret_key=os.getenv('SECRET_KEY')
loginManager=LoginManager(app)



conexion=mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    db=os.getenv('DATABASE')
)

print(conexion)

@loginManager.user_loader
def load_user(id):
    return ModelUser.get_by_id(conexion,id)

@app.route('/')#ruta que enviará directamente al login
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        if current_user.is_authenticated:
            return redirect(url_for('perfil'))
        else:
            return render_template('login.html')
    elif request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        user=User(0,'',email,password)

        logged_user=ModelUser.login(conexion,user)
        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('perfil'))
            else:
                return 'Contraseña incorrecta'
        else:
            return 'Email incorrecto'




@app.route('/perfil',methods=['GET'])
@login_required
def perfil():
    return render_template('perfil.html')



@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


def status_404(error):
    return render_template('error404.html')

def status_401(error):
    return redirect(url_for('login'))





if __name__=='__main__':
    app.register_error_handler(404,status_404)
    app.register_error_handler(401,status_401)
    app.run(debug=True)