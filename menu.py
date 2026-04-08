from mian import limpar_tarefas, mostrar_por_status, mudar_status, listar_tarefas, adicionar_tarefa, deletar_tarefa


def menu():
    while True:
        print("[1] Adicionar Tarefas")
        print('[2] Listar Tarefas')
        print('[3] Mudar status')
        print('[4] Mostrar por status')
        print('[5] Deletar tarefa')
        print('[0] Limpar')
        op = int(input('Qual ação deseja executar? '))
        if op == 1:
            adicionar_tarefa()
        elif op == 2:
            listar_tarefas()
        elif op == 3:
            mudar_status()
        elif op == 4:
            mostrar_por_status()
        elif op == 5:

            deletar_tarefa()
        else:
            limpar_tarefas()
            menu()


menu()
