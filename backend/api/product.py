import json

class ProductApi:
    def __init__(self,req,services):
        self.req=req
        self.services=services
        
    def read(self):
        length = int(self.req.headers.get("Content-Length", 0))
        body = self.req.rfile.read(length)
        return json.loads(body) if body else {}
    
    def respond(self,data):
        self.req.send_response(200)
        self.req.send_header("Content-Type", "application/json")
        self.req.end_headers()
        self.req.wfile.write(json.dumps(data).encode())
    
    def get(self,product_id):
        self.respond(self.service.get_product(product_id))
    
    def post(self):
        data=self.read()
        self.respond(self.services.create_product(**data))
        
        
    def patch(self,product_id):
        data=self.read()
        self.respond(self.services.patch_product(product_id,data))
        
    def delete(self,product_id):
        self.respond(self.services.deleted_product(product_id))
        
    
        