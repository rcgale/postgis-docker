from flask import jsonify


def ok(data = ''):
    return data, 200


def bad_request(message=""):
    return jsonify({"error": "bad request", "message": message}), 400


def forbidden(message=""):
    return jsonify({"error": "forbidden", "message": message}), 403


def not_found(message=""):
    return jsonify({"error": "not found", "message": message}), 404


def server_error(message=""):
    return jsonify({"error": "server error", "message": message}), 500
