import os
import zipfile

import requests


def download_file(url: str | None, filename: str) -> str:
    """Função para baixar um arquivo de uma URL

    Args:
        url: URL do arquivo a ser baixado
        filename: Nome do arquivo a ser salvo (sem extensão)

    Returns:
        path: path do arquivo baixado
    """
    if url is None:
        raise ValueError("URL is None")
    print('Baixando arquivo: ', url)
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', '')
    path = f"{filename}.{content_type.split('/')[-1]}"
    with open(path, "wb") as f:
        f.write(response.content)
    return path


def zip_files(file_paths: list[str], zip_path: str):
    """Função para zipar arquivos

    Args:
        file_paths: Lista de paths dos arquivos a serem zipados
        zip_path: Path do arquivo zip a ser criado
    """
    print(f'Zipando arquivos: {file_paths} no arquivo {zip_path}')
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in file_paths:
            zipf.write(file, os.path.basename(file))
            os.remove(file)
