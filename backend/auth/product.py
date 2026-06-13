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
    def patch_product(self,product_id,**kwargs):
        conn=self.db.connect()
        cursor=conn.cursor()
        fields=[]
        value=[]
        allowed_fields=["product_name","per_product_price","total_product"]
        
        for key in allowed_fields:
            if key in kwargs and kwargs[key] is not None:
                fields.append(f"{key}=%s")
                value.append(kwargs[key])
                
        if "per_product_price" in kwargs or  "total_product" in kwargs:
            price=kwargs.get('per_product_price')
            qty=kwargs.get('total_product')
            cursor.execute(
                """
                SELECT (per_product_price,total_product)
                FROM product WHERE id = %s
                """,(product_id)
                
            )
            old_price,old_qty=cursor.fetchone()
            price =price if price is None else old_price
            qty=qty if price is None else old_qty
            
            fields.append("total_price = %s")
            value.append(price*qty)
        value.append(product_id)
        query=f"""
            UPDATE product 
            SET{", ".join(fields)}
            WHERE id = %s
            RETURNING id
        """
        
        cursor.execute(query,value)
        updated_id=cursor.fetchone()[0]
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            "id":updated_id,
            
        }
            
            
        
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