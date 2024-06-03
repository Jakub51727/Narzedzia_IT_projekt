import argparse
from konwerter import nIT_json, nIT_yaml, nIT_xml


def parsowanie_arg():
    pars = argparse.ArgumentParser(description='Konwersja danych miedzy formatami .xml; .json; .yaml')
    pars.add_argument('plik_wejsciowy', type=str, help='sciezka pliku wejsciowego')
    pars.add_argument('plik_wyjsciowy', type=str, help='sciezka pliku wyjsciowego')
    arg = pars.parse_args()
    return arg


def main():
    arg = parsowanie_arg()
    plik_wejsciowy = arg.plik_wejsciowy
    plik_wyjsciowy = arg.plik_wyjsciowy

    if plik_wejsciowy.endswith('.json') and plik_wyjsciowy.endswith('.json'):
        dane = nIT_json.jsonek(plik_wejsciowy)
        nIT_json.save_jsonek(dane, plik_wyjsciowy)
        print(f"dokonano konwersji {plik_wejsciowy} do {plik_wyjsciowy}")
    elif plik_wejsciowy.endswith('.yml') and plik_wyjsciowy.endwith('.yml'):
        dane = nIT_yaml.yamlek(plik_wejsciowy)
        nIT_yaml.save_yamlek(dane, plik_wyjsciowy)
        print(f"dokonano konwersji {plik_wejsciowy} do {plik_wyjsciowy}")
    elif plik_wejsciowy.endswith('.yml') and plik_wyjsciowy.endwith('.json'):
        dane = nIT_yaml.yamlek(plik_wejsciowy)
        nIT_json.save_jsonek(dane, plik_wyjsciowy)
        print(f"dokonano konwersji {plik_wejsciowy} do {plik_wyjsciowy}")
    elif plik_wejsciowy.endswith('.json') and plik_wyjsciowy.endwith('.yml'):
        dane = nIT_json.jsonek(plik_wejsciowy)
        nIT_yaml.save_yamlek(dane, plik_wyjsciowy)
        print(f"dokonano konwersji {plik_wejsciowy} do {plik_wyjsciowy}")
    elif plik_wejsciowy.endswith('.xml'):
        dane = nIT_xml.xmlek(plik_wejsciowy)
        print(dane)
    else:
        print(f"Niewlasciwy format pliku: {plik_wejsciowy}")


if __name__ == "__main__":
    main()
