import psycopg2

class Database:
    def __init__(self,db_name="store.db"):
        self.db_name=db_name
        self.init_db()
    
    def connect(self):
        return psycopg2.connect(
            host="localhost",
            port=5432,
            database="shop_db",
            user="postgres",
            password="Kanye@12"
        )
    
    def init_db(self):
        conn=self.connect()
        cursor=conn.cursor()
        cursor.execute(
            'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'
        )
        cursor.execute(
            """
            CREATE TABLE user(
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                email VARCHAR(50) UNIQUE NOT NULL,
                PASSWORD VARCHAR(50) NOT NULL,
            )
            """
            
        )
        cursor.execute(
            """
            CREATE TABLE product(
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                user_id UUID ,
                product_name VARCHAR(50) UNIQUE NOT NULL,
                per_product_price DECIMAL ,
                total_product DECIMAL,
                total_price DECIMAL,
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
            """
        )
        conn.commit()
        conn.close()
        
        