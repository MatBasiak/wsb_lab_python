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
