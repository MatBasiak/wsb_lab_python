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
