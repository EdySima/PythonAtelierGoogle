# 1
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)

# 2
lista_ord_cresc = lista.copy()
lista_ord_cresc.sort()
print(F"\n{lista}")
print(lista_ord_cresc)


# 3
lista_ord_descr = lista.copy()
lista_ord_descr.sort(reverse=True)
print(F"\n{lista}")
print(lista_ord_descr)

# 4
temp = slice(1, len(lista), 2)
print(F"\n{lista}")
print(lista[temp])

# 5
temp = slice(0, len(lista), 2)
print(F"\n{lista}")
print(lista[temp])

# 6
multiple_of_3 = []
for i in lista:
    if i % 3 == 0:
        multiple_of_3.append(i)
print(F"\n{multiple_of_3}")

