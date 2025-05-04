import os 
os.system ("cls")

Metas = []

def calcular_dias(dia_atual, mes_atual, ano_atual, dia_final, mes_final, ano_final):

    dias_ano_atual = ano_atual * 365 + mes_atual * 30 + dia_atual
    dias_ano_final = ano_final * 365 + mes_final * 30 + dia_final

    
    return dias_ano_final - dias_ano_atual


while True:



    ac = int(input("Selecione, escrevendo o número indicado, que tipo de ação deseja realizar:\n1 - Visualizar metas\n2 - Adicionar metas\n3 - Editar metas\n4 - Excluir metas\n\nDigite aqui a ação selecionada: "))


    if ac == 1:
        with open('metas.txt', 'r') as visualizar:
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
        with open('metas.txt', 'a') as adicionar:
            dia_atual = int(input("\nDigite o dia do início da meta: "))
            mes_atual = int(input("\nDigite o mês do início da meta: "))
            ano_atual = int(input("\nDigite o ano atual: "))
            dia_final = int(input("\nDigite o dia do fim da meta: "))
            mes_final = int(input("\nDigite o mês final: "))
            ano_final = int(input("\nDigite o ano final: "))
            dias_restantes = calcular_dias(dia_atual, mes_atual, ano_atual, dia_final, mes_final, ano_final)
            print(f"Faltam {dias_restantes} dias para a meta ser concluída.")

            tipo = input("\nDigite o tipo de meta (Emagracimento; Ganho de massa muscular; Bater pr; Condicionamento; Habilidade): ")
            adicione = input("\nDigite seu pr,peso,habilidade,condicionamento ou massa muscular atual: ")
            Metas.append (input("\nDigite as metas que desja realizar: "))
            adicionar.write(f"{dia_atual}/{mes_atual}/{ano_atual}, {dia_final}/{mes_final}/{ano_final}, {tipo}, {adicione}, {Metas}, Duracao da meta {dias_restantes} dias\n")
        
        Metas.clear()
        
        print("\nMetas adicionada com sucesso!")
        
        escolha = input("\nDeseja realizar mais alguma ação?\nResponda com \"Sim\" ou \"Não\": ")

        if escolha == "sim" or escolha == "Sim":
            print()
            continue
        else:
            break
        
    elif ac == 3:
        print()
        lista_nova = []
        
        with open('metas.txt', 'r') as editar:
            linhas = editar.readlines()
            
            for i in range(len(linhas)):
                print(f"{i + 1} - {linhas[i]}")
            
            linha_remover = int(input("\nDigite o número da linha que deseja editar: "))
            if linha_remover <= 0 or linha_remover > len(linhas):
                print("\nA linha informada não existe. Por favor, tente novamente.")
            else:
               dia_atual = int(input("\nDigite o dia do início da meta: "))
               mes_atual = int(input("\nDigite o mês do início da meta: "))
               ano_atual = int(input("\nDigite o ano atual: "))
               dia_final = int(input("\nDigite o dia do fim da meta: "))
               mes_final = int(input("\nDigite o mês final: "))
               ano_final = int(input("\nDigite o ano final: "))
               dias_restantes = calcular_dias(dia_atual, mes_atual, ano_atual, dia_final, mes_final, ano_final)
               print(f"Faltam {dias_restantes} dias para a meta ser concluída.")

               tipo = input("\nDigite o tipo de meta (Emagracimento; Ganho de massa muscular; Bater pr; Condicionamento; Habilidade): ")
               adicione = input("\nDigite seu pr,peso,habilidade,condicionamento ou massa muscular atual: ")
               Metas.append (input("\nDigite as metas que deseja realizar: "))
               lista_nova.append(f"{dia_atual}/{mes_atual}/{ano_atual}, {dia_final}/{mes_final}/{ano_final}, {tipo}, {adicione}, {Metas}, Duracao da meta {dias_restantes} dias\n")
        with open('metas.txt', 'w') as editar:
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
            with open('metas.txt', 'r') as excluir:
                linhas = excluir.readlines()

                for i in range(len(linhas)):
                    print(f"{i + 1} - {linhas[i]}")

                linha_remover = int(input("\nDigite o número da linha que deseja remover: "))

                if linha_remover <= 0 or linha_remover > len(linhas):
                    print("\nA linha informada não existe. Por favor, tente novamente.")
            with open('metas.txt', 'w') as excluir:
                lista_nova =  linhas[:linha_remover - 1] + linhas[linha_remover:]
                excluir.write(''.join(lista_nova))
                if 0 < linha_remover <= len(linhas):
                    print("\nLinha excluída com sucesso!")
        
        elif tipo == 2:
            with open('metas.txt', 'r') as excluir:
                linhas = excluir.readlines()
            
            with open('metas.txt', 'w') as excluir:
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

    else: 
        print("\nA ação escolhida é inválida. Por favor, tente novamente.")
        print()