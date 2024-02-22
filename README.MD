# Dokumentacja programu

## Autorzy
- Karol Kuźma
- Wiktor Wenta

## Język programowania
Python

## Opis ogólny
Program działa w pętli posługując się instrukcjami od 1 do 5. Program umożliwia zarządzanie fakturami i płatnościami. Pozwala użytkownikowi dodawać nowe faktury, dokonywać płatności, sprawdzać stan faktur, importować dane z plików oraz obliczać różnice kursowe w walutach na fakturze.

# Funkcje

`pobierz_kwote(komunikat)`: Funkcja ta prosi użytkownika o podanie kwoty i sprawdza, czy podana wartość jest liczbą całkowitą. Jeśli tak, zwraca tę kwotę.

`pobierz_walute()`: Funkcja ta prosi użytkownika o podanie waluty i sprawdza, czy wprowadzona waluta znajduje się na liście obsługiwanych walut (PLN, USD, EUR, GBP). Jeśli tak, zwraca wybraną walutę.

`pobierz_date(komunikat)`: Funkcja ta prosi użytkownika o podanie daty w formacie dd-mm-rrrr i sprawdza, czy podana wartość jest poprawną datą. Jeśli tak, zwraca tę datę.

`get_exchange_rate(currency)`: Funkcja ta pobiera kurs wymiany dla określonej waluty z API Narodowego Banku Polskiego. Jeśli kurs wymiany dla danej waluty nie został jeszcze pobrany, funkcja wysyła zapytanie do API i zapisuje kurs wymiany w słowniku kursy_wymiany, aby uniknąć wielokrotnego pobierania tego samego kursu.

`dodaj_fakture()`: Funkcja ta dodaje nową fakturę do listy faktury. Pobiera kwotę, datę i walutę od użytkownika, tworzy unikalne ID faktury, a następnie dodaje fakturę do listy wraz z kwotą, datą, walutą i kwotą do zapłaty.

`dodaj_platnosc()`: Funkcja ta dodaje nową płatność do listy platnosci. Najpierw użytkownik podaje ID faktury, do której ma być dodana płatność. Jeśli faktura istnieje, pobiera kwotę płatności i walutę od użytkownika, a następnie dodaje płatność do listy wraz z datą płatności. Jeśli waluta płatności jest inna niż waluta faktury, funkcja konwertuje kwotę płatności na walutę faktury, korzystając z kursu wymiany pobranego z funkcji get_exchange_rate(currency).

`sprawdz_fakture(id_faktury)`: Funkcja ta sprawdza fakturę o podanym identyfikatorze. Jeśli faktura istnieje, wyświetla informacje o niej, w tym kwotę do zapłaty. Jeśli faktura nie istnieje, wyświetla odpowiedni komunikat.

`zapisz_do_pliku_fakture(nazwa_pliku, faktura)`: Funkcja ta przyjmuje nazwę pliku i obiekt faktury jako argumenty i zapisuje dane faktury do pliku tekstowego. Format zapisu danych jest predefiniowany w tej funkcji i zawiera ID faktury, kwotę, datę, walutę oraz kwotę do zapłaty.

# Instrukcja uruchomienia programu

Aby uruchomić program, wykonaj poniższe kroki:


1.Użyj poniższej komendy w terminalu, aby sklonować repozytorium:

```bash
git clone [link_do_repozytorium]
```
2.Przejdz do folderu z repozytorium na swoim komputerze za pomocą

```bash
cd [link_do_repozytorium]
```
3. Mając zainstalowanego pythona uruchom
```bash
python main.py
```

