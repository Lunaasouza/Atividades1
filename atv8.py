distancia = float(input("Digite a distância da viagem em km: "))
combustivel = float (input ("Digite consumo combustivel do carro em km/l: "))
valor_combustivel = float (input ("Digite o valor do combustivel em R$: "))

litros = distancia / combustivel
custo = litros * valor_combustivel  

print(f"Quantidade de litros necessária: {litros:.2f}")
print(f"Custo total da viagem: R$ {custo:.2f}")
