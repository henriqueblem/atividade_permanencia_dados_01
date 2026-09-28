from pathlib import Path

'''Função para verificar a existência do arquivo com dados de cliente e fazer a sua leitura'''

def ler_arquivo():
    caminho_pasta = r"C:\Users\servidor_imperial\Desktop\DEV\Cursos\Alura\Códigos e Projetos\2026\Python Permanencia de dados"
    nome_arquivo = "input_data.txt"
    arquivo = Path(caminho_pasta) / nome_arquivo

    if arquivo.is_file():
        print(f"O arquivo '{nome_arquivo}' foi encontrado com sucesso!\n")
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            print("--- Conteúdo do Arquivo ---\n")
            print(conteudo)
            print("---------------------------")

    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório")