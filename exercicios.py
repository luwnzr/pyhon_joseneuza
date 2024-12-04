"""PASSO 01 - SEQUÊNCIAS BÁSICAS"""

#Questão 1 - Escreva um programa que mostre na tela a mensagem "Olá, Mundo!
print("Olá, Mundo!")

#Questão 2 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boasvindas para ela:
nome = input("Escreva seu nome ")
print(f"Olá {nome}, é um prazer te conhecer ")

#Questão 3 -  Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
funcionario = input("Nome do funcionario: ")
salario = float(input("Escreva seu salário: "))
print(f"O funcionario {funcionario}, tem um sálario de {salario:.2f} em Junho.")

#Questão 4 - Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles."""
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
soma = a + b
print(f"A soma entre {a} e {b} é igual a {soma}.")

#Questão 5 - Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
media = (nota1 + nota2) / 2
print(f"A média entre {nota1} e {nota2} é igual a {media:.1f}")

#Questão 6 - Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
numero = int(input("Digite um número inteiro: "))
antecessor = numero -1
sucessor = numero +1
print(f"O antecessor de {numero} é igual a {antecessor} ")
print(f"O sucessor de {numero} é igual a {sucessor} ")

#Questão 7 - Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
numero = float(input("Digite um número: "))
dobro = numero * 2
terço = numero / 3
print(f"O dobro de {numero} é {dobro}, e a terça parte de {numero} é {terço:.1f}")

#Questão 8 - Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
metros = float(input("Digite uma distância em metros: "))
print(f"A distância de {metros}m corresponde a:")
print(f"{metros / 1000} Km")
print(f"{metros / 100} Hm")
print(f"{metros / 10} Dam")
print(f"{metros * 10} dm")
print(f"{metros * 100} cm")
print(f"{metros * 1000} mm")

#Questão 9
reais = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = reais / 3.45
print(f"Com R${reais:.2f} você pode comprar US${dolar:.2f}")

#Questão 10
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta = area / 2
print(f"A área da parede é {area} m² e você precisará de {tinta:.1f} litros de tinta.")

#Questão 11
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b**2 - 4 * a * c
print(f"O valor de Delta é {delta}")

#Questão 12
preco = float(input("Digite o preço do produto: R$"))
desconto = preco * 0.05
preco_promocional = preco - desconto
print(f"O preço promocional com 5% de desconto é R${preco_promocional:.2f}")

#Questão 13
salario = float(input("Digite o salário do funcionário: R$"))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O novo salário com 15% de aumento é R${novo_salario:.2f}")

#Questão 14
km_percorridos = float(input("Quantos Km foram percorridos? "))
dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
preco_total = (dias_alugados * 90) + (km_percorridos * 0.20)
print(f"O preço total a pagar é R${preco_total:.2f}")

#Questão 15
dias_trabalhados = int(input("Quantos dias foram trabalhados no mês? "))
horas_por_dia = 8
salario_por_hora = 25
salario_mensal = dias_trabalhados * horas_por_dia * salario_por_hora
print(f"O salário mensal é R${salario_mensal:.2f}")

#Questão 16
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

# Calculando a perda total de tempo em minutos
tempo_perdido_minutos = cigarros_por_dia * 10 * 365 * anos_fumando
tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)
print(f"Você perdeu aproximadamente {tempo_perdido_dias:.1f} dias de vida devido ao fumo.")

"""PASSO 02 - CONDIÇÕES BÁSICAS"""

