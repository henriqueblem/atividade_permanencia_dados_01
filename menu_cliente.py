from modulos import chamar_cadastrar_cliente
from modulos import chamar_leitor

'''Aqui está o bloco de código referênte ao menu principal'''

def exibir_menu():
    print()
    print('𝕄𝕖𝕟𝕦 𝕕𝕖 𝕔𝕒𝕕𝕒𝕤𝕥𝕣𝕠𝕤')
    print('1. Cadastrar Cliente')
    print('2. Exibir cadastros')
    print('3. Sair')
    print()

def menu_principal():
    while True:
        exibir_menu()
        escolha = input('Escolha a oprção desejada: ')
        
        if escolha == '1':
            chamar_cadastrar_cliente()
        elif escolha == '2':
            chamar_leitor()
        elif escolha == '3':
            print('Encerrando progrma')
            break
        else:
            print('Opção inválida. Tente novamente\n')

def chamar_menu_principal():
    return menu_principal

menu_principal()