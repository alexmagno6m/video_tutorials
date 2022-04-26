notas = [33, 28, 40, 25, 45]
valorations = ['bajo' if notas[i] < 30 else 'basico' if notas[i] <= 40
               else 'superior' for i in range(len(notas))]
print(valorations)