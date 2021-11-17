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
