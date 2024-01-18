#Entrada de dados
velocidadeMs = float(input("Digite a velocidade em metros por segundo (m/s): "))

# Realiza a conversão para quilômetros por hora (1 m/s = 3.6 km/h)
velocidadeKmph = velocidadeMs * 3.6

# Exibe o resultado da conversão
print(f"A velocidade de {velocidadeMs} m/s é igual a {velocidadeKmph} km/h")