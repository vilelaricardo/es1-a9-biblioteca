"""Confere se o computador está pronto para a Atividade A9.

Execute dentro da pasta do repositório:
    python3 conferir_ambiente.py
No Windows, troque python3 por py.
"""

import subprocess
import sys
from pathlib import Path

PYTHON_MINIMO = (3, 8)
PYTEST_MINIMO = (7, 0)
PYLINT_MINIMO = (3, 2)


def versao_instalada(pacote):
    """Devolve a versão instalada do pacote, ou None se ele não estiver instalado."""
    try:
        from importlib.metadata import PackageNotFoundError, version
    except ImportError:
        return None
    try:
        return version(pacote)
    except PackageNotFoundError:
        return None


def numeros_da_versao(versao):
    """Converte "3.2.7" em (3, 2)."""
    partes = versao.split(".")
    numeros = []
    for parte in partes[:2]:
        digitos = ""
        for caractere in parte:
            if not caractere.isdigit():
                break
            digitos = digitos + caractere
        if digitos == "":
            digitos = "0"
        numeros.append(int(digitos))
    return tuple(numeros)


def arquivos_alterados():
    """Lista os arquivos do repositório alterados desde o download, ou None se não houver como saber."""
    if not Path(".git").is_dir():
        return None
    try:
        resultado = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    except OSError:
        return None
    if resultado.returncode != 0:
        return None
    alterados = []
    for linha in resultado.stdout.splitlines():
        if not linha.startswith("??"):
            alterados.append(linha[3:])
    return alterados


def main():
    problemas = 0
    comando = "py" if sys.platform.startswith("win") else "python3"
    # Dentro de um ambiente virtual, o pip não aceita a opção --user.
    if sys.prefix != sys.base_prefix:
        comando = comando + " -m pip install"
    else:
        comando = comando + " -m pip install --user"
    print("Python em uso:", sys.executable)
    print()

    versao_python = sys.version_info[:2]
    if versao_python < PYTHON_MINIMO:
        print("[PROBLEMA] Python", sys.version.split()[0], "é antigo demais. Instalem o Python 3.8 ou mais novo.")
        sys.exit(1)
    print("[ok] Python", sys.version.split()[0])

    if not Path("biblioteca.py").is_file() or not Path("testes").is_dir():
        print("[PROBLEMA] O terminal não está na pasta do repositório. Pasta atual:", Path.cwd())
        print("           Usem o comando cd para entrar na pasta onde está o arquivo biblioteca.py.")
        sys.exit(1)
    print("[ok] Pasta do repositório")

    for pacote, minimo in (("pytest", PYTEST_MINIMO), ("pylint", PYLINT_MINIMO)):
        versao = versao_instalada(pacote)
        if versao is None:
            print("[PROBLEMA]", pacote, "não está instalado para este Python. Executem:")
            print("          ", comando, "-r requirements.txt")
            problemas = problemas + 1
        elif numeros_da_versao(versao) < minimo:
            print("[PROBLEMA]", pacote, versao, "é antigo demais. Executem:")
            print("          ", comando, "--upgrade", pacote)
            problemas = problemas + 1
        else:
            print("[ok]", pacote, versao)

    alterados = arquivos_alterados()
    if alterados:
        print("[PROBLEMA] Arquivos alterados desde o download:", ", ".join(alterados))
        print("           Para desfazer as alterações, executem: git restore .")
        problemas = problemas + 1
    elif alterados is not None:
        print("[ok] Nenhum arquivo do repositório foi alterado")

    print()
    if problemas == 0:
        print("Tudo pronto. Podem seguir o roteiro da atividade.")
    else:
        print("Resolvam os itens marcados com PROBLEMA e executem este comando de novo.")
        print("O guia técnico da atividade explica cada caso.")
        sys.exit(1)


if __name__ == "__main__":
    main()
