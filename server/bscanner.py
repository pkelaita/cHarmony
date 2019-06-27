from pyzbar import pyzbar
import numpy
import urllib
import cv2
import json


def bscan_fs(fs, resize_factor=1.0, show_output=False):
    npimg = numpy.fromstring(fs.read(), numpy.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    return bscan(image, resize_factor, show_output)


def bscan_file(image_file, resize_factor=1.0, show_output=False):
    image = cv2.imread(image_file)
    return bscan(image, resize_factor, show_output)


def bscan(image, resize_factor=1.0, show_output=False):
    decoded = pyzbar.decode(image)
    if not decoded:
        print('Error: could not read barcode')
        return {'error': 'could not read barcode'}
    elif len(decoded) > 1:
        print('Error: Multiple barcodes in image')
        return {'error': 'Multiple barcodes in image'}

    # Parse
    upc = decoded[0].data.decode('utf-8')
    print('Found {} barcode: {}'.format(decoded[0].type, upc))

    # Annotate and display
    if show_output:
        (x, y, w, h) = decoded[0].rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        text = '{} ({})'.format(upc, decoded[0].type)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # show the output image
        resize_factor = float(resize_factor) if resize_factor else 1.0
        cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow('img', 20, 20)
        cv2.imshow('img', cv2.resize(image, (int(image.shape[1] * resize_factor), int(image.shape[0] * resize_factor))))
        cv2.waitKey(0)

    # Get product info
    url = 'https://world.openfoodfacts.org/api/v0/product/{}.json'.format(upc)
    data = json.load(urllib.urlopen(url))

    if not data['status']:
        return {'error': 'Product with UPC {} not found'.format(upc)}

    try:
        product_name = data['product']['product_name']
        brands = data['product']['brands']
    except KeyError:
        return {'error': 'Could not retrieve product info for UPC {}'.format(upc)}

    result = {
        'product_name': product_name,
        'brands': brands,
    }
    print(result)
    return result
