
"""
Gestão de disciplinas e tópicos do PlanoBase.

Implementa operações CRUD e persistência em JSON.
"""

from dados import guardar_dados


def escolher_disciplina(dados):
    """Permite selecionar uma disciplina pelo seu número."""
    disciplinas = dados["disciplinas"]

    if not disciplinas:
        print("Ainda não existem disciplinas registadas.")
        return None

    print("\n--- DISCIPLINAS ---")
    for numero, disciplina in enumerate(disciplinas, start=1):
        print(f"{numero}. {disciplina['nome']}")

    escolha = input("Número da disciplina: ").strip()

    if not escolha.isdigit():
        print("Introduz um número válido.")
        return None

    indice = int(escolha) - 1

    if indice < 0 or indice >= len(disciplinas):
        print("Disciplina não encontrada.")
        return None

    return disciplinas[indice]


def adicionar_disciplina(dados):
    """Regista uma nova disciplina."""
    print("\n--- ADICIONAR DISCIPLINA ---")

    nome = input("Nome da disciplina: ").strip()
    docente = input("Nome do docente: ").strip()
    ects_texto = input("Número de ECTS: ").strip()

    if not nome or not docente:
        print("O nome e o docente são obrigatórios.")
        return

    try:
        ects = float(ects_texto.replace(",", "."))
        if ects <= 0:
            raise ValueError
    except ValueError:
        print("O número de ECTS deve ser positivo.")
        return

    for disciplina in dados["disciplinas"]:
        if disciplina["nome"].lower() == nome.lower():
            print("Já existe uma disciplina com esse nome.")
            return

    disciplina = {
        "id": max(
            (d.get("id", 0) for d in dados["disciplinas"]),
            default=0
        ) + 1,
        "nome": nome,
        "docente": docente,
        "ects": ects,
        "topicos": []
    }

    dados["disciplinas"].append(disciplina)
    guardar_dados(dados)
    print("Disciplina adicionada com sucesso!")


def listar_disciplinas(dados):
    """Apresenta todas as disciplinas registadas."""
    print("\n--- LISTA DE DISCIPLINAS ---")

    if not dados["disciplinas"]:
        print("Não existem disciplinas registadas.")
        return

    for disciplina in dados["disciplinas"]:
        print(f"\nID: {disciplina['id']}")
        print(f"Nome: {disciplina['nome']}")
        print(f"Docente: {disciplina['docente']}")
        print(f"ECTS: {disciplina['ects']}")
        print(f"Tópicos: {len(disciplina['topicos'])}")
        print("-" * 30)


