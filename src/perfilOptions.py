from flask import Blueprint,request,redirect,url_for
from flask_login import current_user
from database import conexion

options=Blueprint('options',__name__,url_prefix='/options')

@options.route('/agregar',methods=['POST'])
def agregar():
    fullname=request.form['fullname']
    phone=request.form['phone']
    email=request.form['email']
    

    cursor=conexion.cursor()
    sql='INSERT INTO contacts (fullname, phone, email,id_user) values (%s,%s,%s,%s)'
    
    values=(fullname,phone,email,current_user.id)
    cursor.execute(sql,values)
    
    conexion.commit()

    return redirect(url_for('perfil'))





