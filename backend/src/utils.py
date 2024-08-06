import json
from copy import deepcopy


def __show_element(element_):
    omit_keys = ['created_at', 'updated_at', 'game', 'players', 'reviews']

    element = deepcopy(element_)

    if not isinstance(element, dict):
        element = element.__dict__

    for key in omit_keys:
        if key in element:
            del element[key]

    print(json.dumps(element, indent=4))


def __show_data(data_):
    data = deepcopy(data_)

    if isinstance(data, list):
        for element in data:
            __show_element(element)

    else:
        __show_element(data)


def __show(body, expected):
    print('Response:')
    __show_data(body)
    print('\nExpected:')
    __show_data(expected)


def __skip_exception(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)

        except Exception as e:
            # print(e)
            return False

    return wrapper
