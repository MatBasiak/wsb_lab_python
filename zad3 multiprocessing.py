import multiprocessing
import time


def read_element(q):
    time.sleep(1)
    word = input("Podaj napis: ")
    q.put(word)
    print(q.get(word))


# def print_element(q):
#     if element != "exit":
#         q.put(element)
#     else:
#         return


if __name__ == "__main__":
    counter = 0
    queue = multiprocessing.Queue()
    read_processes = []
    # while counter < 3:
    p = multiprocessing.Process(target=read_element, args=[queue]).start()
        # read_processes.append(p)
        # counter += 1

    for pr in read_processes:
        pr.start()

    for pr in read_processes:
        pr.join()

    # for i in range(0, len(elements)):
    #     message = queue.get()
    #     print(message)
