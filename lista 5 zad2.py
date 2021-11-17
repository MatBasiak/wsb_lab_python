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
