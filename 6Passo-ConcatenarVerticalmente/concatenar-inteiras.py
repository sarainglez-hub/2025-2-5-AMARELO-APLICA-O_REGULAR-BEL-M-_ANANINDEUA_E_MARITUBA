"""
Propósito: concatenar verticalmente as imagens inteiras da pasta 'inteiras' (sem sufixos de lado)
Autor: Alexandre Nassar de Peder
Criação: 02/10/2025
Atualização: 03/06/2026

OBS1: Este script busca as imagens diretamente da pasta "inteiras".

OBS2: O objetivo deste passo é empilhar as imagens inteiras na ordem correta para formar uma única imagem final.

OBS3: Este código vai criar uma imagem final chamada "colunas_concatenadas_inteiras.png".
"""

from PIL import Image
import os
import re

# Pasta contendo as imagens inteiras
pasta_imagens = "inteiras"
pasta_saida = "."
os.makedirs(pasta_saida, exist_ok=True)

# Extrai qualquer número do nome do arquivo para ordenar (ex: pagina_1.png -> 1)
def get_sort_key(nome_arquivo):
    match = re.search(r'(\d+)', nome_arquivo)
    return int(match.group(1)) if match else 0

# Verifica se a pasta 'inteiras' existe
if not os.path.exists(pasta_imagens):
    print(f"ERRO: A pasta '{pasta_imagens}' não foi encontrada no diretório atual.")
else:
    # Pegar apenas imagens .png que NÃO contenham '_esquerda' nem '_direita'
    arquivos = [
        f for f in os.listdir(pasta_imagens) 
        if f.endswith('.png') and '_esquerda' not in f and '_direita' not in f
    ]

    if not arquivos:
        print(f"ERRO: Nenhuma imagem válida encontrada na pasta '{pasta_imagens}'.")
    else:
        arquivos.sort(key=get_sort_key)

        # Abrir todas as imagens na ordem correta
        imagens = []
        for arquivo in arquivos:
            caminho = os.path.join(pasta_imagens, arquivo)
            imagens.append(Image.open(caminho))
            print(f"Adicionando: {arquivo}")  # Para verificar a ordem

        # Encontrar a largura máxima
        largura_max = max(img.width for img in imagens)

        # Concatenar verticalmente
        altura_total = sum(img.height for img in imagens)
        imagem_final = Image.new('RGB', (largura_max, altura_total))

        y = 0
        for img in imagens:
            imagem_final.paste(img, (0, y))
            y += img.height

        # Salvar com o novo nome solicitado
        caminho_final = os.path.join(pasta_saida, 'colunas_concatenadas_inteiras.png')
        imagem_final.save(caminho_final)

        print("\nImagens inteiras concatenadas na ordem correta!")
        print(f"Imagem final salva em: {caminho_final}")
        print(f"Ordem dos arquivos processados: {arquivos}")