names = ['Laura', 'Juan', 'Pedro']
ages = [18, 23, 26]
pairs = [[names[i], ages[i]] for i in range(len(names))]
print(pairs)

origen = [1, 2]
llegada = [3, 4, 5]
combinacion = [[origen[i], llegada[j]] for i in range(len(origen)) for j in range(len(llegada))]
print(combinacion)