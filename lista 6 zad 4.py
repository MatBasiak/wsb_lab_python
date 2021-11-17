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
