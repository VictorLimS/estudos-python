'''''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) Sindicato (3%)              : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

valorhora = float(input('Digite o valor da hora trabalhada do funcionário: R$'))
qtdhoras = float(input('Digite a quantidade de horas trabalhadas do funcionário no mês: '))

#  Calcula o salário bruto:
salariobruto = valorhora * qtdhoras

#  Calcula o desconto do sindicato (3%)
sindicato = salariobruto * 3 / 100

#  Calcula o desconto do FGTS (11%) - não desconta
fgts = salariobruto * 11 / 100

# Teste de desconto de acordo com a faixa salarial
if salariobruto <= 900:
    desconto = 0
elif salariobruto <= 1500:
    desconto = 5
elif salariobruto <= 2500:
    desconto = 10
else:
    desconto = 20

# Calcula o valor do IR
ir = (salariobruto * desconto) / 100

# Total de descontos
totaldescontos = ir + sindicato
#  Salário líquido
salarioliquido = salariobruto - totaldescontos

print(f'Salário bruto: ({valorhora} * {qtdhoras:.2f})    : R${salariobruto:.2f}')
print(f'(-) IR ({desconto}%)                   : R${ir:.2f}')
print(f'(-) Sindicato (3%)                     : R${sindicato:.2f}')
print(f'FGTS (11%)                             : R${fgts:.2f}')
print(f'Total de descontos                     : R${totaldescontos:.2f}')
print(f'Salário liquido                        : R${salarioliquido:.2f}')