r'''dia=input('Dia?')
mes= input('Mês?')
ano= input('Ano?')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano,' Correto?')'''

a=int(input('Qual o primeiro numero?'))
b=int(input('Qual o segundo numero?'))

soma = a + b
#print('A soma entre',a,'e',b,'vale:', soma)

print('A soma entre {} e {} vale {}'.format(a, b, soma))