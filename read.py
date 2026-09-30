from pathlib import Path

'''Função para verificar a existência do arquivo com dados de cliente e fazer a sua leitura'''

def ler_arquivo():
    pasta_atual = Path(__file__).parent
    arquivo = pasta_atual / "input_data.txt"
    
    if arquivo.is_file():
        print(f"O arquivo '{arquivo.name}' foi encontrado com sucesso!\n")
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            print("--- Conteúdo do Arquivo ---\n")
            print("---------------------------")
            print(conteudo)
            print("---------------------------")

    else:
        print(f"...Erro: O arquivo '{arquivo.name}' não foi encontrado no diretório.")