lista = [1,4,67,59]
a=sum(lista)
print('Somma della lista: {}'.format(a))

def somma (list):
    sum=0
    for element in list:
        sum=sum+element
    return sum
risultato = somma (lista)
print('Somma della lista:{}'.format(risultato))