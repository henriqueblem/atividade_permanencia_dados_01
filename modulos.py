'''Está aqui uma camada de atalhos, as importações poderiam ser feitas diretamente pelo main.py também'''

from read import ler_arquivo
from input_data import cadastrar_cliente

def chamar_leitor():
    return ler_arquivo()

def chamar_cadastrar_cliente():
    return cadastrar_cliente()