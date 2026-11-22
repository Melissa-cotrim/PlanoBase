
"""
Módulo responsável pela persistência dos dados do PlanoBase.

Os dados são armazenados num ficheiro JSON.
"""

import json
from pathlib import Path


FICHEIRO_DADOS = Path(__file__).resolve().parent / "planobase_dados.json"


def carregar_dados():
    """Carrega os dados guardados ou devolve a estrutura inicial."""
    dados_iniciais = {
        "utilizador": None,
        "disciplinas": [],
        "tarefas": [],
        "sessoes": []
    }

    if not FICHEIRO_DADOS.exists():
        return dados_iniciais

    try:
        with open(FICHEIRO_DADOS, "r", encoding="utf-8") as ficheiro:
            dados = json.load(ficheiro)

        if not isinstance(dados, dict):
            raise ValueError("Formato de dados inválido.")

        for chave, valor in dados_iniciais.items():
            dados.setdefault(chave, valor)

        return dados

    except (json.JSONDecodeError, OSError, ValueError) as erro:
        print(f"Erro ao carregar os dados: {erro}")
        raise


def guardar_dados(dados):
    """Guarda os dados da aplicação num ficheiro JSON."""
    try:
        with open(FICHEIRO_DADOS, "w", encoding="utf-8") as ficheiro:
            json.dump(dados, ficheiro, indent=4, ensure_ascii=False)

        print("Dados guardados com sucesso!")
        return True

    except OSError as erro:
        print(f"Erro ao guardar os dados: {erro}")
        return False