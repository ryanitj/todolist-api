from flask import jsonify

def response(success, message, data, statusCode):
    return jsonify({
        "success":success,
        "message":message,
        "data":data,
    }), statusCode