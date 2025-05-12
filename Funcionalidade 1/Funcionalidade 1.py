import os 
os.system ("cls")

try:
    with open('registros.txt', 'r') as verificação:
        verificação.close()
except FileNotFoundError:
    with open('registros.txt', 'x') as criar:
        criar.close()

movimentos = []

while True:

    ac = int(input("Selecione, escrevendo o número indicado, que tipo de ação deseja realizar:\n1 - Visualizar registros\n2 - Adicionar registros\n3 - Editar registros\n4 - Excluir registros\n5 - Visualizar por filtros\n\nDigite aqui a ação selecionada: "))

    if ac == 1:
        with open('registros.txt', 'r') as visualizar:
            conteudo = visualizar.readlines()
            print()
            
            for i in range(len(conteudo)):
                print(f"{i + 1} - {conteudo[i]}")

        escolha = input("\nDeseja realizar mais alguma ação?\nResponda com \"Sim\" ou \"Não\": ")

        if escolha == "sim" or escolha == "Sim":
            print()
            continue
        else:
            break
        
    elif ac == 2:
        with open('registros.txt', 'a') as adicionar:
            data1 = input("\nDigite o dia da realização do treino: ")
            data2 = input("\nDigite o mês da realização do treino: ")
            tipo = input("\nDigite o tipo do treino (AMRAP; EMOM; For time): ")
            tempo = input("\nDigite o tempo do treino (Em minutos): ")
            movimentos.append(input("\nDigite os movimentos realizados: "))
            adicionar.write(f"{data1}/{data2}, {tipo}, {tempo} min, {movimentos}\n")
        
        movimentos.clear()
        
        print("\nRegistro adicionado com sucesso!")
        
        escolha = input("\nDeseja realizar mais alguma ação?\nResponda com \"Sim\" ou \"Não\": ")

        if escolha == "sim" or escolha == "Sim":
            print()
            continue
        else:
            break
        
    elif ac == 3:
        print()
        lista_nova = []
        
        with open('registros.txt', 'r') as editar:
            linhas = editar.readlines()
            
            for i in range(len(linhas)):
                print(f"{i + 1} - {linhas[i]}")
            
            linha_remover = int(input("\nDigite o número da linha que deseja editar: "))
            if linha_remover <= 0 or linha_remover > len(linhas):
                print("\nA linha informada não existe. Por favor, tente novamente.")
            else:
                data1 = input("\nDigite o dia da realização do treino: ")
                data2 = input("\nDigite o mês da realização do treino: ")
                tipo = input("\nDigite o tipo do treino (AMRAP; EMOM; For time): ")
                tempo = input("\nDigite o tempo do treino (Em minutos): ")
                movimentos.append(input("\nDigite os movimentos realizados: "))
                lista_nova.append(f"{data1}/{data2}, {tipo}, {tempo} min, {movimentos}\n")
        with open('registros.txt', 'w') as editar:
            lista_editada = linhas[:linha_remover - 1] + lista_nova + linhas[linha_remover:]
            editar.write(''.join(lista_editada))
            if 0 < linha_remover <= len(linhas):
                print("\nLinha editada com sucesso!")
            
        lista_nova.clear()
        
            
        
        escolha = input("\nDeseja realizar mais alguma ação?\nResponda com \"Sim\" ou \"Não\": ")
        
        if escolha == "sim" or escolha == "Sim":
            print()
            continue
        else:
            break
        
    elif ac == 4:
        
        tipo = int(input("\nSelecione, escrevendo o número indicado, o que deseja excluir\n1 - Linha única\n2 - Todo o registro\n\nDigite aqui o método de exclusão selecionado: "))
        
        if tipo == 1:
            print()
            with open('registros.txt', 'r') as excluir:
                linhas = excluir.readlines()

                for i in range(len(linhas)):
                    print(f"{i + 1} - {linhas[i]}")

                linha_remover = int(input("\nDigite o número da linha que deseja remover: "))

                if linha_remover <= 0 or linha_remover > len(linhas):
                    print("\nA linha informada não existe. Por favor, tente novamente.")
            with open('registros.txt', 'w') as excluir:
                lista_nova =  linhas[:linha_remover - 1] + linhas[linha_remover:]
                excluir.write(''.join(lista_nova))
                if 0 < linha_remover <= len(linhas):
                    print("\nLinha excluída com sucesso!")
        
        elif tipo == 2:
            with open('registros.txt', 'r') as excluir:
                linhas = excluir.readlines()
            
            with open('registros.txt', 'w') as excluir:
                del linhas
            
            print("\nRegistro excluído com sucesso!")
        
        else: 
            print("\nO tipo de exclusão escolhido é inválido. Por favor, tente novamente.")
            print()
        
        escolha = input("\nDeseja realizar mais alguma ação?\nResponda com \"Sim\" ou \"Não\": ")
        
        if escolha == "sim" or escolha == "Sim":
            print()
            continue
        else:
            break
    
    # elif ac == 5:

    else: 
        print("\nA ação escolhida é inválida. Por favor, tente novamente.")
        print()