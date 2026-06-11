import hashlib
from database import Database

class AuthServices:
    def __init__(self):
        self.db=Database()
    
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create(self,email,password):
        conn=self.db.connect()
        cursor=conn.cursor()
        hashed=self.hash_password(password)
        cursor.execute(
            """"
            INSERT INTO user(email,password) values(?,?)
            """,(email,hashed)
        )
        conn.commit()
        conn.close()
        
        return {
            "message":"user register successfully",
            "user":{
                "email":email,
            }
        }
    def login(self,email,password):
        conn=self.db.connect()
        cursor=conn.cursor()
        hashed=self.hash_password(password)
        cursor.execute(
            """
            SELECT (user_id,email,password) FROM user where 
            email = ? AND password =?
            """,(email,password))
        user=cursor.fetchone()
        conn.close()
        if user:
            return {
                "success":True,
                "user_id":user[0],
                "email":user[1],
            }
            
        return {"success": False, "message": "Invalid login"}