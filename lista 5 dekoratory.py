#zad1
def hello(fn):
    def internal():
        print("hello")
        return fn()

    return internal


@hello
def moja_funkcja():
    print("moja funkcja")


def main():
    moja_funkcja()
    moja_funkcja()


if __name__ == '__main__':
    main()

#zad2

def tetranacci(n):
    tetra = [0, 0, 0, 1, ]

    if n in (1, 2, 3, 4):
        return tetra[n - 1]
    else:
        return tetranacci(n - 1) + tetranacci(n - 2) + tetranacci(n - 3) + tetranacci(n - 4)


def main():
    x = tetranacci(12)
    print(x)


if __name__ == '__main__':
    main()

#zad3
def cache(fn):
    tetra_cache = {}

    def check_cache(*args, **kwargs):
        n = fn(*args, **kwargs)
        if args[0] in tetra_cache:
            return tetra_cache[args[0]]
        else:
            tetra_cache[args[0]] = fn(args[0])
        return n

    return check_cache


@cache
def tetranacci(n):
    tetra = [0, 0, 0, 1]
    if n in (1, 2, 3, 4):
        return tetra[n - 1]
    else:
        return tetranacci(n - 1) + tetranacci(n - 2) + tetranacci(n - 3) + tetranacci(n - 4)


if __name__ == "__main__":
    x = tetranacci(20)
    print(x)

#zad 4

# lista użytkowników i ich haseł
users = {"jan": "jan123", "tomasz": "tom234", "agata": "aga123", "anonymous": "anonymous"}


# wyjątek rzucany podczas błędnoego logowania
class NotLoggedIn(Exception):
    pass


# dekorator sprawdzający czy użytkownik jest zalogowany poprawnie
def login_required(fn):
    def login_validate(*args, **kwargs):
        # weryfikacja czy nazwa użytkownika istnieje w bazie
        if args[0] in users:
            # weryfikacja czy podane hasło jest prawidłowe
            if users.get(args[0]) == args[1]:
                # jeżeli login i hasło są prawidłowe wywołujemy funkcję
                return fn(*args, **kwargs)
            else:
                # rzucienie wyjątkiem
                raise NotLoggedIn("Username or password is not correct")
        else:
            raise NotLoggedIn("Username or password is not correct")

    return login_validate


@login_required
def login(user, passw):
    print("Zalogowano do konta")


@login_required
def anonymous(user, passw):
    print("Użytkownik anonimowy zalogowany")


def main():
    type_of_login = int(input("""Wybierz 1 jeżeli chcesz sie zalogować do swojego konta.
Wybierz 0 jeżeli chcesz być anonimowy:"""))

    if type_of_login == 1:
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj Hasło: ")
        login(username, password)
    else:
        anonymous("anonymous", "anonymous")


if __name__ == "__main__":
    main()


