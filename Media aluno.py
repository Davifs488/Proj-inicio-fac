qtde_faltas = int (input("Digite a quantidade de faltas: "))
media_final = (input("Digite a média final: "))

if qtde_faltas <= 5 and média_final >= 7:
  print("Aluno aprovado !")
else:
    print("Aluno reprovado !")