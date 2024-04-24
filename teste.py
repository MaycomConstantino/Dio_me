def recomendar_plano(consumo_medio):
    if consumo < 10:
        print("Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.")
    elif consumo > 10 and consumo <= 20:
        print("Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.")
    else:
        print("Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.")

    return consumo_medio


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Digite em GB a quantidade média do consume mensal de internet: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))