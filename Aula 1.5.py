numeros = [x for x in range(101)]
primos = list()

divisores = [x for x in numeros if x != 0]

for num in numeros:

    soma_divisores = 0

    for d in divisores:

        if num % d == 0:
            soma_divisores += 1

        elif num < d:
            break

    if soma_divisores == 2:
        primos.append(num)

print(primos)