'''Função que cadastra o cliente e cria o arquivo inicial com esses dados inseridos'''

def cadastrar_cliente():
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    telefone = input('Digite seu n° de telefone: ')

    with open('input_data.txt', 'w') as f:
        f.write(f'Nome: {nome}\n')
        f.write(f'Idade: {idade}\n')
        f.write(f'Telefone: {telefone}\n')