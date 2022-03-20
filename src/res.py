from flask import make_response, jsonify

def success(values):
    res = {
        "status" : 200,
        "messages" : "Success!",
        "data" : values
    }
    return make_response(jsonify(res), 200)

def badRequest(values, message):
    res = {
        "status" : 400,
        "messages" : message,
        "data" : values
    }
    return make_response(jsonify(res), 400)