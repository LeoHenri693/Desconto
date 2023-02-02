n1=int(input('insira um número:  '))
n2=int(input('insira um número:  '))
result=n1+n2
n3=int(input('valor de desconto'))
print('resultado:',result)
result2=((n1+n2)/100)*n3
result3=(result-result2)
print('resultado',result)
print('porcentagem',result3)