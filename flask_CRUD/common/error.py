import json

from flask import Response

def resolve_error(error_object):
    if error_object["error"]["error"]:
        message = error_object["error"]["message"]
        response = Response(
            json.dumps({"message": message}),
            status=error_object["error"]["status"],
            mimetype="application/json"
        )
        return response
    # in the event that parsing the error fails return a parsing error
    error_message = {"message": "error in evaulating failure state"}
    response = Response(
        json.dumps(error_message), status=500, mimetype="application/json"
    )
    return response

def build_error(boolean, msg, code):
    error = dict(error=dict(error=boolean, message=str(msg), status=int(code)))
    return error