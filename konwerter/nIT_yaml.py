import yaml

def yamlek(yaml_file):
    with open(yaml_file, 'r') as g:
        dane = yaml.safe_load(g)
    return dane