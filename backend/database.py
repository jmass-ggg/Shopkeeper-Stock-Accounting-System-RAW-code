import sqlite3

class Database:
    def __init__(self,db_name="store.db"):
        self.db_name=db_name
        self.init_db()
    
    def connect(self):
        return sqlite3.connect(self.db_name)
    
    def init_layer(self):
        conn=self.connect()
        cursor=conn.cursor()
        
        cursor.execute(
            """
            CREATE TABLE user(
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                email VARCHAR(50) UNIQUE NOT NULL,
                PASSWORD VARCHAR(50) UNIQUE NOT NULL,
            )
            """
            
        )
        cursor.execute(
            """
            CREATE TABLE product(
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                product_name VARCHAR(50) UNIQUE NOT NULL,
                per_product_price DECIMAL ,
                total_price DECIMAL,
            )
            """
        )
        