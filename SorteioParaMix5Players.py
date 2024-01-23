import random
#Pode ser/vai ser substituido por uma entrada de dados comum em string, mas para utilizar somente colocar os nomes conforme a lista abaixo
players = ['Ale', 'Estoppa', 'Lobo', 'Kaká', 'Nega', 'Levi', 'Dani', 'Cebola', 'BDesotti13', 'Yuj1ro']
#Exibe a lista de jogadores inscritos para o sorteio
print('Jogadores que serão sorteados: ', players)
#Realiza o embaralhamento da lista de nomes
sorteio = random.shuffle(players)
#Imprime a lista de players embaralhada
print('Time A:', players[0:5])
print('Time B:', players[5:10])
