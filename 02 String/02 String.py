print("Este programa tem como objetivo verificar se a palavraou frase contem a letra A e quantas veses ela se encontra")
print("Coloque abaixo a palavra ou frase para a verificação: ")

sentenca = input()

contagem = 0

sentenca = sentenca.lower()

contagem = sentenca.count('a')

if contagem > 0:
    print("Esta(s) palavra(s) apresentam a letra A ", contagem, " veses")

if contagem == 0:
    print("Esta(s) palavra(s) não apresentam a letra A")



