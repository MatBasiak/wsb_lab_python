# zad1

import multiprocessing
print(multiprocessing.cpu_count())

# zad 2
import os, multiprocessing


# 2.1
pid = os.getpid()
print(pid)
# 2.2

def print_pid():
    print(os.getpid())
    return


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_pid)
    p2 = multiprocessing.Process(target=print_pid)
    p1.start()
    p2.start()

# zad3
# 3.1
import multiprocessing

elements = [1, 2, "lolo", "john", "exit"]


def print_element(element, q):
    if element != "exit":
        q.put(element)
    else:
        return


if __name__ == "__main__":

    queue = multiprocessing.Queue()

    for i in range(0, len(elements)):
        multiprocessing.Process(target=print_element, args=(elements[i], queue)).start()

    for i in range(0, len(elements)):
        message = queue.get()
        print(message)

3.2

import multiprocessing

elements = []


def print_element(q):
    message = q.get()
    print(message)


def read_element(q):
    user_input = input("PODAJ NAPIS: ")
    q.put(user_input)


def main():
    queue = multiprocessing.Queue()
    counter = 0
    flag = True

    while flag:
        multiprocessing.Process(target=read_element, args=(queue,)).start()
        multiprocessing.Process(target=print_element, args=(queue,)).start()
        counter += 1
        if counter > 10:
            flag = False


if __name__ == "__main__":
    main()



# zad 4
import concurrent.futures


def read_numbers():
    numbers = []
    for i in range(3):
        number = int(input("Podaj liczbę: "))
        numbers.append(number)
    return numbers


def power(n):
    return n * n


def main():
    results = []
    numbers = read_numbers()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(0, len(numbers)):
            res = executor.submit(power, numbers[i]).result()
            results.append(res)

    for res in results:
        print(res, end=" ")


if __name__ == "__main__":
    main()



# # zad 5
import uuid, hashlib
import concurrent.futures

uuids = []
md5s = []


def generate():
    for i in range(0, 200):
        uid = uuid.uuid4().hex
        uuids.append(uid)


def checksum(uid):
    md5checksum = hashlib.md5(uid.encode()).hexdigest()
    return md5checksum


def main():
    generate()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(0, len(uuids)):
            res = executor.submit(checksum, uuids[i]).result()
            md5s.append(res)

    for uuid, md5 in zip(uuids, md5s):
        print(f"{uuid} - {md5}")


if __name__ == "__main__":
    main()

