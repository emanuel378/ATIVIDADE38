#Crie duas lista par e impar,faça o usuario coloca 20 numero e depois imprimir a lista par ou impar

par = []
impar = []
for n in range(20):
      numero = int(input(f"numero {n} + 1:"))
      if numero%2==0:
            par.append(numero)
      else:
            impar.append(numero)
print(par)
print(impar)