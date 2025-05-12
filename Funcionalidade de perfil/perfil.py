import os 
os.system ("cls")

try:
    with open('perfil.txt', 'r') as verificação:
        verificação.close()
except FileNotFoundError:
    with open('perfil.txt', 'x') as criar:
        criar.close()

def sem_numeros(mensagem):
    while True:
        entrada = input(mensagem)
        if all(char.isalpha() or char.isspace() for char in entrada):
            if entrada.strip():
                return entrada
            else:
                raise ValueError
        else:
            raise ValueError


def criar_perfil():
    while True:
        try:
            while True:
                nome = sem_numeros("\nDigite o seu nome: ")
                sobrenome = sem_numeros("\nDigite o seu sobrenome: ")
                perfil_existe = verificar_perfil_existe(nome.strip(), sobrenome.strip())
                
                if perfil_existe:
                    print("\nEsse perfil já existe. Por favor, tente um novo nome e/ou sobrenome.")
                else:
                    break
            altura = float(input("\nDigite a sua altura (em Cm): "))
            peso = float(input("\nDigite o seu peso (em Kg): "))
            sexo = sem_numeros("\nDigite o seu sexo: ")
            
            print("\nPerfil criado com sucesso!")
            break
        except ValueError:
            print("\nValor inválido. Por favor, tente novamente.")

    with open('perfil.txt', 'a') as arquivo:
        arquivo.write(f"{nome.strip()},{sobrenome.strip()},{altura},{peso},{sexo}\n")

def ler_perfis(nome, sobrenome):
    nome_lower = nome.lower()
    sobrenome_lower = sobrenome.lower()
    
    with open('perfil.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_procurada = linha.strip().lower()
        if nome_lower in linha_procurada and sobrenome_lower in linha_procurada:
            nome, sobrenome, altura, peso, sexo = linha.strip().split(',')
            print(f"\nNome: {nome} {sobrenome}\nAltura: {altura} Cm\nPeso: {peso} Kg\nGênero: {sexo}")

def verificar_perfil_existe(nome, sobrenome):
    nome_lower = nome.lower()
    sobrenome_lower = sobrenome.lower()
    
    with open('perfil.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_procurada = linha.strip().lower()
            if nome_lower in linha_procurada and sobrenome_lower in linha_procurada:
                return True
    return False

def editar_perfil(nome, sobrenome):
    nome_lower = nome.lower()
    sobrenome_lower = sobrenome.lower()
    perfis_atual = []
    perfis_novo = []
    perfil_encontrado = False
    
    with open('perfil.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_procurada = linha.strip().lower()
        if nome_lower in linha_procurada and sobrenome_lower in linha_procurada:
            perfis_atual.append(linha)
            perfis_atual_str = ' '.join(perfis_atual)
            perfis_atual_separado = perfis_atual_str.strip().split(',')
            
            perfil_encontrado = True
            altura_atual =  perfis_atual_separado[2]
            peso_atual = perfis_atual_separado[3]
            sexo_atual = perfis_atual_separado[4]

            while True:
                try:
                    novo_nome = sem_numeros(f"\nNovo nome (atual: {nome}): ") or nome
                    novo_sobrenome = sem_numeros(f"\nNovo sobrenome (atual: {sobrenome}): ") or sobrenome
                    nova_altura = float(input(f"\nNova altura (em Cm) (atual: {altura_atual}): ") or altura_atual)
                    novo_peso = float(input(f"\nNovo peso (em Kg) (atual: {peso_atual}): ") or peso_atual)
                    novo_sexo = sem_numeros(f"\nNovo sexo (atual: {sexo_atual}): ") or sexo_atual
                    perfis_novo.append(f"{novo_nome.strip()},{novo_sobrenome.strip()},{nova_altura},{novo_peso},{novo_sexo}\n")
                    break
                except ValueError:
                    print("\nValor inválido. Por favor, tente novamente.")
        else:
            perfis_novo.append(linha)
    if perfil_encontrado:
        with open('perfil.txt', 'w') as arquivo:
            arquivo.writelines(perfis_novo)
            print("\nPerfil atualizado com sucesso!")
    else:
        print(f"\nPerfil com nome '{nome}' e sobrenome '{sobrenome}' não encontrado.")
    
    perfis_atual.clear()
    perfis_novo.clear()

def excluir_perfil(nome_busca, sobrenome_busca):
    nome_lower = nome_busca.strip().lower()
    sobrenome_lower = sobrenome_busca.strip().lower()
    linha_remover = None

    with open('perfil.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas, start=1):
        linha_procurada = linha.strip().lower()
        if nome_lower in linha_procurada and sobrenome_lower in linha_procurada:
            linha_remover = i
            break

    if linha_remover is None:
        print("\nPerfil não encontrado.")
        return

    with open('perfil.txt', 'w') as excluir:
        lista_nova = linhas[:linha_remover - 1] + linhas[linha_remover:]
        excluir.write(''.join(lista_nova))

    print(f"\nPerfil excluído com sucesso!")

def abrir_perfil():
    nome = input("Informe o seu primeiro nome aqui: ")
    sobrenome = input("\nInforme o seu sobrenome: ")
    while True:
        try:
            perfil = verificar_perfil_existe(nome.strip(), sobrenome.strip())
    
            if perfil:
                ler_perfis(nome.strip(), sobrenome.strip())
        
            else:
                print("\nPerfil não encontrado. Iniciando a criação de um novo perfil.")
                criar_perfil()
                break
        
            try:
                opcao = int(input("\nSelecione, escrevendo o número indicado, que tipo de ação deseja realizar:\n\n1 - Editar Perfil\n2 - Excluir perfil\n3 - Sair da aba de perfil\n\nDigite aqui a ação selecionada: "))

                if opcao == 1:
                    editar_perfil(nome.strip(), sobrenome.strip())
                    ler_perfis(nome.strip(), sobrenome.strip())
                    print()
                    break
                elif opcao == 2:
                    excluir_perfil(nome.strip(), sobrenome.strip())
                    print()
                    break
                elif opcao == 3:
                    print("\nSaindo da aba de perfil\n")
                    break
                else: 
                    print("\nOpção inválida. Por favor, tente novamente")
            except ValueError:
                print("\nOpção inválida. Por favor, tente novamente")
        except UnboundLocalError:
            print("\nPerfil não encontrado. Iniciando a criação de um novo perfil.")
            criar_perfil()
            break

abrir_perfil()