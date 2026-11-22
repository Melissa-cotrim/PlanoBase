
"""
Módulo de gestão de utilizadores do PlanoBase.

Permite criar, consultar e editar o perfil do estudante.
"""

from dados import guardar_dados


def criar_perfil(dados):
    """Cria um novo perfil de estudante."""
    print("\n--- CRIAR PERFIL ---")

    if dados["utilizador"] is not None:
        print("Já existe um perfil registado.")
        return

    nome = input("Nome do estudante: ").strip()
    curso = input("Curso: ").strip()

    if not nome or not curso:
        print("Erro: o nome e o curso são obrigatórios.")
        return

    dados["utilizador"] = {
        "nome": nome,
        "curso": curso
    }

    if guardar_dados(dados):
        print("Perfil criado com sucesso!")


def consultar_perfil(dados):
    """Apresenta os dados do perfil existente."""
    print("\n--- CONSULTAR PERFIL ---")

    utilizador = dados["utilizador"]

    if utilizador is None:
        print("Ainda não existe um perfil registado.")
        return

    print(f"Nome: {utilizador['nome']}")
    print(f"Curso: {utilizador['curso']}")


def editar_perfil(dados):
    """Permite alterar o nome e o curso do estudante."""
    print("\n--- EDITAR PERFIL ---")

    utilizador = dados["utilizador"]

    if utilizador is None:
        print("Não existe nenhum perfil para editar.")
        return

    print("Deixa o campo vazio para manter o valor atual.")

    nome = input(f"Nome ({utilizador['nome']}): ").strip()
    curso = input(f"Curso ({utilizador['curso']}): ").strip()

    if nome:
        utilizador["nome"] = nome

    if curso:
        utilizador["curso"] = curso

    if guardar_dados(dados):
        print("Perfil atualizado com sucesso!")


def menu_utilizadores(dados):
    """Apresenta o submenu de gestão do perfil."""
    while True:
        print("\n===== GESTÃO DE UTILIZADORES =====")
        print("1. Criar perfil")
        print("2. Consultar perfil")
        print("3. Editar perfil")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            criar_perfil(dados)
        elif opcao == "2":
            consultar_perfil(dados)
        elif opcao == "3":
            editar_perfil(dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tenta novamente.")