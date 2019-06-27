import db

JSON = 0
PRICE = 1


def get_item_information():
    pass


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
        store_name = store_data_list[i][JSON]['name']
        distance = norm_distances[i]
        price = norm_prices[i]
        ranks[store_name] = calculate_rank(distance, price)

    return ranks


def calculate_rank(distance, price):
    """
    Calculates rank based on the formula:
    0.7*price + 0.3*distance

    :param price: price of item at specific store
    :param distance: distance to specific store
    :return: ranking based on distance and store
    """
    return 0.7*price + 0.3*distance


def normalize(data):
    max_ = max(data)
    normalized = [data[i] / max_ for i in range(len(data))]
    return normalized





