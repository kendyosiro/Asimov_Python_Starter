import os
import shutil


curr_dir = os.getcwd()

arquivos = os.listdir(curr_dir)

arquivos_ordenados = sorted(arquivos)

for arquivo in arquivos_ordenados:
    if os.path.isfile(arquivo):
        nome, extensao = os.path.splitext(arquivo)

        if extensao != '.py':
            extensao = extensao.lower().lstrip('.')

            pasta_destino = os.path.join(curr_dir, extensao)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            caminho_origem = os.path.join(curr_dir, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)

            shutil.move(caminho_origem, caminho_destino)
