print("Este programa tem como objetivo verificar se um dado numero é pertencente a sequencia de Fibonacci")
print("Coloque abaixo o numero para a verificação: ")

numero = int(input())

var0 = 0
var1 = 0
var2 = 1
igual = 0

while var1 <= numero:
    var0 = var2
    var2 = var1 + var2
    var1 = var0
    if var1 == numero:
        igual = var1
        
    
if var1 == numero or igual == numero:
    print ("o numero digitado faz parte da sequencia de Fibonacci")
else :
    print ("O numero Não Faz parte da sequencia de Fibonacci")