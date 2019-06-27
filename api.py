from flask import Flask, make_response, request
from bscanner import bscan_fs
import json

app = Flask(__name__)


def tojson(res):
    r = make_response(json.dumps(res))
    r.mimetype = 'application/json'
    return r


@app.route('/', methods=['POST'])
def scan():
    img_fs = request.files['image']
    return tojson(bscan_fs(img_fs))


if __name__ == '__main__':
    app.run()
