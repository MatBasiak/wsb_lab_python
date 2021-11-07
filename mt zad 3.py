import threading
import uuid, hashlib

uuids = []
md5s = []
threads = []


def generate():
    for i in range(0, 200):
        uid = uuid.uuid4().hex
        uuids.append(uid)


def chesksum(uid):
    md5checksum = hashlib.md5(uid.encode()).hexdigest()
    md5s.append(md5checksum)


def main():
    generate()

    for i in range(0, len(uuids)):
        thread = threading.Thread(target=chesksum, args=(uuids[i],))
        threads.append(thread)

    # uruchomienie wszystkich wątków
    for thread in threads:
        thread.start()

    # zamknięcie wątków
    for thread in threads:
        thread.join()

    for uuid, md5 in zip(uuids, md5s):
        print(f"{uuid} - {md5}")


if __name__ == "__main__":
    main()
