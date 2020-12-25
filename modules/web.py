import webbrowser
from Database import browsers
from Database import py 

def google():
    webbrowser.open('https://google.com', new = 2)

def maps():
    webbrowser.open('https://google.ru/maps', new = 2)

def open_browsers():
    print('what browser do u want? (for example: google-chrome)')
    kind = str(input())
    for key in py :
        print(key)
        """, ' --> ', browsers[key]"""

