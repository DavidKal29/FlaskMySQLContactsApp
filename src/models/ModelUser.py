from .entities.User import User
from werkzeug.security import check_password_hash,generate_password_hash

class ModelUser:
    
    @classmethod
    def login(cls,conexion,user):
        cursor=conexion.cursor()
        sql='SELECT * FROM users WHERE email=%s'
        email=(user.email,)

        cursor.execute(sql,email)
        row=cursor.fetchone()

        if row:
            id=row[0]
            username=row[1]
            email=row[2]
            password=check_password_hash(row[3],user.password)
        
            return User(id,username,email,password)
        else:
            return False
    

    @classmethod
    def registrar(cls,conexion,user):
        cursor=conexion.cursor()
        sql='INSERT INTO users (username,email,password) VALUES (%s,%s,%s)'
        
        encripted_password=generate_password_hash(user.password)
        values=(user.username,user.email,encripted_password)

        try:
            cursor.execute(sql,values)
            conexion.commit()
        except:
            return None

        
        sql='SELECT * FROM users WHERE email=%s'
        cursor.execute(sql,(user.email,))
        row=cursor.fetchone()

        if row:
            id=row[0]
            username=row[1]
            email=row[2]
            password=check_password_hash(row[3],user.password)

            return User(id,username,email,password)
        else:
            return None


    @classmethod
    def get_by_id(cls,conexion,id):
        cursor=conexion.cursor()
        sql='SELECT * FROM users WHERE id=%s'

        cursor.execute(sql,(id,))
        row=cursor.fetchone()

        if row:
            id=row[0]
            username=row[1]
            email=row[2]
            #el password da igual, pa que lo queremos
        
            return User(id,username,email,None)
        else:
            return False
