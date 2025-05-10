import random

def dados():
    return random.randint(1,100)


numSort=dados()
num=0
tent=0

print("________________O JOGO COMEÇOU____________")
while num!=numSort :
    num= int(input("Acerte o número de 1 até 100\nR="))
    if num>100 or num<1:
        print("numero invalido")
    else:
        if num>numSort:
            print("o numero é mais em baixo meu caro")
        
        if num<numSort:
            print("o numero é mais em cima meu caro")
          
    tent=tent+1
        
print("Acertou!!!!")
print("NÚMERO DE TENTATIVAS :",tent)




    