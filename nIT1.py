import argparse
from konwerter import nIT_json

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

    if plik_wejsciowy.endswith('.json'):
        dane = nIT_json.jsonek(plik_wejsciowy)
        print(dane)
    else:
        print(f"Niewlasciwy format pliku: {plik_wejsciowy}")

if __name__ == "__main__":
    main()