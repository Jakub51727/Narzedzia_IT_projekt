import json


def jsonek(json_file):
    with open(json_file, 'r') as f:
        dane = json.load(f)
    return dane

def save_jsonek(dane, json_file):
    with open(json_file, 'w') as f:
        json.dump(dane, f, indent=4)