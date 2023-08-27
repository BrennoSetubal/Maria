import os
import yaml


def ler_arquivo_yaml(caminho_arquivo):
    caminho_absoluto = os.path.abspath(caminho_arquivo)

    with open(caminho_absoluto, 'r', encoding='utf-8') as arquivo:
        data = yaml.load(arquivo, Loader=yaml.FullLoader)

    return data


if __name__ == "__main__":
    caminho_arquivo = 'nlu/comandos.yml'
    data = ler_arquivo_yaml(caminho_arquivo)
    print(data)
