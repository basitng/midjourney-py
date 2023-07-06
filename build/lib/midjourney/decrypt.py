import json


def jsonDecrpter(data) -> json:
    json_data = data
    parse_data = json.loads(json_data)

    return parse_data
