# Substitua a String com nomes separados por vírgulas e espaços
nomes = "Exemplo1, Exemplo2, Exemplo3."

# Divide usando a vírgula como parâmetro
nomes_divididos = nomes.split(", ")

# Imprima cada nome na tela
for nome in nomes_divididos:
    print(nome)