def editar_disciplina(dados):
    """Altera os dados de uma disciplina existente."""
    print("\n--- EDITAR DISCIPLINA ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    print("Deixa vazio para manter o valor atual.")

    nome = input(f"Nome ({disciplina['nome']}): ").strip()
    docente = input(f"Docente ({disciplina['docente']}): ").strip()
    ects_texto = input(f"ECTS ({disciplina['ects']}): ").strip()

    if nome:
        for outra in dados["disciplinas"]:
            if (outra is not disciplina
                    and outra["nome"].lower() == nome.lower()):
                print("Já existe outra disciplina com esse nome.")
                return

    if ects_texto:
        try:
            ects = float(ects_texto.replace(",", "."))
            if ects <= 0:
                raise ValueError
        except ValueError:
            print("Número de ECTS inválido.")
            return
        disciplina["ects"] = ects

    if nome:
        disciplina["nome"] = nome

    if docente:
        disciplina["docente"] = docente

    guardar_dados(dados)
    print("Disciplina atualizada com sucesso!")


def eliminar_disciplina(dados):
    """Elimina uma disciplina após confirmação."""
    print("\n--- ELIMINAR DISCIPLINA ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    print(f"Disciplina selecionada: {disciplina['nome']}")
    print("Os tópicos associados também serão eliminados.")

    confirmar = input("Confirmar eliminação? (s/n): ").lower()

    if confirmar != "s":
        print("Operação cancelada.")
        return

    dados["disciplinas"].remove(disciplina)
    guardar_dados(dados)
    print("Disciplina eliminada com sucesso!")


def adicionar_topico(dados):
    """Adiciona um tópico a uma disciplina."""
    print("\n--- ADICIONAR TÓPICO ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    nome = input("Nome do tópico: ").strip()

    if not nome:
        print("O nome do tópico é obrigatório.")
        return

    topico = {
        "id": max(
            (t.get("id", 0) for t in disciplina["topicos"]),
            default=0
        ) + 1,
        "nome": nome,
        "concluido": False
    }

    disciplina["topicos"].append(topico)
    guardar_dados(dados)
    print("Tópico adicionado com sucesso!")


def listar_topicos(dados):
    """Apresenta os tópicos de uma disciplina."""
    print("\n--- LISTAR TÓPICOS ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    if not disciplina["topicos"]:
        print("Esta disciplina ainda não tem tópicos.")
        return

    for topico in disciplina["topicos"]:
        estado = "Concluído" if topico["concluido"] else "Pendente"
        print(f"{topico['id']}. {topico['nome']} - {estado}")


def escolher_topico(disciplina):
    """Seleciona um tópico pelo seu número na lista."""
    topicos = disciplina["topicos"]

    if not topicos:
        print("Não existem tópicos nesta disciplina.")
        return None

    for numero, topico in enumerate(topicos, start=1):
        print(f"{numero}. {topico['nome']}")

    escolha = input("Número do tópico: ").strip()

    if not escolha.isdigit():
        print("Número inválido.")
        return None

    indice = int(escolha) - 1

    if indice < 0 or indice >= len(topicos):
        print("Tópico não encontrado.")
        return None

    return topicos[indice]


def editar_topico(dados):
    """Altera o nome ou estado de um tópico."""
    print("\n--- EDITAR TÓPICO ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    topico = escolher_topico(disciplina)
    if topico is None:
        return

    nome = input(f"Nome ({topico['nome']}): ").strip()

    if nome:
        topico["nome"] = nome

    resposta = input("Marcar como concluído? (s/n/Enter para manter): ")
    resposta = resposta.strip().lower()

    if resposta == "s":
        topico["concluido"] = True
    elif resposta == "n":
        topico["concluido"] = False

    guardar_dados(dados)
    print("Tópico atualizado com sucesso!")


def eliminar_topico(dados):
    """Elimina um tópico de uma disciplina."""
    print("\n--- ELIMINAR TÓPICO ---")

    disciplina = escolher_disciplina(dados)
    if disciplina is None:
        return

    topico = escolher_topico(disciplina)
    if topico is None:
        return

    confirmar = input(
        f"Eliminar o tópico '{topico['nome']}'? (s/n): "
    ).strip().lower()

    if confirmar == "s":
        disciplina["topicos"].remove(topico)
        guardar_dados(dados)
        print("Tópico eliminado com sucesso!")
    else:
        print("Operação cancelada.")


def menu_disciplinas(dados):
    """Apresenta o menu de gestão de disciplinas e tópicos."""
    while True:
        print("\n===== GESTÃO DE DISCIPLINAS =====")
        print("1. Adicionar disciplina")
        print("2. Listar disciplinas")
        print("3. Editar disciplina")
        print("4. Eliminar disciplina")
        print("5. Adicionar tópico")
        print("6. Listar tópicos")
        print("7. Editar tópico")
        print("8. Eliminar tópico")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            adicionar_disciplina(dados)
        elif opcao == "2":
            listar_disciplinas(dados)
        elif opcao == "3":
            editar_disciplina(dados)
        elif opcao == "4":
            eliminar_disciplina(dados)
        elif opcao == "5":
            adicionar_topico(dados)
        elif opcao == "6":
            listar_topicos(dados)
        elif opcao == "7":
            editar_topico(dados)
        elif opcao == "8":
            eliminar_topico(dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tenta novamente.")
