#1
print("Alo Mundo")

#2
n = int(input("informe um número: "))
print("O número informado foi ", n)

# 3
n1 = int(input("informe um número: "))
n2 = int(input("informe outro número: "))
soma = n1 + n2
print("a soma dos dois números informados é: ", soma)

#4
n1 = float(input("informe sua primeira nota: "))
n2 = float(input("informa sua segunda nota: "))
n3 = float(input("informe sua terceira nota: "))
n4 = float(input("informe sua quarta nota: "))
media = (n1+n2+n3+n4) / 4
print("Sua media é: ", media)

#5
metros = float(input("quantos metros você deseja? "))
cent = 100 * metros
print("São ", cent, " centímetros")

#6
raio = float(input("Qual o tamanho do raio do círculo?"))
pi = 3.14
area = (pi*raio)**2
area_Certa = round(area, 2)
print("A área do círculo é: ", area_Certa)

#7
lado = float(input("Qual o tamamho do lado? "))
area = lado * 2
dobro_area = area * 2
print("O dobro da area é: ", dobro_area)


#8
salarioHora = float(input("Qual o seu salário? "))
qtdHoras = int(input("Quantidade de horas trabalhadas? "))
salarioTotal = salarioHora * qtdHoras
#salarioTotal = round(salarioTotal, 2)
#print("O seu salário total é: ", salarioTotal)
print(f"O seu salário total é: {salarioTotal:.2f}")


#9
far = int(input("Qual a temperatura em Farenheit? "))
celsius = (5 * (far-32) / 9)
celsius = round(celsius, 2)
print("A temperatura em Celsius é: ", celsius)

#15
salario = float(input("Qual o seu salario por hora? "))
horas = int(input("Quantas horas trabalhadas no mês? "))
salarioBruto = salario * horas
iRenda = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salarioLiquido = salarioBruto - (iRenda + inss + sindicato)
print("Seu imposto de renda é: R$ ", iRenda)
print("Você pagou R$ ", inss, " de inss.")
print("Você pagou R$ ", sindicato, " ao sindicato")
print("Seu salário liquido é: ", salarioLiquido)

