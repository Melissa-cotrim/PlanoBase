
"""
PlanoBase - Aplicação de Planeamento de Estudos.

Unidade Curricular: Ambientes de Desenvolvimento Colaborativo
Universidade do Algarve
"""

from dados import carregar_dados, guardar_dados
from utilizadores import menu_utilizadores


def mostrar_menu():
    """Apresenta as opções do menu principal."""
    print("\n" + "=" * 40)
    print("               PLANObASE")
    print("       Planeamento de Estudos")
    print("=" * 40)

    print("1. Gerir perfil")
    print("2. Gerir disciplinas")
    print("3. Gerir tarefas")
    print("4. Agendar sessões de estudo")
    print("5. Temporizador Pomodoro")
    print("6. Consultar estatísticas")
    print("7. Exportar relatório")
    print("8. Ajuda")
    print("0. Guardar e sair")


def main():
    """Executa o ciclo principal da aplicação."""
    dados = carregar_dados()

    print("Bem-vindo ao PlanoBase!")

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            menu_utilizadores(dados)

        elif opcao in ("2", "3", "4", "5", "6", "7", "8"):
            print("\nEsta funcionalidade será implementada em breve.")

        elif opcao == "0":
            if guardar_dados(dados):
                print("Obrigado por utilizares o PlanoBase!")
                break
            print("Não foi possível guardar. Tenta novamente.")

        else:
            print("Opção inválida. Tenta novamente.")


if __name__ == "__main__":
    main()