#Questão 17
velocidade = float(input("Qual é a velocidade do carro em Km/h? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado! O valor da multa é de R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade.")

#Questão 18
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2024 - ano_nascimento
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você ainda não pode votar.")
  
#Questão 19
nome = input("Nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média do aluno {nome} é {media:.2f}")
if media >= 7.0:
    print("Bom aproveitamento!")
else:
    print("Aproveitamento insuficiente.")
  
#Questão 20
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")
    
#Questão 21
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
  
#Questão 22
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2024 - ano_nascimento
if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
elif idade == 18:
    print("Você deve se alistar este ano!")
else:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
  
#Questão 23
nome = input("Nome do cliente: ")
sexo = input("Sexo (M/F): ").strip().upper()
valor_compras = float(input("Valor das compras: R$"))

if sexo == 'F':
    desconto = valor_compras * 0.13
else:
    desconto = valor_compras * 0.05

preco_final = valor_compras - desconto
print(f"O preço final para {nome} é R${preco_final:.2f}")
  
#Questão 24
distancia = float(input("Qual é a distância da viagem em Km? "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da passagem é R${preco:.2f}")
  
#Questão 25
lado1 = float(input("Digite o primeiro segmento de reta: "))
lado2 = float(input("Digite o segundo segmento de reta: "))
lado3 = float(input("Digite o terceiro segmento de reta: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos não podem formar um triângulo.")

"""PASSO 03 - CONDIÇÕES COMPOSTAS"""

#Qestão 26
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro valor é o maior")
elif num2 > num1:
    print("O segundo valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")

#Qestão 27
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"Média: {media:.2f}")

if media < 5.0:
    print("REPROVADO")
elif 5.0 <= media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")

#Questão 28
largura = float(input("Digite a largura do terreno (m): "))
comprimento = float(input("Digite o comprimento do terreno (m): "))
area = largura * comprimento

print(f"Área do terreno: {area:.2f}m²")

if area < 100:
    print("Classificação: TERRENO POPULAR")
elif 100 <= area <= 500:
    print("Classificação: TERRENO MASTER")
else:
    print("Classificação: TERRENO VIP")

#Questão 29
nome = input("Nome do funcionário: ")
salario = float(input("Salário atual: R$"))
anos = int(input("Anos de trabalho na empresa: "))

if anos < 3:
    aumento = salario * 0.03
elif 3 <= anos < 10:
    aumento = salario * 0.125
else:
    aumento = salario * 0.20

novo_salario = salario + aumento
print(f"Novo salário de {nome}: R${novo_salario:.2f}")

#Questão 30
a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos podem formar um triângulo", end=' ')
    if a == b == c:
        print("EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("Os segmentos não podem formar um triângulo")

#Questão 31
import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(opcoes)
jogador = input("Escolha (Pedra, Papel, Tesoura): ").capitalize()

print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == 'Pedra' and computador == 'Tesoura') or \
     (jogador == 'Papel' and computador == 'Pedra') or \
     (jogador == 'Tesoura' and computador == 'Papel'):
    print("Você venceu!")
else:
    print("Computador venceu!")

#Questão 32
import random

numero = random.randrange(1, 6)
tentativa = int(input("Adivinhe o número entre 1 e 5: "))

if tentativa == numero:
    print("Parabéns! Você acertou!")
else:
    print(f"Errado! O número era {numero}.")

#Questão 33
valor_casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos para pagar? "))
prestacao = valor_casa / (anos * 12)

print(f"Prestação mensal: R${prestacao:.2f}")

if prestacao > salario * 0.30:
    print("Empréstimo negado.")
else:
    print("Empréstimo aprovado!")

#Questão 34
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

#Questão 35
tipo = input("Tipo de carro (popular/luxo): ").lower()
dias = int(input("Dias de aluguel: "))
km = float(input("Km percorridos: "))

if tipo == 'popular':
    preco = dias * 90
    preco += 0.20 * km if km <= 100 else 0.10 * km
else:
    preco = dias * 150
    preco += 0.30 * km if km <= 200 else 0.25 * km

print(f"Preço total: R${preco:.2f}")

#Questão 36
horas = float(input("Horas de atividade no mês: "))

if horas <= 10:
    pontos = horas * 2
elif horas <= 20:
    pontos = horas * 5
else:
    pontos = horas * 10

dinheiro = pontos * 0.05
print(f"Pontos: {pontos}, Dinheiro ganho: R${dinheiro:.2f}")

#Questão 37
salario = float(input("Salário atual: R$"))
genero = input("Gênero (M/F): ").upper()
anos = int(input("Anos na empresa: "))

if genero == 'F':
    if anos < 15:
        aumento = 0.05
    elif anos <= 20:
        aumento = 0.12
    else:
        aumento = 0.23
else:
    if anos < 20:
        aumento = 0.03
    elif anos <= 30:
        aumento = 0.13
    else:
        aumento = 0.25

novo_salario = salario * (1 + aumento)
print(f"Novo salário: R${novo_salario:.2f}")

"""PASSO 04 – REPETIÇÕES ENQUANTO"""

#Exemplo While 1
cont = 1
while cont <= 10:
    print(cont)
    cont = cont + 1

#Exemplo While 2
cont = 0
while cont <=50:
    print(cont)
    cont = cont + 5
else:
    print("O valor de cont passou de 50 ", cont)

#Questão 38 - Escreva um programa que mostre na tela a seguinte contagem: 6 7 8 9 10 11 Acabou
cont = 6
while cont <= 11 :
    print(cont)
    cont = cont + 1
else :
    print("Acabou")

#Questão 39 - Faça um algoritmo que mostre na tela a seguinte contagem: 10 9 8 7 6 5 4 3 Acabou
cont = 10
while cont >= 3 :
    print(cont)
    cont = cont - 1
else :
    print("Acabou")

#Questão 40 -  Crie um aplicativo que mostre na tela a seguinte contagem: 0 3 6 9 12 15 18 Acabou!
cont = 0
while cont <= 18 :
    print(cont)
    cont = cont + 3
else :
    print("Acabou")

#Questão 41 - Desenvolva um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou!
cont = 100
while cont >= 0 :
    print(cont)
    cont = cont - 5
else :
    print("Acabou")

#Questão 42 -  Faça um algoritmo que pergunte ao usuário um número inteiro e positivo qualquer e mostre uma contagem até esse valor:
#Ex: Digite um valor: 35 Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou
inteiro = int(input("Digite um numero inteiro positivo"))
cont = 1
while cont <= inteiro :
    print(cont)
    cont = cont + 1
else :
    print("Acabou")

#Questão 43 - CDesenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1, marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...
contador = 30
while (contador >= 1):
    if contador%4==0:
        print(f"[{contador}]")
    else:
        print(contador)
    contador = contador - 1
else:    
    print("Acabou!")

#Questão 44 -  Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
#Ex: Digite o primeiro Valor: 3
#Digite o último Valor: 10
#Digite o incremento: 2
#Contagem: 3 5 7 9 Acabou!

primeiro_valor = int(input("Digite o primeiro valor: "))
ultimo_valor = int(input("Digite o ultimo valor: "))
incremento = int(input("Digite o incremento: "))

while primeiro_valor <= ultimo_valor:
    print(primeiro_valor, end=" ")
    primeiro_valor = primeiro_valor + incremento
print("Acabou")
                
                
#Questão 45 - O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.
primeiro_valor = int(input("Digite o primeiro valor: "))
ultimo_valor = int(input("Digite o ultimo valor: "))
incremento = int(input("Digite o incremento: "))

if primeiro_valor > ultimo_valor:
    aux = primeiro_valor
    primeiro_valor = ultimo_valor
    ultimo_valor = aux

while primeiro_valor <= ultimo_valor:
    print(primeiro_valor, end=" ")
    primeiro_valor = primeiro_valor + incremento
print("Acabou")

#Questão 46 - Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
soma = 0
for num in range (6,102,2):
    soma = soma + num

print("Soma = ", soma)

#Questão 47 - Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0

soma = 0
for cont in range(1,4):
    num = int(input('Digite um n25úmero:'))
    soma = soma + num
print('Soma dos numeros', soma)

#Questão 48 - Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
soma = 0
cont = 1
while cont <= 7:
    numero = int(input(f'Digite o {cont}° número'))
    soma += numero
    print(f'A soma dos números é: {soma}')
    cont += 1

#49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
pares = 0
impares = 0
contador = 1
while contador <= 6:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1
print(f"Pares: {pares}, Ímpares: {impares}")

#50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
#a) Quais foram os números sorteados
#b) Quantos números estão acima de 5
#c) Quantos números são divisíveis por 3
import random

numeros = []
contador = 1
while contador <= 20:
    numero = random.randint(0, 10)
    numeros.append(numero)
    contador += 1

print(f"Números sorteados: {numeros}")

acima_5 = 0
div3 = 0
contador = 0
while contador < 20:
    if numeros[contador] > 5:
        acima_5 += 1
    if numeros[contador] % 3 == 0:
        div3 += 1
    contador += 1

print(f"Quantos números estão acima de 5: {acima_5}")
print(f"Quantos números são divisíveis por 3: {div3}")

# 51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.

maior_preco = float(input("Digite o preço do produto 1: "))
menor_preco = maior_preco

contador = 2
while contador <= 8:
    preco = float(input(f"Digite o preço do produto {contador}: "))
    if preco > maior_preco:
        maior_preco = preco
    if preco < menor_preco:
        menor_preco = preco
    contador += 1

print(f"Maior preço: {maior_preco}")
print(f"Menor preço: {menor_preco}")

# 52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

soma_idades = 0
mais_de_18 = 0
menos_de_5 = 0
maior_idade = 0
contador = 1

while contador <= 10:
    idade = int(input(f"Digite a idade da pessoa {contador}: "))
    soma_idades += idade
    
    if idade > 18:
        mais_de_18 += 1
    if idade < 5:
        menos_de_5 += 1
    if idade > maior_idade:
        maior_idade = idade
    
    contador += 1

media_idade = soma_idades / 10
print(f"Média de idade: {media_idade:.2f}")
print(f"Pessoas com mais de 18 anos: {mais_de_18}")
print(f"Pessoas com menos de 5 anos: {menos_de_5}")
print(f"Maior idade lida: {maior_idade}")

# 53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos

soma_idades = 0
soma_idades_homens = 0
homens = 0
mulheres = 0
mulheres_mais_20 = 0
contador = 1

while contador <= 5:
    idade = int(input(f"Digite a idade da pessoa {contador}: "))
    sexo = input(f"Digite o sexo da pessoa {contador} (M/F): ").strip().upper()
    
    soma_idades += idade
    
    if sexo == 'M':
        homens += 1
        soma_idades_homens += idade
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulheres_mais_20 += 1
    
    contador += 1

media_idade = soma_idades / 5
if homens > 0:
    media_idade_homens = soma_idades_homens / homens
else:
    media_idade_homens = 0

print(f"Quantidade de homens cadastrados: {homens}")
print(f"Quantidade de mulheres cadastradas: {mulheres}")
print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Média de idade dos homens: {media_idade_homens:.2f}")
print(f"Mulheres com mais de 20 anos: {mulheres_mais_20}")

# 54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

soma_alturas = 0
mais_de_90kg = 0
menos_50kg_menos_1_60m = 0
mais_1_90m_mais_100kg = 0
contador = 1

while contador <= 7:
    peso = float(input(f"Digite o peso da pessoa {contador} (kg): "))
    altura = float(input(f"Digite a altura da pessoa {contador} (m): "))
    
    soma_alturas += altura
    
    if peso > 90:
        mais_de_90kg += 1
    if peso < 50 and altura < 1.60:
        menos_50kg_menos_1_60m += 1
    if altura > 1.90 and peso > 100:
        mais_1_90m_mais_100kg += 1
    
    contador += 1

media_altura = soma_alturas / 7

print(f"Média de altura do grupo: {media_altura:.2f}")
print(f"Pessoas que pesam mais de 90Kg: {mais_de_90kg}")
print(f"Pessoas com peso menor que 50Kg e altura menor que 1.60m: {menos_50kg_menos_1_60m}")
print(f"Pessoas com altura maior que 1.90m e peso maior que 100Kg: {mais_1_90m_mais_100kg}")

# 55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. O computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 tentativas para tentar acertar.

import random

numero_sorteado = random.randint(1, 10)
tentativas = 4

print("Bem-vindo ao jogo! Tente adivinhar o número entre 1 e 10.")

while tentativas > 0:
    tentativa = int(input(f"Você tem {tentativas} tentativas restantes. Qual é o seu palpite? "))
    
    if tentativa == numero_sorteado:
        print("Parabéns! Você acertou o número!")
        tentativas = 0  # Zera as tentativas para terminar o jogo
    else:
        tentativas -= 1
        if tentativa < numero_sorteado:
            print("O número sorteado é maior. Tente novamente!")
        elif tentativa > numero_sorteado:
            print("O número sorteado é menor. Tente novamente!")

if tentativas == 0 and tentativa != numero_sorteado:
    print(f"Você não acertou! O número sorteado era {numero_sorteado}.")

DESAFIO

numero = int(input("Digite um valor múltiplo de 10: "))

if numero % 10 != 0:
    print("Número inválido. O número deve ser múltiplo de 10.")
else:
    
    c100 = numero // 100
    numero %= 100  # Atualiza o valor com o restante após retirar as cédulas de 100
   
    c50 = numero // 50
    numero %= 50  # Atualiza o valor com o restante após retirar as cédulas de 50
    
    c20 = numero // 20
    numero %= 20  # Atualiza o valor com o restante após retirar as cédulas de 20

    c10 = numero // 10
    numero %= 10  # Atualiza o valor com o restante após retirar as cédulas de 10

    
    if c100 > 0:
        print(f"{c100} nota(s) de 100.00")
    if c50 > 0:
        print(f"{c50} nota(s) de 50.00")
    if c20 > 0:
        print(f"{c20} nota(s) de 20.00")
    if c10 > 0:
        print(f"{c10} nota(s) de 10.00")

DESAFIO 2
#Criar um programa que o computador faça um sorteio de um numero de 1 ate 100 
#E você terá que adivinhar o número sorteado, a cada vez que colocar o numero o computador terá que exibir a mensagem:
#- você acertou o número;
#- o número digitado é menor que o numero sorteado
#- o numero digitado é maior que o numero sorteado
#- o jogo poderá terminar quando você acertar o número ou quando for feita 10 tentativas
import random

sorteio = random.randint(1, 100)

tentativas = 0

while tentativas < 10:
    jogador = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1  

    if jogador == sorteio:
        print(f"Você acertou! O número sorteado era {sorteio}.")
        break  
    elif jogador < sorteio:
        print("O número digitado é menor que o sorteado.")
    else:
        print("O número digitado é maior que o sorteado.")

    if tentativas == 10:
        print(f"Você atingiu o número máximo de tentativas. O número sorteado era {sorteio}.")

DESAFIO 3
# Inicializando as variáveis para contar os votos
Candidato_a = 0
Candidato_b = 0
Candidato_c = 0
Candidato_d = 0
Candidato_e = 0
votos_nulos = 0
votos_brancos = 0
total_votos = 0

# Iniciando o loop de votação
resposta = 'S'  # Começa com a opção de continuar a votação

while resposta == 'S' or resposta == 's':  # Enquanto a resposta for 'S' ou 's'
    # Solicita o voto
    voto = input("Escreva o número do candidato em que deseja votar (1-5). Qualquer outro número será considerado voto nulo: ")

    # Verifica qual candidato foi escolhido ou se o voto é nulo
    if voto == "1":
        Candidato_a += 1
        print("Você votou no Candidato A.")
    elif voto == "2":
        Candidato_b += 1
        print("Você votou no Candidato B.")
    elif voto == "3":
        Candidato_c += 1
        print("Você votou no Candidato C.")
    elif voto == "4":
        Candidato_d += 1
        print("Você votou no Candidato D.")
    elif voto == "5":
        Candidato_e += 1
        print("Você votou no Candidato E.")
    else:
        votos_nulos += 1
        print("Voto nulo.")

    # Aumenta o total de votos
    total_votos += 1

    # Pergunta se deseja votar novamente
    resposta = input("Deseja votar novamente? (S/N): ").upper()

# Exibe os resultados finais
print("Resultados finais:")
print(f"Total de votos: {total_votos}")
print(f"Candidato A: {Candidato_a} votos")
print(f"Candidato B: {Candidato_b} votos")
print(f"Candidato C: {Candidato_c} votos")
print(f"Candidato D: {Candidato_d} votos")
print(f"Candidato E: {Candidato_e} votos")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos brancos: {votos_brancos}")

# Determina o vencedor de forma manual
if Candidato_a > Candidato_b and Candidato_a > Candidato_c and Candidato_a > Candidato_d and Candidato_a > Candidato_e:
    vencedor = "Candidato A"
elif Candidato_b > Candidato_a and Candidato_b > Candidato_c and Candidato_b > Candidato_d and Candidato_b > Candidato_e:
    vencedor = "Candidato B"
elif Candidato_c > Candidato_a and Candidato_c > Candidato_b and Candidato_c > Candidato_d and Candidato_c > Candidato_e:
    vencedor = "Candidato C"
elif Candidato_d > Candidato_a and Candidato_d > Candidato_b and Candidato_d > Candidato_c and Candidato_d > Candidato_e:
    vencedor = "Candidato D"
elif Candidato_e > Candidato_a and Candidato_e > Candidato_b and Candidato_e > Candidato_c and Candidato_e > Candidato_d:
    vencedor = "Candidato E"
else:
    vencedor = "Nenhum candidato, empate"

# Exibe o vencedor
print(f"O vencedor da eleição é: {vencedor}")

#Exemplo For in
for cont in range(10):
    print(cont)

for cont in range(20,30):
    print(cont)
    
for cont in range(50,100,5):
    print(cont)

#Exemplo Lista
lista = ['Maria', 'Joao', 'Ana']
print(lista)
lista.append('Marcos')

print(lista)
for nome in lista:
    print(nome)

numeros = [10,20,30,50,60,80]
print('Soma = ', sum(numeros))
print('Total de numeros = ', len(numeros))
print('Menor Valor = ', min(numeros))
print('Maior Valor = ', max(numeros))

# EX 1 : No python criar uma aplicação que defina uma lista co o nome dos alunos da turma.
# E em seguida faça o sorteio de um dos nomes da lista.
import random
lista = ['Maria', 'Luane', 'Riklemy', 'Emilly', 'Pedro', 'Lara', 'Tiago', 'Izabela', 'Luciel', 'Nicolas', 'Samuel', 'Nathan', 'Nathan Aguiar', 'Danilo', 'Leandro', 'Bia', 'Vinicius', 'Ingrid', 'Debora', 'Yasmin']
for nome in lista:
    print(nome)
    
tamanho_lista = len(lista)
num_sorteado = random.randint(0, tamanho_lista + 1)

print(f'O aluno Sorteado foi: {lista[num_sorteado]}')

# EX 2: Refaça o exercício anterior para ler a quantidade de nomes para sortear.
# Exemplo: Quantos nomes deseja sortear? 5
# Então, deverá ser feito 5 sorteios dentro da lista

import random

alunos = ['Maria', 'Luane', 'Riklemy', 'Emilly', 'Pedro', 'Lara', 'Tiago', 'Izabela', 'Luciel', 'Nicolas', 'Samuel', 'Nathan', 'Nathan Aguiar', 'Danilo', 'Leandro', 'Bia', 'Vinicius', 'Ingrid', 'Debora', 'Yasmin']
quantidade = int(input('Quantos nomes deseja sortear? '))

if quantidade > len(alunos):
    print('O numero de nomes a serem sorteados é maior do que o número de alunos.')
    print(f'Temos apenas {len(alunos)}alunos.')
else:
    print('Nomes sorteados')
    for contador in range(quantidade):
        nome_sorteado = random.choice(alunos)
        print(nome_sorteado)

# Criar um jogo de pedra, papel e tesoura no qual o computador é um dos jogadores. Ao final de cada jogada devera perguntar:
# Qual sua opção de jogada?
# 1 -  Pedra 
# 2 -  Palel 
# 3 - Tesoura
# Opção : 1
# Você escolheu Pedra e o computador Pedra - EMPATE, JOGAR NOVAMENTE (S/N) ?

import random

jogo = ["PEDRA", "PAPEL", "TESOURA"]
meus_pontos = 0
computador_pontos = 0

while True:
    print("Escolha uma das opções (Pedra / Papel / Tesoura)")
    opcao = input("Escolha uma das opções: ").upper()
    computador = random.choice(jogo)

    if opcao == computador:
        print("Empate")
        print("Você escolheu:", opcao)
        print("Computador escolheu:", computador)

    elif opcao == "PEDRA":
        if computador == "TESOURA":
            meus_pontos += 1
            print("Você ganhou")
            print("Você escolheu:", opcao)
            print("Computador escolheu:", computador)
        else:
            computador_pontos += 1
            print("Computador ganhou")
            print("Você escolheu:", opcao)
            print("Computador escolheu:", computador)

    elif opcao == "TESOURA":
        if computador == "PAPEL":
            meus_pontos += 1
            print("Você ganhou")
            print("Você escolheu:", opcao)
            print("Computador escolheu:", computador)
        else:
            computador_pontos += 1
            print("Computador ganhou")
            print("Você escolheu:", opcao)
            print("Computador escolheu:", computador)

    elif opcao == "PAPEL":
        if computador == "PEDRA":
            meus_pontos += 1
            print("Você ganhou")
            print("Você escolheu:", opcao)
            print("Computador escolheu:", computador)
        else:
            computador_pontos += 1
            print("Computador ganhou")
            print("Você escolheu:", opcao)
            print("Computador escolheu:", computador)

    resposta = input("Deseja jogar novamente (S/N)? ").upper()
    if resposta != "S":
        break

print("Resultado Final")
print("Meus pontos:", meus_pontos, "Pontos")
print("Computador pontos:", computador_pontos, "Pontos")

# Criar um programa que leia um numero e exiba a tabuada de multiplicação do numero que foi lido.
# Exemplo: Digite um número: 7
# 7 x 1 = 4, 7 x 2 = 14, 7 x 3 = 21...

numero = int(input('Escreva um numero: '))
cont = 1
for cont in range(1,11):
    print(numero, 'X', cont, '=', numero*cont)
