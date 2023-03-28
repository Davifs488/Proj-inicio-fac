#/Exemplo de lista (mutavel)com numeros /
#/Evolouindo com os exemplo da faculdade

numeros = list(range(0,21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)