a = 3
b = 5
print('Os valores são \033[31;40m{}\033[m e \033[7;30;41m{}\033[m!!!'.format(a, b))
nome = str(input('Qual seu nome? '))
print("Ola, Muito prazer, seja bem vindo {}{}{}".format('\033[4;31;40m',nome,'\033[m'))