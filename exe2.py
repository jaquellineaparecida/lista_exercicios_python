# Fazer um algoritmo que lê dois números, a base e o expoente, e imprime a potência (base elevada ao 
# expoente). Dica: use a função matemática Math.pow(). Exemplo: 5 elevado ao cubo ficaria 
# Math.pow(5, 3). Você pode trocar esses números por variáveis.

print("POTENCIAÇÃO")
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
potencia = pow(base, expoente)
print("Seu resultado é: " + str(potencia))