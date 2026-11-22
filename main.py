
"""
PlanoBase - Aplicação de Planeamento de Estudos.

Unidade Curricular: Ambientes de Desenvolvimento Colaborativo
Universidade do Algarve

Aplicação de consola para gerir perfis, disciplinas,
tarefas e sessões de estudo.
"""

from dados import carregar_dados, guardar_dados
from utilizadores import menu_utilizadores
from disciplinas import menu_disciplinas
from tarefas import menu_tarefas
from sessoes import menu_sessoes


def mostrar_menu():
    """Apresenta o menu principal do PlanoBase."""

    print("\n" + "=" * 45)
    print("                 PLANObASE")
    print("          Planeamento de Estudos")
    print("=" * 45)

    print("\n--- MENU PRINCIPAL ---")
    print("1. Gerir perfil")
    print("2. Gerir disciplinas e tópicos")
    print("3. Gerir tarefas e prioridades")
    print("4. Agendar e gerir sessões de estudo")
    print("5. Temporizador Pomodoro")
    print("6. Consultar estatísticas")
    print("7. Exportar relatório")
    print("8. Ajuda")
    print("0. Guardar e sair")

    print("=" * 45)


def main():
    """Inicia a aplicação e gere a navegação entre menus."""

    dados = carregar_dados()

    print("\nBem-vindo ao PlanoBase!")

    if dados["utilizador"] is not None:
        nome = dados["utilizador"]["nome"]
        print(f"Olá, {nome}! Bom estudo!")

    while True:
        mostrar_menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            menu_utilizadores(dados)

        elif opcao == "2":
            menu_disciplinas(dados)

        elif opcao == "3":
            menu_tarefas(dados)

        elif opcao == "4":
            menu_sessoes(dados)

        elif opcao == "5":
            print("\n--- TEMPORIZADOR POMODORO ---")
            print("Funcionalidade em desenvolvimento.")

        elif opcao == "6":
            print("\n--- ESTATÍSTICAS ---")
            print("Funcionalidade em desenvolvimento.")

        elif opcao == "7":
            print("\n--- EXPORTAR RELATÓRIO ---")
            print("Funcionalidade em desenvolvimento.")

        elif opcao == "8":
            print("\n--- AJUDA ---")
            print("Bem-vindo ao PlanoBase!")
            print("Utiliza os números para navegar pelos menus.")
            print("1 - Gerir o teu perfil de estudante.")
            print("2 - Organizar disciplinas e tópicos.")
            print("3 - Criar e acompanhar tarefas.")
            print("4 - Agendar sessões de estudo.")
            print("0 - Guardar os dados e sair.")

        elif opcao == "0":
            print("\nA guardar os dados...")

            if guardar_dados(dados):
                print("Dados guardados com sucesso!")
                print("Obrigado por utilizares o PlanoBase!")
                print("Até à próxima sessão de estudo!")
                break

            print("Não foi possível guardar os dados.")
            print("Tenta novamente.")

        else:
            print("\nOpção inválida!")
            print("Por favor, escolhe uma opção do menu.")


if __name__ == "__main__":
    main()
