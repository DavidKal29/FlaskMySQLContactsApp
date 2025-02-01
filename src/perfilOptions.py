from flask import Blueprint,request,redirect,url_for,render_template
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

@options.route('/edit/<id>',methods=['GET','POST'])
def editar(id):
    if request.method=='GET':
        cursor=conexion.cursor()
        sql='SELECT * FROM contacts WHERE id=%s'
        cursor.execute(sql,(id,))
        datos=cursor.fetchall()

        return render_template('editar.html',datos=datos)
    
    elif request.method=='POST':
        cursor=conexion.cursor()

        fullname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']

        sql='UPDATE contacts SET fullname=%s,phone=%s,email=%s WHERE id=%s'
        values=(fullname,phone,email,id)

        cursor.execute(sql,values)

        conexion.commit()

        return redirect(url_for('perfil'))
    

@options.route('/delete/<id>')
def eliminar(id):
    cursor=conexion.cursor()
    sql='DELETE FROM contacts WHERE id=%s'
    cursor.execute(sql,(id,))
    conexion.commit()

    return redirect(url_for('perfil'))





        








