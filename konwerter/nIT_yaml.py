import yaml

def yamlek(yaml_file):
    with open(yaml_file, 'r') as g:
        dane = yaml.safe_load(g)
    return dane

def save_yamlek(dane, yaml_file):
    with open(yaml_file, 'w') as g:
        yaml.dump(dane, g, default_style=False)