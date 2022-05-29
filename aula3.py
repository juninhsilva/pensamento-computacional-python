descontos=300
comissao=3
vendas=37800
salario_fixo=1200

vendas=vendas*comissao/100

salario_liquido = salario_fixo + vendas - descontos
print(salario_liquido)
