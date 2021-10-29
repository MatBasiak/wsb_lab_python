import threading

# #zad1------------------------
# lock = threading.Lock() # stworzenie instancji obiektu Lock
#
# result = []
#
# # funkcja numbers generująca kolejny ciąg liczb wg zadanego wzoru
# def numbers(i):
#     for k in range(0, 9):
#         lock.acquire()
#         result.append(10 * i + k)
#         lock.release()
#
#
# threads = [] # lista zawierająca wszystkie wątki
#
# # kilejne wątki z zadanymi parametrami
# t1 = threading.Thread(target=numbers, args=(1,))
# t2 = threading.Thread(target=numbers, args=(5,))
# t3 = threading.Thread(target=numbers, args=(6,))
# t4 = threading.Thread(target=numbers, args=(9,))
#
# #wypełnienie listy wątkami
# threads.append(t1)
# threads.append(t2)
# threads.append(t3)
# threads.append(t4)
#
# # uruchomienie wątków
# for thread in threads:
#     thread.start()
# #zakończenie wątków
# for thread in threads:
#     thread.join()
#
# # print(result)

# zad2--------------------------------------------
print("--------------------")
import urllib.request
import time

webpages = []  # zawiera adresy stron przekazanych przez użytkownika
code_lenght = []  # zawiera długość kodu poszczególnych stron internetowych

lock = threading.Lock() # instancja obiektu Lock
# pobieranie adresów od uzytkownika i dodanie ich do listy webpages
for i in range(1, 6):
    adress = input(f"Podaj URL {i}: ")
    webpages.append(adress)

print("Rozpoczynanie pobierania...")

# funkcja pobierająca kod żrodłówy podanej strony
def request_url(url):
    lock.acquire()
    try:
        url = urllib.request.urlopen(url) # pobranie kodu
        code_lenght.append(len(url.read())) # przekazanie do listy code_lenght długości kodu
    except Exception as e:
        print(e)
    lock.release()


threads = [] # tablica z wątkami

# stworzenie wątków na podstawie ilości podanych adresów stron.
for i in range(0, len(webpages)):
    thread = threading.Thread(target=request_url, args=(webpages[i],))
    threads.append(thread)# wpisanie wątku do listy threads

# uruchomienie wszystkich wątków
for thread in threads:
    thread.start()

is_active = True # flaga warująca działanie pętli

while is_active:
    for thread in threads:
        if thread.is_alive(): # sprawdzenie czy wątek wciąż jest aktywny
            print("Oczekiwanie na zakończenie pobierania...")
            time.sleep(1)
        else:
            is_active = False
            print("Wszystko pobrano.")
            break

# zamknięcie wątków
for thread in threads:
    thread.join()
# wyświetlenie adresu strony i ilości znaków jej kodu
for i in range(0, len(code_lenght)):
    print(f"Liczba znaków dla {webpages[i]}: {code_lenght[i]}")

