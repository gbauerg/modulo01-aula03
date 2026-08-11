salario_atual = float(input("Qual seu salário? "))

AUMENTO = float(salario_atual * 0.18)
reajuste = float(salario_atual + AUMENTO)

print(f"Seu salário atual é R${salario_atual:.2f}. Com o aumento, passará a ser R${reajuste:.2f}")
print(f"O aumento foi de R${AUMENTO:.2f}.")
