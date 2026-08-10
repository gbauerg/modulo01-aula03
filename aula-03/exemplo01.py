#Veiculo percorre 10km p/ litro (pensar duas distancise definir combustivel necessário)

distancia1 = float(input("Qual a primeira distância em Kilometros? "))
distancia2 = float(input("Qual a segunda distância em Kilometros? "))

somadistancia = distancia1 + distancia2

AUTONOMIA = 10 #Constante em upcase

consumocombustivel1 = distancia1/AUTONOMIA
consumocombustivel2 = distancia2/AUTONOMIA
consumototal = somadistancia/AUTONOMIA

print(f"A distância percorrida foi {somadistancia}Km.")
print(f"O consumo no primeiro trecho foi {consumocombustivel1}L. No segundo trecho, {consumocombustivel2}L. O consumo total foi {consumototal}L")