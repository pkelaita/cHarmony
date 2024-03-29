from flask import Flask, make_response, request
from flask_cors import CORS
from bscanner import bscan_fs
from ItemHandler import get_item_information
import json

app = Flask(__name__)
CORS(app)


def tojson(res):
    r = make_response(json.dumps(res))
    r.mimetype = 'application/json'
    return r


@app.route('/scan', methods=['POST'])
def scan():
    img_fs = request.files['image']
    return tojson(bscan_fs(img_fs))


@app.route('/', methods=['POST'])
def root():
    img_fs = request.files['image']
    price = request.args.get('price')
    return tojson(get_item_information(img_fs, price))


if __name__ == '__main__':
    app.run()
