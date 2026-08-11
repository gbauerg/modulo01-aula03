#compra ingressos com valor limitado.

valoringresso = float(input("Qual o valor do ingresso? "))
dinheirolimite = float(input("Qual o valor máximo que você tem? "))

quantidade_ingressos = int(dinheirolimite//valoringresso)

troco = float(dinheirolimite % valoringresso)

print(f"Você pode comprar {quantidade_ingressos} ingressos.")
print(f"Seu troco será R${troco}.")