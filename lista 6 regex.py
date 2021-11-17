#zad 1

import re


def main():
    text = input("Podaj napis: ")

    rex = re.search(r'^\d*\d$', text)
    if rex:
        print("To jest liczba.")
    else:
        print("To nie jest liczba.")


if __name__ == '__main__':
    main()

#zad 2

import re


def main():
    text = input("Podaj napis: ")

    rex = re.findall(r'[0-9]+', text)

    length = len(rex)
    numbers = str(rex)[1:-1]

    if length > 0:
        print(f"Znalezione liczby: {numbers}")
    else:
        print("Nie znaleziono liczb")


if __name__ == '__main__':
    main()

# zad 3

import re


def main():
    running = True
    while running:
        text = input("Podaj napis: ")
        if text.lower() != "koniec":
            rex_compile = re.compile("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")
            rex = re.search(rex_compile, text)
            if rex:
                print("Zapis poprawny")
            else:
                print("Zapis niepoprawny!!!")
        else:
            running = False


if __name__ == '__main__':
    main()

# zad 4

import re


def main():
    running = True
    while running:

        text = input("Podaj kod: ")
        if text.lower() != "koniec":

            rex_compile = re.compile("[0-9]{2}-[0-9]{3}")
            rex = re.search(rex_compile, text)
            if rex:
                print("Kod jest poprawny")
            else:
                print("Kod jest niepoprawny!!!")
        else:
            running = False


if __name__ == '__main__':
    main()

#zad5
import re


def main():
    running = True
    while running:

        text = input("Podaj adres: ")
        if text.lower() != "koniec":

            rex_compile = re.compile(r"[a-zA-Z0-9_+-.]+@[a-zA-Z0-9_+-.]+\.[a-zA-Z0-9]")
            rex = re.search(rex_compile, text)
            if rex:
                print("Adres jest poprawny")
            else:
                print("Adres jest niepoprawny!!!")
        else:
            running = False


if __name__ == '__main__':
    main()
