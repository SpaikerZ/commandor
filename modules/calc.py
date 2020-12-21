def calculator():
    print()
    print("write number ")
    n1 = int(input())
    print("write symbol (for example / * - + % )")
    symbol = input()
    print("write number ")
    n2 = int(input())

    if (symbol == '+'):
        result = n1 + n2
        print(result)
    if (symbol == '-'):
        result = n1 - n2
        print(result)
    if (symbol == '*'):
        result = n1 * n2
        print(result)
    if (symbol == '/'):
        result = n1 / n2
        print(result)

