from flask import make_response, jsonify, abort
from werkzeug.exceptions import HTTPException



class FPAPIException(HTTPException):
    def __init__(self, message, errors=None):
        payload = {"message": message}
        if errors:
            payload["errors"] = errors

        abort(make_response(jsonify(payload), 400))

