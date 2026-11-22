
"""
PlanoBase - Gestão de sessões de estudo.

Permite agendar, consultar, editar e cancelar sessões.
"""

from datetime import datetime
from dados import guardar_dados
from tarefas import escolher_disciplina


def validar_data_hora(data, hora):
    """Valida a data e a hora de uma sessão."""
    try:
        datetime.strptime(
            f"{data} {hora}", "%d/%m/%Y %H:%M"
        )
        return True
    except ValueError:
        return False


def escolher_sessao(dados):
    """Seleciona uma sessão pelo ID."""
    if not dados["sessoes"]:
        print("Não existem sessões registadas.")
        return None

    listar_sessoes(dados)
    escolha = input("ID da sessão: ").strip()

    for sessao in dados["sessoes"]:
        if str(sessao["id"]) == escolha:
            return sessao

    print("Sessão não encontrada.")
    return None


def agendar_sessao(dados):
    """Agenda uma nova sessão de estudo."""
    print("\n--- AGENDAR SESSÃO ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    data = input("Data (DD/MM/AAAA): ").strip()
    hora = input("Hora de início (HH:MM): ").strip()

    if not validar_data_hora(data, hora):
        print("Data ou hora inválida.")
        return

    try:
        duracao = int(input("Duração em minutos: "))
        if duracao <= 0:
            raise ValueError
    except ValueError:
        print("A duração deve ser um número positivo.")
        return

    novo_id = max(
        (s["id"] for s in dados["sessoes"]),
        default=0
    ) + 1

    sessao = {
        "id": novo_id,
        "disciplina_id": disciplina["id"],
        "data": data,
        "hora": hora,
        "duracao": duracao,
        "estado": "Agendada"
    }

    dados["sessoes"].append(sessao)
    guardar_dados(dados)
    print("Sessão agendada com sucesso!")


def listar_sessoes(dados):
    """Apresenta as sessões de estudo."""
    print("\n--- SESSÕES DE ESTUDO ---")

    if not dados["sessoes"]:
        print("Não existem sessões registadas.")
        return

    for sessao in dados["sessoes"]:
        disciplina = next(
            (
                d["nome"] for d in dados["disciplinas"]
                if d["id"] == sessao["disciplina_id"]
            ),
            "Disciplina removida"
        )

        print(f"\nID: {sessao['id']}")
        print(f"Disciplina: {disciplina}")
        print(f"Data: {sessao['data']}")
        print(f"Hora: {sessao['hora']}")
        print(f"Duração: {sessao['duracao']} minutos")
        print(f"Estado: {sessao['estado']}")
        print("-" * 35)


def editar_sessao(dados):
    """Permite alterar uma sessão existente."""
    print("\n--- EDITAR SESSÃO ---")

    sessao = escolher_sessao(dados)
    if sessao is None:
        return

    print("Deixa vazio para manter o valor atual.")

    data = input(f"Data ({sessao['data']}): ").strip()
    hora = input(f"Hora ({sessao['hora']}): ").strip()
    duracao = input(
        f"Duração ({sessao['duracao']} min): "
    ).strip()

    nova_data = data or sessao["data"]
    nova_hora = hora or sessao["hora"]

    if not validar_data_hora(nova_data, nova_hora):
        print("Data ou hora inválida.")
        return

    if duracao:
        try:
            nova_duracao = int(duracao)
            if nova_duracao <= 0:
                raise ValueError
        except ValueError:
            print("Duração inválida.")
            return
    else:
        nova_duracao = sessao["duracao"]

    sessao["data"] = nova_data
    sessao["hora"] = nova_hora
    sessao["duracao"] = nova_duracao

    guardar_dados(dados)
    print("Sessão atualizada com sucesso!")


def concluir_sessao(dados):
    """Marca uma sessão como concluída."""
    print("\n--- CONCLUIR SESSÃO ---")

    sessao = escolher_sessao(dados)
    if sessao is None:
        return

    sessao["estado"] = "Concluída"
    guardar_dados(dados)
    print("Sessão concluída!")


def cancelar_sessao(dados):
    """Cancela uma sessão de estudo."""
    print("\n--- CANCELAR SESSÃO ---")

    sessao = escolher_sessao(dados)
    if sessao is None:
        return

    confirmar = input(
        "Confirmar cancelamento? (s/n): "
    ).strip().lower()

    if confirmar == "s":
        sessao["estado"] = "Cancelada"
        guardar_dados(dados)
        print("Sessão cancelada!")
    else:
        print("Operação cancelada.")


def eliminar_sessao(dados):
    """Remove definitivamente uma sessão."""
    print("\n--- ELIMINAR SESSÃO ---")

    sessao = escolher_sessao(dados)
    if sessao is None:
        return

    confirmar = input(
        "Eliminar definitivamente? (s/n): "
    ).strip().lower()

    if confirmar == "s":
        dados["sessoes"].remove(sessao)
        guardar_dados(dados)
        print("Sessão eliminada!")
    else:
        print("Operação cancelada.")


def menu_sessoes(dados):
    """Apresenta o submenu das sessões."""
    while True:
        print("\n===== SESSÕES DE ESTUDO =====")
        print("1. Agendar sessão")
        print("2. Listar sessões")
        print("3. Editar sessão")
        print("4. Concluir sessão")
        print("5. Cancelar sessão")
        print("6. Eliminar sessão")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            agendar_sessao(dados)
        elif opcao == "2":
            listar_sessoes(dados)
        elif opcao == "3":
            editar_sessao(dados)
        elif opcao == "4":
            concluir_sessao(dados)
        elif opcao == "5":
            cancelar_sessao(dados)
        elif opcao == "6":
            eliminar_sessao(dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
