
"""
PlanoBase - Gestão de tarefas.

Permite criar, consultar, editar, eliminar e concluir tarefas.
"""

from datetime import datetime
from dados import guardar_dados


def escolher_disciplina(dados):
    """Seleciona uma disciplina existente."""
    disciplinas = dados["disciplinas"]

    if not disciplinas:
        print("Primeiro, regista uma disciplina.")
        return None

    for disciplina in disciplinas:
        print(f"{disciplina['id']}. {disciplina['nome']}")

    escolha = input("ID da disciplina: ").strip()

    for disciplina in disciplinas:
        if str(disciplina["id"]) == escolha:
            return disciplina

    print("Disciplina não encontrada.")
    return None


def escolher_tarefa(dados):
    """Seleciona uma tarefa através do seu ID."""
    if not dados["tarefas"]:
        print("Não existem tarefas registadas.")
        return None

    listar_tarefas(dados)
    escolha = input("ID da tarefa: ").strip()

    for tarefa in dados["tarefas"]:
        if str(tarefa["id"]) == escolha:
            return tarefa

    print("Tarefa não encontrada.")
    return None


def validar_data(texto):
    """Valida uma data no formato DD/MM/AAAA."""
    try:
        return datetime.strptime(texto, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        return None


def escolher_prioridade():
    """Permite escolher uma prioridade válida."""
    print("1. Alta")
    print("2. Média")
    print("3. Baixa")

    prioridades = {"1": "Alta", "2": "Média", "3": "Baixa"}
    escolha = input("Prioridade: ").strip()

    return prioridades.get(escolha)


def criar_tarefa(dados):
    """Regista uma nova tarefa de estudo."""
    print("\n--- CRIAR TAREFA ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição: ").strip()
    prazo = input("Prazo (DD/MM/AAAA): ").strip()

    if not titulo:
        print("O título é obrigatório.")
        return

    prazo = validar_data(prazo)
    if prazo is None:
        print("Data inválida.")
        return

    prioridade = escolher_prioridade()
    if prioridade is None:
        print("Prioridade inválida.")
        return

    novo_id = max(
        (t["id"] for t in dados["tarefas"]),
        default=0
    ) + 1

    tarefa = {
        "id": novo_id,
        "disciplina_id": disciplina["id"],
        "titulo": titulo,
        "descricao": descricao,
        "prazo": prazo,
        "prioridade": prioridade,
        "estado": "Pendente"
    }

    dados["tarefas"].append(tarefa)

    if guardar_dados(dados):
        print("Tarefa criada com sucesso!")


def listar_tarefas(dados):
    """Apresenta as tarefas e respetivas informações."""
    print("\n--- LISTA DE TAREFAS ---")

    if not dados["tarefas"]:
        print("Não existem tarefas registadas.")
        return

    for tarefa in dados["tarefas"]:
        disciplina = next(
            (
                d["nome"] for d in dados["disciplinas"]
                if d["id"] == tarefa["disciplina_id"]
            ),
            "Disciplina removida"
        )

        print(f"\nID: {tarefa['id']}")
        print(f"Tarefa: {tarefa['titulo']}")
        print(f"Disciplina: {disciplina}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prazo: {tarefa['prazo']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Estado: {tarefa['estado']}")
        print("-" * 35)


def editar_tarefa(dados):
    """Altera os dados de uma tarefa existente."""
    print("\n--- EDITAR TAREFA ---")

    tarefa = escolher_tarefa(dados)
    if tarefa is None:
        return

    print("Deixa vazio para manter o valor atual.")

    titulo = input(f"Título ({tarefa['titulo']}): ").strip()
    descricao = input(
        f"Descrição ({tarefa['descricao']}): "
    ).strip()
    prazo = input(f"Prazo ({tarefa['prazo']}): ").strip()

    if prazo:
        data_validada = validar_data(prazo)
        if data_validada is None:
            print("Data inválida. Alterações canceladas.")
            return
        prazo = data_validada

    print("\nAlterar prioridade?")
    print("1. Alta | 2. Média | 3. Baixa")
    print("Enter - manter atual")

    opcao = input("Escolha: ").strip()
    prioridades = {"1": "Alta", "2": "Média", "3": "Baixa"}

    if opcao and opcao not in prioridades:
        print("Prioridade inválida. Alterações canceladas.")
        return

    print("\nAlterar disciplina?")
    resposta = input("(s/n): ").strip().lower()

    if resposta not in ("s", "n"):
        print("Resposta inválida.")
        return

    nova_disciplina = None
    if resposta == "s":
        nova_disciplina = escolher_disciplina(dados)
        if nova_disciplina is None:
            return

    if titulo:
        tarefa["titulo"] = titulo
    if descricao:
        tarefa["descricao"] = descricao
    if prazo:
        tarefa["prazo"] = prazo
    if opcao:
        tarefa["prioridade"] = prioridades[opcao]
    if nova_disciplina:
        tarefa["disciplina_id"] = nova_disciplina["id"]

    guardar_dados(dados)
    print("Tarefa atualizada com sucesso!")


def concluir_tarefa(dados):
    """Marca uma tarefa como concluída."""
    print("\n--- CONCLUIR TAREFA ---")

    tarefa = escolher_tarefa(dados)
    if tarefa is None:
        return

    if tarefa["estado"] == "Concluída":
        print("Esta tarefa já está concluída.")
        return

    tarefa["estado"] = "Concluída"
    guardar_dados(dados)
    print("Tarefa marcada como concluída!")


def eliminar_tarefa(dados):
    """Elimina uma tarefa após confirmação."""
    print("\n--- ELIMINAR TAREFA ---")

    tarefa = escolher_tarefa(dados)
    if tarefa is None:
        return

    confirmar = input(
        f"Eliminar '{tarefa['titulo']}'? (s/n): "
    ).strip().lower()

    if confirmar == "s":
        dados["tarefas"].remove(tarefa)
        guardar_dados(dados)
        print("Tarefa eliminada com sucesso!")
    else:
        print("Operação cancelada.")


def menu_tarefas(dados):
    """Apresenta o submenu de gestão de tarefas."""
    while True:
        print("\n===== GESTÃO DE TAREFAS =====")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Editar tarefa")
        print("4. Marcar tarefa como concluída")
        print("5. Eliminar tarefa")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            criar_tarefa(dados)
        elif opcao == "2":
            listar_tarefas(dados)
        elif opcao == "3":
            editar_tarefa(dados)
        elif opcao == "4":
            concluir_tarefa(dados)
        elif opcao == "5":
            eliminar_tarefa(dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
