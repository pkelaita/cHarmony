import requests as web
import json

endpoint = "http://127.0.0.1:5000"

images = ["chocolate.jpg", "cookies.jpg", "salmon.jpg", "sauce.jpg", "sugar.jpg"]

jsons = []

for image in images:

    image_path = 'images/{0}'.format(image)

    files = {
        'image': (image_path, open(image_path, 'rb')),
    }

    response = web.post(endpoint, files=files)
    data = response.json()
    jsons.append(data)

with open('items.json', 'w') as f:
    json.dump(jsons, f, indent=4)

print('done')







