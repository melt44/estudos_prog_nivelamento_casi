#exercício-01
name = input("Qual seu nome?")
print(f"Bem vindo(a) {name}!")

#exercício-02

num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha outro número: "))
novo1 = num1
num1 = num2
num2 = novo1
print(num2)

#exercício-03

numero1 = int(input("Digite o primeiro número da soma: "))
numero2 = int(input("Digite o segundo número da soma: "))
print(f"O resultado da sua soma é: {numero1+numero2}")

#exercício-04

nuM1 = int(input("Digite o primeiro número que será utilizado soma, subtração, multiplicação e divisão:"))
nuM2 = int(input("Digite o segundo número:"))
soma = nuM1+nuM2
subtracao = nuM1-nuM2
multiplicacao = nuM1*nuM2
divisao = nuM1//nuM2
print(f"""O resultado da sua soma é {soma}, 
o resultado da subtração é {subtracao}, 
o resultado da sua multiplicação é {multiplicacao} 
e o resultado da divisão é {divisao}.""")

#exercício-05

horas = int(input("Digite o número de horas: "))
min = int(input("Digite o número de minutos: "))
h_m = 60
horas_minutos = horas*h_m+min
print(f"O total de minutos é: {horas_minutos}")

#exercício-06

salario = 5600
desconto = 0.85
liq = salario*desconto
print(f"O salário líquido é de aproximadamente {liq}")

#exercício-07

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
num4 = int(input("Digite o quarto valor: "))
num5 = int(input("Digite o quinto valor: "))
soma = num1+num2+num3+num4+num5
media = soma/5
print(f"A média aritmética dos 5 números é: {media}")

#exercício-08

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
tnum1 = num1*3
tnum2 = num2*3
print(f"O triplo do primeiro número é {tnum1} e o triplo do segundo número é {tnum2}.")

#exercício-09

base = int(input("Digite o valor,em metros, da base do triângulo: "))
alt = int(input("Digite o valor, em metros, da altura do triângulo: "))
b_a = base*alt
area = b_a/2
print(f"A área do triângulo é {area} metros quadrados.")

#exercício-10

raio = int(input("Digite o raio do círculo: "))
areacirc = 3.14*raio**2
circunferencia_do_circulo = 3.14*raio*2
print(f"A área do circulo é {areacirc} metros quadrados e o comprimento da circunferência é {circunferencia_do_circulo}.")

#exercício-11
 
tempFahr = int(input("Digite a temperatura em graus fahrenheit: "))
temp1 = (tempFahr-32)/1.8
print(f"{tempFahr} graus Fahrenheit equivalem a {temp1} graus Celsius.")

#exercício-12

distKm = int(input("Digite a distância em quilômetros: "))
distMilhas = distKm*0.621371
print(f"{distKm} quilômetros equivalem a aproximadamente {distMilhas} milhas.")

#exercício-13

num1 = int(input("Digite um valor: "))
antecessor_num1 = num1-1
sucessor_num1 = num1+1
print(f"""O sucessor e o antecessor do número {num1} são, respectivamente, {sucessor_num1} e {antecessor_num1}.""")

#exercício-14
diasdetrabalho = int(input("Quantos dias você trabalhou esse mês?"))
horasdetrabalho_dia = 8
reais_hora = 20
horasdetrabalho_mes = diasdetrabalho*horasdetrabalho_dia
salario = horasdetrabalho_mes*reais_hora
print(f"O seu salário é de {salario}")

#exercício-15

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite seu curso: ")

print(f"Olá, {nome}! Você tem {idade} anos e faz {curso}!")

#exercício-16

produto = int(input("Digite o valor do produto:"))
desconto = int(input("Digite o valor percentual do desconto:"))
desconto_nominal = produto*desconto/100
valor_final = produto-desconto_nominal
print(f"O valor do produto após a aplicação do desconto é {valor_final}.")

#exercício-17

numero_de_vezes = int(input("Digite o número de vezes que você quer repetir o ':)'"))
resultado = ":)"*numero_de_vezes
print(resultado)

#exercício-18
valor_salario = int(input("Digite o valor do salário:"))
valor_reajuste = int(input("Digite o valor percentual do reajuste:"))
reajuste_nominal = valor_salario*valor_reajuste/100
valor_total = valor_salario+reajuste_nominal
print(valor_total)