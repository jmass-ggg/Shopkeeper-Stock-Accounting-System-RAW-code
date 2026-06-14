from http.server import BaseHTTPRequestHandler,HTTPServer

from services.product import Product
from services.auth   import AuthServices

from api.product import ProductApi
from api.auth import AuthApi

product_services=Product()
auth_services=AuthServices()
