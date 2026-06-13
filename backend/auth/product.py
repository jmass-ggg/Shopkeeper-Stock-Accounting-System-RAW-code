import hashlib
from database import Database

class Product:
    def __init__(self):
        self.db=Database()
   
    
    def create_product(self,user_id,product_name,per_product_price,total_product):
        conn=self.db.connect()
        cursor=conn.cursor()
        total_price=total_product*per_product_price
        cursor.execute(
            """
            INSERT INTO product (user_id,product_name,per_product_price,total_product,total_price)
            VALUES (%s, %s, %s, %s, %s)
            """,(user_id,product_name,per_product_price,total_product,total_price)
            
        )
        conn.commit()
        cursor.close()
        return {
            "user_id":user_id,
            "product_name":product_name,
            "per_product_price":per_product_price,
            "total_product":total_product,
            "total_price":total_price
        }
    def get_product(self,product_id):
        conn=self.db.connect()
        cursor=conn.cursor()
        cursor.execute(
            """
            SELECT * FROM product WHERE id = %s
            """,(product_id)
            
        )
        product=cursor.fetchone()
        cursor.close()
        conn.close()
        if not product:
            return {
                "error" : "product not found"
            }
            
        return   {
            "product_id":product[0],
            "user_id":product[1],
            "product_name":product[2],
            "per_product_price":product[3],
            "total_product":product[4],
            "total_price":product[5],
        }
    # def patch_product(self,product_id,**kwargs):
        
    def deleted_product(self,product_id):
        conn=self.db.connect()
        cursor=conn.cursor()
        cursor.execute(
            """
            DELETE FROM product
            WHERE id %s
            """,(product_id)
            
        )
        conn.commit()
        conn.close()
        cursor.close()
        return {
            "successfully":"product deleted"
        }