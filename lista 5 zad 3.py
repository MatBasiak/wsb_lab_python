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
