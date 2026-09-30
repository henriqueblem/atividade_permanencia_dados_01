'''Função que cadastra o cliente e cria o arquivo inicial com esses dados inseridos'''
from pathlib import Path

def cadastrar_cliente():
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    telefone = input('Digite seu n° de telefone: ')

    arquivo = Path(__file__).parent / "input_data.txt"
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(f'Nome: {nome}\n')
        f.write(f'Idade: {idade}\n')
        f.write(f'Telefone: {telefone}\n')
        print('___ Cadastro concluido ___')


# Aqui podemos mudar a função para "a" (append) no lugar do "w" para que adicione e não sobrescreva o arquivo.
# Ou adicionar uma nova funcionalidade para faze-lo e fazer as alterações no menu principal.