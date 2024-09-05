from functools import wraps
from flask import request
from api.utils.response import response
from werkzeug.exceptions import Unauthorized
from config.env import API_KEY

def auth_route(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
       
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        
        if not token:
            return response(
                data=[],
                message="Not authorized",
                statusCode=401,
                success=False,
            )
        
        try:
            if token != API_KEY:
                raise Unauthorized('Invalid token')
        
        except Unauthorized:
            return response(
                data=[],
                message="Not authorized",
                statusCode=401,
                success=False,
            )
        
        return func(*args, **kwargs)
    
    return decorated