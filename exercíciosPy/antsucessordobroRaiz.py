print(' ========== ANTECESSOR, SUCESSOR, DOBRO, TRIPLO E RAIZ QUADRADA ========== ')
n = int(input('Digite um número: ')) #recebe número

#utiliza soma e sub para printar antecessor e sucessor 
print('\nVocê digitou {}, o antecessor é {} e o sucessor é {}\n'.format(n,n-1,n+1)) 

#printa dobro, triplo e raiz quadrada do número
print('O dobro deste número é {}, o triplo é {} e a raiz quadrada é {:.2f}\n'.format(n*2,n*3,n**(1/2)))