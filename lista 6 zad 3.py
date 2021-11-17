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
