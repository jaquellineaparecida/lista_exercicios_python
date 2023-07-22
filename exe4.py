# Fazer um algoritmo que lê dois números inteiros e imprime os números consecutivos desses números. (Por 
# exemplo: se o usuário digitar 2 e -9, a saída deverá ser 3 e -8, porque 3 é consecutivo de 2. –8 é consecutivo 
# de –9)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
cons_n1 = 0
cons_n2 = 0

if n1 < n2:
    cons_n1 = n1 + 1
    cons_n2 = n2 - 1

else:
   cons_n1 = n1 + 1
   cons_n2 = n2 - 1

print(f"Consecutivo de {n1}: {cons_n1}")
print(f"Consecutivo de {n2}: {cons_n2}")




