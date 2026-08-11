#10% de desconto sobre o valor total da compra. solicite valor do produto e quantidade. 
#calcule valor total, aplique o desconto e informe o valor final.

valor_produto = float(input("Qual o valor do produto? "))
quantidade = int(input("Quantas unidades você irá comprar? "))

preço_bruto = float(valor_produto*quantidade)

DESCONTO = 0.9

valor_desconto = float(preço_bruto*DESCONTO)

print(f"O valor sem desconto é R${preço_bruto}. Com os 10% de desconto, você irá pagar R${valor_desconto}.")
