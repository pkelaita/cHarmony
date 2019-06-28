from bscanner import bscan_fs
import json

JSON = 0
PRICE = 1


def get_item_information(img_fs, price):
    item = bscan_fs(img_fs)

    # TODO configure SQL DB
    with open('data/stores.json') as f:
        stores = json.load(f)
    with open('data/items.json') as f:
        items = json.load(f)

    # Find the matching item
    match = None
    for it in items:
        if it['product_name'] == item['product_name'] and it['brands'] == item['brands']:
            match = it
    if not match:
        return {'error': 'product not found in any stores'}

    # Map name to stores
    store_map = {}
    for it in stores:
        store_map[it['store_name']] = it

    # Filter stores
    tuple_list = []
    for store_name in match['stores']:
        tup = (
            store_map[store_name],
            match['wsp'] * store_map[store_name]['markup']
        )
        tuple_list.append(tup)

    ranked = rank(tuple_list)
    result = {}
    for key in ranked:
        if float(ranked[key][PRICE]) < float(price):
            result[key] = ranked[key]
    return result


def rank(store_data_list):
    """
    Populates a returns list with associated "scores" for each store
    in the input list

    :param: store_data_list associated with a specific item received from get_item_information()
    :raises: ValueError if there are no stores in the store_data_list
    :return: list of rankings associated with each store in store_data_list
    """

    if len(store_data_list) < 1:
        raise ValueError

    ranks = {}

    distances = [pair[JSON]['distance'] for pair in store_data_list]
    prices = [pair[PRICE] for pair in store_data_list]
    norm_distances = normalize(distances)
    norm_prices = normalize(prices)
    assert len(norm_distances) == len(distances)

    for i in range(len(store_data_list)):
        store_name = store_data_list[i][JSON]['store_name']
        distance = norm_distances[i]
        price = norm_prices[i]
        ranks[store_name] = (calculate_rank(distance, price), store_data_list[i][PRICE], distances[i])

    return ranks


def calculate_rank(distance, price):
    """
    Calculates rank based on the formula:
    0.7*price + 0.3*distance

    :param price: price of item at specific store
    :param distance: distance to specific store
    :return: ranking based on distance and store
    """
    return 0.7 * price + 0.3 * distance


def normalize(data):
    max_ = max(data)
    normalized = [data[i] / max_ for i in range(len(data))]
    return normalized
