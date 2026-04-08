tarefas = []
status = ["A fazer", "Fazendo", "Feito"]


def adicionar_status(status_dado):
    status.append(status_dado)


def adicionar_tarefa():
    titulo = input("Título: ")
    responsavel = input("Responsável: ")

    tarefa = {
        "titulo": titulo,
        "responsavel": responsavel,
        "status": "A fazer"
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        print(f"{i+1} - {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")


def mudar_status():
    try:
        listar_tarefas()
        tarefa_alterar = input("Qual tarefa deseja alterar? ")
        encontrada = False
        novo_status = None
        for tarefa in tarefas:
            if tarefa["titulo"] == tarefa_alterar:
                encontrada = True
                adicionado = None
                print('Esses são os status adicionados até o momento: ')
                for status_adicionado in status:
                    print(status_adicionado)
                novo_status = input("Qual será o novo status? ")
                for status_adicionado in status:
                    if novo_status == status_adicionado:
                        adicionado = True
                if not adicionado:

                    status_adicionar = input('Vimos que este status não está na sua lista de status, deseja adicioná-lo a lista? (S/N)').lower().strip()
                    if status_adicionar == "s":
                        adicionar_status(novo_status)
                    else:
                        print("Certo, ele não será adicionado a lista de status porém o status da tarefa sera mudado.")

                tarefa["status"] = novo_status
                print("Status alterado com sucesso!")
                break

        if not encontrada:
            print("Tarefa não encontrada, tente novamente!")

    except:
        print("Algum erro inesperado ocorreu, tente novamente!")


def mostrar_por_status():
    quantidade = 0
    for status_adicionado in status:
        print(status_adicionado)
    status_selecionado = input('Deseja mostrar por qual status?')

    try:
        for i, tarefa in enumerate(tarefas):
            if tarefa["status"] == status_selecionado:
                quantidade += 1
                print(f"{i+1} | {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")

        print(f"Foram encontradas {quantidade} tarefas")

    except:
        print("Algum erro inesperado aconteceu!")


def deletar_tarefa():
    listar_tarefas()
    try:
        tarefa_pos = int(input('Qual é a posição da tarefa que deseja deletar?')) - 1
        for i, tarefa in enumerate(tarefas):
            if i == tarefa_pos:
                print(f"{i+1} | {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")
                confirm = input('Deseja realmente deletar esta tarefa? (S/N)').lower().strip()
                if confirm == "s":
                    tarefas.pop(i)
                    print('Tarefa deletada com sucesso!')
                else:
                    print('Ação cancelada.')

    except:
        print("Algum erro inesperado aconteceu, tente novamente!")


def limpar_tarefas():
    global tarefas
    tarefas = []