import json


def jsonek(json_file):
    with open(json_file, 'r') as f:
        dane = json.load(f)
    return dane