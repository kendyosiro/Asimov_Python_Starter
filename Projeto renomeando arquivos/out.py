import os
import shutil

curr_dir = os.getcwd()

diretorios = os.listdir(curr_dir)

# Filtra apenas os diretórios
diretorios = [arquivo for arquivo in diretorios if os.path.isdir(os.path.join(curr_dir, arquivo))]

for diretorio in diretorios:
    caminho_diretorio = os.path.join(curr_dir, diretorio)

    # Lista todos os arquivos e subdiretórios dentro do diretório atual
    conteudo = os.listdir(caminho_diretorio)

    for item in conteudo:
        caminho_item  = os.path.join(caminho_diretorio, item)

        shutil.move(caminho_item, curr_dir)

    # Deleta o diretório corrente
    os.rmdir(caminho_diretorio)
    print(f"Diretório '{caminho_diretorio}' deletado com sucesso.")
