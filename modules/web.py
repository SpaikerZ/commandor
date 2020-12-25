import webbrowser

def google():
    webbrowser.open('https://google.com', new = 2)

def maps():
    webbrowser.open('https://google.ru/maps', new = 2)

def browsers():
    print('what browser do u want? (for example: google-chrome)')
    kind = str(input())
    
