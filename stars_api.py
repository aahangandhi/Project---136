from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/star/<string:star_name>")
def get_star(star_name):
    star = [star for star in data if star['Star Name'] == star_name]
    if star:
        return jsonify({
            "star": star[0],
            "message": "success"
        }), 200
    else:
        return jsonify({
            "message": "Star not found"
        }), 404

if __name__ == '__main__':
    app.run()
