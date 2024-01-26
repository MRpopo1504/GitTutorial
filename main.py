import datetime
from urllib import response
import requests

courses = ["PLN",]
body = requests.get('https://api.nbp.pl/api/exchangerates/tables/a')
response = body.json()

for rate in response[0]['rates']:
    courses.append((rate['code']))


print("Podaj dane dotyczący faktury")
def biling_input_amount():
    
    print("Podaj kwotę")
    raw_input = input()
    try:
        amount = float(raw_input)
        print("Wprowadzona liczba jako float:", amount)
    except ValueError:
        print("nieprawidłowa kwota")
        biling_input_amount()

biling_input_amount

    ##########
def biling_input_course():
    
    print("Podaj kurs")
    raw_input = input()
    try:
        course = float(raw_input)
        print("Wprowadzona liczba jako float:", course)
    except ValueError:
        print("nieprawidłowa kwota")
        biling_input_course()

biling_input_course()

#####

def biling_input_date():
    
    day = int()
    month = int()
    year = int()

    print("Podaj rok, następnie miesiąc, następnie dzień")
    raw_input = input()
    try:
        day = int(raw_input)
    except ValueError:
        print("nieprawidłowa dane")
        biling_input_date()

    raw_input = input()
    try:
        month = int(raw_input)
    except ValueError:
        print("nieprawidłowa dane")
        biling_input_date()
    raw_input = input()
    try:
        year = int(raw_input)
    except ValueError:
        print("nieprawidłowa dane")
        biling_input_date()
    date = datetime.datetime(year, month, year)
    print(date)

biling_input_date()



