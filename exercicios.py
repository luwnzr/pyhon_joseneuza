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

"""Qestão 26"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro valor é o maior")
elif num2 > num1:
    print("O segundo valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")

"""Qestão 27"""
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
cont = 6
soma = 0
while cont <= 100:
    soma = soma + cont
    cont = cont + 2

print("Soma é igual ", soma)

#Questão 47 - Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
cont = 500
soma = 0
while cont >= 0:
    soma = soma + cont
    cont = cont - 50 

print("Soma é igual ", soma)

#Questão 48 - Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
soma = 0
cont = 1
while cont <= 7:
    numero = int(input(f'Digite o {cont}° número'))
    soma += numero
    print(f'A soma dos números é: {soma}')
    cont += 1

#Questão 49 - Contagem de pares e ímpares em 6 números
pares = impares = 0
for _ in range(6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Pares: {pares}, Ímpares: {impares}")

#Questão 50 - Sorteio de 20 números entre 0 e 10
import random

sorteados = [random.randint(0, 10) for _ in range(20)]
print("Números sorteados:", sorteados)
acima_de_5 = sum(1 for num in sorteados if num > 5)
divisiveis_por_3 = sum(1 for num in sorteados if num % 3 == 0)
print(f"Números acima de 5: {acima_de_5}")
print(f"Números divisíveis por 3: {divisiveis_por_3}")

#Questão 51 - Leitura do preço de 8 produtos e identificação do maior e menor
precos = [float(input("Digite o preço do produto: R$")) for _ in range(8)]
print(f"Maior preço: R${max(precos):.2f}")
print(f"Menor preço: R${min(precos):.2f}")

#Questão 52 - Análise de idades em um grupo de 10 pessoas
idades = [int(input("Digite a idade: ")) for _ in range(10)]
media = sum(idades) / 10
mais_18 = sum(1 for idade in idades if idade > 18)
menos_5 = sum(1 for idade in idades if idade < 5)
print(f"Média de idade: {media:.1f}")
print(f"Pessoas com mais de 18 anos: {mais_18}")
print(f"Pessoas com menos de 5 anos: {menos_5}")
print(f"Maior idade: {max(idades)}")

#Questão 53 - Análise de idade e sexo de 5 pessoas
homens = mulheres = total_idade = idade_homens = mulheres_mais_20 = 0

for _ in range(5):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()
    total_idade += idade

    if sexo == 'M':
        homens += 1
        idade_homens += idade
    else:
        mulheres += 1
        if idade > 20:
            mulheres_mais_20 += 1

media_idade = total_idade / 5
media_homens = idade_homens / homens if homens > 0 else 0
print(f"Homens cadastrados: {homens}")
print(f"Mulheres cadastradas: {mulheres}")
print(f"Média de idade do grupo: {media_idade:.1f}")
print(f"Média de idade dos homens: {media_homens:.1f}")
print(f"Mulheres com mais de 20 anos: {mulheres_mais_20}")

#Questão 54 - Análise de peso e altura de 7 pessoas
altura_total = peso_mais_90 = baixo_peso_altura = altos_pesados = 0

for _ in range(7):
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
    altura_total += altura

    if peso > 90:
        peso_mais_90 += 1
    if peso < 50 and altura < 1.60:
        baixo_peso_altura += 1
    if altura > 1.90 and peso > 100:
        altos_pesados += 1

media_altura = altura_total / 7
print(f"Média de altura: {media_altura:.2f}m")
print(f"Pessoas com mais de 90kg: {peso_mais_90}")
print(f"Pessoas abaixo de 50kg e 1.60m: {baixo_peso_altura}")
print(f"Pessoas acima de 1.90m e 100kg: {altos_pesados}")

#Questão 55 - Jogo de adivinhação com 4 tentativas
import random

numero_sorteado = random.randint(1, 10)
tentativas = 4

while tentativas > 0:
    palpite = int(input("Adivinhe o número (1-10): "))
    if palpite == numero_sorteado:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        print(f"Errado! Você tem {tentativas} tentativas restantes.")
if tentativas == 0:
    print(f"Você perdeu! O número era {numero_sorteado}.")