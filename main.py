#Menu Principal
menuPrincipla = {
    "1": " Nossos Contatos",
    "2": " Dúvidas Frequentes ",
    "3": " Projetos",
    "4": " Sair?",
}

# Base de dados para cada opção

#menu da opção 1 (Nossos Contatos)
opcao1 = {
    "1": "1. E-mail",
    "2": "2. Telefone ",
    "3": "3. instagram",
    "4": "4. Sair",
}

opcao2 = {
    "1": "1. Frequência e formato da aula ",
    "2": "2. Requisitos para fazer o curso (Análise de Dados) ",
    "3": "3. Qual a linguagem de programação abordada ?  ",
    "4": "4. Sair",
}

opcao3 = {
    "1": "1. Projeto chatbot ",
    "2": "2. Projeto Banco de Dados",
    "3": "3. Projeto análise e fluxo de caixa",
    "4": "4. Sair",
}

# função para mostrar as opções de atendimento e capturar a escolha do usuário
def escolher_opcao():
    print("Para atendimento por favor digite o número correspondente e clique Enter:")
    for selecione, pergunta in menuPrincipla.items():
        print(f"{selecione}. {pergunta}")
    escolha = int(input("Opcao escolhida : "))
    if escolha == 4:
        exit()
    return escolha


# função para mostrar as perguntas e respostas correspondentes à opção escolhida
def mostrar_perguntas_respostas(escolha):
    while True:
        print("1. E-mail\n2. Telefone\n3. instagram\n4. Sair")
        escolha2 = int(input('Digite o número referente a escolha: '))
        if escolha2 == 1:
            print('E-mail = resilia.edu@gmail.com')  
            break
        if escolha2 == 2:
            print('Telefone = (21)98544-2514')
            break
        elif escolha2 == 3:
            print('Instagram = ResiliaEdu')
            break
        elif escolha2 == 4:
            break
def mostrar_perguntas_respostas(escolha):
    while True:
        print("1. Frequência e formato da aula\n2. Requisitos para fazer o curso(Análise de Dados)\n3. Qual a linguagem de programação abordada ?\n4. Sair")
        escolha3 = int(input('Digite o número referente a escolha: '))
        if escolha3 == 1:
            print("As aulas são todas online pela plataforma zoom e a frequência mínima para aprovação é 85%")  
            break
        if escolha3 == 2:
            print("Idade Mínima 18 anos, um computador com acesso a internet e ensino médio completo")
            break
        elif escolha3 == 3:
            print("A linguagem de programação que estudamos é Python")
            break
        elif escolha3 == 4:
            break
def mostrar_perguntas_respostas(escolha):
    while True:
        print("1. Projeto chatbot\n2. Projeto Banco de Dados\n3. Projeto análise e fluxo de caixa\n4. Sair",)
        escolha4 = int(input('Digite o número referente a escolha: '))
        if escolha4 == 1:
            print("www.resilia.com/projeto_chatboot")  
            break
        if escolha4 == 2:
            print( "www.resilia.com/projeto_banco_de_dados")
            break
        elif escolha4 == 3:
            print("www.resilia.com/analise_de_fluxo")
            break
        elif escolha4 == 4:
            break




# loop principal do bot
while True:
    selecione = escolher_opcao()
    mostrar_perguntas_respostas(selecione)
    reiniciar = input("Deseja reiniciar este atendimento? (s/n) ")
    if reiniciar.lower() != "s":
        break