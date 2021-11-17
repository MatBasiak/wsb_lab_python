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
