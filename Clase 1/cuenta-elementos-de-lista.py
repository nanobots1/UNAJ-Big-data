cadena = []
text = open("libro.txt", mode='r', encoding='utf-8-sig')
for line in text:
    for i in line.split():
        cadena.append(i.split()[0])
text.close()

frecuenciaPalab = [cadena.count(w) for w in cadena] 

print(str(list(zip(cadena, frecuenciaPalab))))