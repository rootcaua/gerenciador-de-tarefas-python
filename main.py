tarefas = []
status_disponiveis = ["A fazer", "Fazendo", "Feito"]


def adicionar_status(status_dado):
    status_dado = status_dado.strip()

    if not status_dado:
        print("Status vazio nao pode ser adicionado.")
        return False

    if status_dado in status_disponiveis:
        print("Esse status ja existe.")
        return False

    status_disponiveis.append(status_dado)
    print("Status adicionado!")
    return True


def adicionar_tarefa():
    titulo = input("Titulo: ").strip()
    responsavel = input("Responsavel: ").strip()

    if not titulo or not responsavel:
        print("Titulo e responsavel sao obrigatorios.")
        return

    tarefa = {
        "titulo": titulo,
        "responsavel": responsavel,
        "status": "A fazer",
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return False

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i} - {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")

    return True


def escolher_tarefa():
    if not listar_tarefas():
        return None

    try:
        posicao = int(input("Informe o numero da tarefa: "))
    except ValueError:
        print("Digite um numero valido.")
        return None

    indice = posicao - 1
    if indice < 0 or indice >= len(tarefas):
        print("Tarefa nao encontrada.")
        return None

    return indice


def mostrar_status_disponiveis():
    print("Status disponiveis:")
    for status in status_disponiveis:
        print(f"- {status}")


def mudar_status():
    indice = escolher_tarefa()
    if indice is None:
        return

    mostrar_status_disponiveis()
    novo_status = input("Qual sera o novo status? ").strip()

    if not novo_status:
        print("Status vazio nao e valido.")
        return

    if novo_status not in status_disponiveis:
        resposta = input("Esse status nao existe. Deseja adiciona-lo? (S/N) ").lower().strip()
        if resposta == "s":
            adicionar_status(novo_status)
        else:
            print("Status nao alterado.")
            return

    tarefas[indice]["status"] = novo_status
    print("Status alterado com sucesso!")


def mostrar_por_status():
    mostrar_status_disponiveis()
    status_selecionado = input("Deseja mostrar por qual status? ").strip()

    encontradas = [
        (i, tarefa)
        for i, tarefa in enumerate(tarefas, start=1)
        if tarefa["status"] == status_selecionado
    ]

    if not encontradas:
        print("Nenhuma tarefa encontrada para esse status.")
        return

    for i, tarefa in encontradas:
        print(f"{i} - {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")

    print(f"Foram encontradas {len(encontradas)} tarefas.")


def deletar_tarefa():
    indice = escolher_tarefa()
    if indice is None:
        return

    tarefa = tarefas[indice]
    print(f"{indice + 1} - {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")

    confirmacao = input("Deseja realmente deletar esta tarefa? (S/N) ").lower().strip()
    if confirmacao == "s":
        tarefas.pop(indice)
        print("Tarefa deletada com sucesso!")
    else:
        print("Acao cancelada.")


def limpar_tarefas():
    tarefas.clear()
    print("Todas as tarefas foram removidas.")


def exibir_menu():
    print()
    print("[1] Adicionar tarefa")
    print("[2] Listar tarefas")
    print("[3] Mudar status")
    print("[4] Mostrar por status")
    print("[5] Deletar tarefa")
    print("[6] Limpar tarefas")
    print("[0] Sair")


def executar_menu():
    while True:
        exibir_menu()
        opcao = input("Qual acao deseja executar? ").strip()

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            mudar_status()
        elif opcao == "4":
            mostrar_por_status()
        elif opcao == "5":
            deletar_tarefa()
        elif opcao == "6":
            limpar_tarefas()
        elif opcao == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    executar_menu()
