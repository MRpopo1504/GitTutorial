import uuid
from datetime import datetime
import requests

faktury = []
platnosci = []
kursy_wymiany = {}  


def pobierz_kwote(komunikat):
    while True:
        kwota = input(komunikat)
        try:
            return int(kwota)
        except ValueError:
            print("Nieprawidłowe dane! Proszę podać poprawną liczbę.")

def pobierz_walute():
    while True:
        waluta = input("Waluta (PLN, USD, EUR, GBP): ").upper()
        if waluta in ["PLN", "USD", "EUR", "GBP"]:
            return waluta
        else:
            print("Nieprawidłowa waluta! Proszę wybrać spośród PLN, USD, EUR, GBP.")

def pobierz_date(komunikat):
    while True:
        data_str = input(komunikat + " (dd-mm-rrrr): ")
        try:
            return datetime.strptime(data_str, "%d-%m-%Y").date()
        except ValueError:
            print("Nieprawidłowy format daty! Proszę użyć dd-mm-rrrr.")

def get_exchange_rate(currency):
    if currency not in kursy_wymiany:
        url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["rates"][0]["mid"]
            kursy_wymiany[currency] = exchange_rate
            return exchange_rate
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    else:
        return kursy_wymiany[currency]

def dodaj_fakture():
    print("Dodaj Nową Fakturę")
    kwota = pobierz_kwote("Podaj kwotę:")
    data = pobierz_date("Podaj Datę")
    waluta = pobierz_walute()
    do_zaplaty = kwota
    id_faktury = str(uuid.uuid4())
    
    faktury.append({
        "id": id_faktury,
        "kwota": kwota,
        "data": data,
        "waluta": waluta,
        "do_zaplaty": do_zaplaty
    })
    print("Faktura została dodana pomyślnie.")

def sprawdz_fakture(id_faktury):
    faktura = next((f for f in faktury if f["id"] == id_faktury), None)
    if faktura:
        if faktura["do_zaplaty"] > 0:
            print(f"Masz do zapłaty jeszcze {faktura['do_zaplaty']} w walucie {faktura['waluta']}.")
        else:
            print("Faktura została opłacona w całości.")
    else:
        print("Nie znaleziono faktury o podanym ID.")

def dodaj_platnosc():
    print("Dodaj Nową Płatność")
    id_faktury = input("Podaj ID Faktury: ")
    faktura = next((f for f in faktury if f["id"] == id_faktury), None)
    if faktura:
        kwota = pobierz_kwote("Podaj Kwotę Płatności:")
        waluta = pobierz_walute()
        data_platnosci = datetime.now().date()

        if waluta != faktura["waluta"]:
            kurs_wymiany = get_exchange_rate(faktura["waluta"]) / get_exchange_rate(waluta)
            kwota = round(kwota * kurs_wymiany, 2)

        platnosci.append({
            "id_faktury": id_faktury,
            "kwota": kwota,
            "waluta": waluta,
            "data_platnosci": data_platnosci
        })
        faktura["do_zaplaty"] -= kwota
        print("Płatność została dodana pomyślnie.")
    else:
        print("Nie znaleziono faktury o podanym ID.")

def zapisz_do_pliku_faktury(nazwa_pliku):
    try:
        with open(nazwa_pliku, "w") as file:
            for faktura in faktury:
                file.write(f"Faktura ID: {faktura['id']}, Kwota: {faktura['kwota']} {faktura['waluta']}, Data: {faktura['data']}\n")
        print(f"Dane zostały zapisane do pliku: {nazwa_pliku}")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku: {e}")        


while True:
    print("Co chcesz zrobić?")
    print("1. Dodaj nową fakturę")
    print("2. Dodaj nową płatność")
    print("3. Wyjdź z programu")
    wybor = input("Twój wybór: ")


def dodaj_platnosc():
    print("Dodaj Nową Płatność")
    id_faktury = input("Podaj ID Faktury: ")
    faktura = next((f for f in faktury if f["id"] == id_faktury), None)
    if faktura:
        kwota = pobierz_kwote("Podaj Kwotę Płatności:")
        waluta = pobierz_walute()
        data_platnosci = datetime.now().date()

        if waluta != faktura["waluta"]:
            kurs_wymiany = get_exchange_rate(faktura["waluta"]) / get_exchange_rate(waluta)
            kwota = round(kwota * kurs_wymiany, 2)

        platnosci.append({
            "id_faktury": id_faktury,
            "kwota": kwota,
            "waluta": waluta,
            "data_platnosci": data_platnosci
        })
        faktura["do_zaplaty"] -= kwota
        print("Płatność została dodana pomyślnie.")
    else:
        print("Nie znaleziono faktury o podanym ID.")

while True:
    print("Co chcesz zrobić?")
    print("1. Dodaj nową fakturę")
    print("2. Dodaj nową płatność")
    print("3. Wyjdź z programu")
    wybor = input("Twój wybór: ")


    if wybor == "1":
        dodaj_fakture()
    elif wybor == "2":
        dodaj_platnosc()
    elif wybor == "3":
        print("Dziękujemy. Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Proszę wybrać 1, 2 lub 3.")

while True:
    print("Co chcesz zrobić?")
    print("1. Dodaj nową fakturę")
    print("2. Dodaj nową płatność")
    print("3. Sprawdź fakturę")
    print("4. Zapisz dane faktur do pliku")
    print("5. Wyjdź z programu")
    wybor = input("Twój wybór: ")

    if wybor == "1":
        dodaj_fakture()
    elif wybor == "2": 
        dodaj_platnosc()
    elif wybor == "3":
        id_faktury = input("Podaj ID Faktury: ")
        sprawdz_fakture(id_faktury)  
    elif wybor == "4":
        nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
        zapisz_do_pliku_faktury(nazwa_pliku)      
    elif wybor == "5":
        print("Dziękujemy. Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Proszę wybrać 1, 2, 3, 4 lub 5.")
