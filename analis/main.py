something = "write sentenses"


print()
print(something)
print(" \"\"\" ")

sentenses = str(input())

massiv = [(sentenses)]
print(massiv)

c = 'cucamber'
a = []
a.append(c)
print(a)

print(sentenses)

print()
print()

#x = 0
y = []
z = []
for i in sentenses:
    if i != ' ':
        
        y.append(i)
#        x += 1
        #print(i)
    elif i ==' ':
#        x += 1
        new_word = str()
        for word in y:
            new_word += str(word)
        z.append(new_word)
        y.clear()
print(z)



"""
for i in sentenses:
    b = 0

    z = {}

    a=' '

    if i != a:
        print(i)
    elif i == a:
        s = 0
        continue
        z[b] = sentenses
        s += 1
    
    
    
    b += 1
"""
