import argparse


def parsowanie_arg():
    pars = argparse.ArgumentParser(description='Konwersja danych miedzy formatami .xml; .json; .yaml')
    pars.add_argument('plik_wejsciowy', type=str, help='sciezka pliku wejsciowego')
    pars.add_argument('plik_wyjsciowy', type=str, help='sciezka pliku wyjsciowego')
    arg = pars.parse_args()
    return arg


if __name__ == "__main__":
    arg = parsowanie_arg()
    print(f'plik wejsciowy: {arg.plik_wejsciowy}')
    print(f'plik wyjsciowy: {arg.plik_wyjsciowy}')
