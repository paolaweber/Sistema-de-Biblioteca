#TRABALHO FINAL - ALGORÍTMOS E PROGRAMAÇÃO 2026.1
#Discente: Paola Weber Turma:02.

#SISTEMA DE CONTROLE DE BIBLIOTECAS COM A STRUCT: CLASS

class Livro:  #aqui vou deixar os dados necessários p/livros.

    titulo = ''
    autor = ''
    ano = 0
    codigo = ''
    status = ''

#aqui vou listar as funções necessárias e as solicitadas para o trabalho.
#não vou comentar todas pois algumas já estão com nome auto explicativo.


def criar_Livro(titulo, autor, ano, codigo, status):
    livro = Livro()
    livro.titulo = titulo
    livro.autor = autor
    livro.ano = ano
    livro.codigo = codigo
    livro.status = status
    return livro

def buscar_pelo_codigo(biblioteca, codigo):
    for i in range(len(biblioteca)):
        if biblioteca[i].codigo == codigo:
            return i
    return -1  #retorna -1 se não encontrar

def exibir_livro(livro):
    print("Codigo  : " + livro.codigo)
    print("Titulo  : " + livro.titulo)
    print("Autor   : " + livro.autor)
    print("Ano     : " + str(livro.ano))
    print("Status  : " + livro.status)
    print("----------------------------")

def ordenar_por_titulo(biblioteca):
    for i in range(1, len(biblioteca)):
        chave = biblioteca[i]
        j = i - 1
        while j >= 0 and biblioteca[j].titulo.lower() > chave.titulo.lower():  #lower() deixa tudo minúsculo para comparar sem diferenciar maiúsculas de minúsculas
            biblioteca[j + 1] = biblioteca[j]
            j -= 1
        biblioteca[j + 1] = chave
    return biblioteca


#aqui vou criar "def's" para listar as funcionalidades do menu.


def cadastrar_livro(biblioteca):
    print('=== Cadastrar Livro ===')
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    ano = int(input('Digite o ano do livro: '))
    codigo = input('Digite o código do livro: ')

    if buscar_pelo_codigo(biblioteca, codigo) != -1:
        print('Já existe um livro com esse código!')
        return biblioteca

    livro = criar_Livro(titulo, autor, ano, codigo, 'disponivel')
    biblioteca.append(livro)
    biblioteca = ordenar_por_titulo(biblioteca)
    print('Livro cadastrado!')
    return biblioteca

def consultar_livro(biblioteca):
    print('=== Consultar Livro ===')
    print('1- Por codigo')
    print('2- Por autor')
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        codigo = input('Digite o código do livro: ')
        indice = buscar_pelo_codigo(biblioteca, codigo)
        if indice == -1:
            print('Livro não encontrado.')
            return
        exibir_livro(biblioteca[indice])
        return

    if opcao == '2':
        autor = input('Digite o nome do autor do livro: ')
        encontrou = False
        for livro in biblioteca:
            if livro.autor.lower() == autor.lower():
                exibir_livro(livro)
                encontrou = True
        if not encontrou:
            print('Livro não foi encontrado.')
        return

    print('Opção inválida.')

def alterar_dados(biblioteca):
    print('=== Alterar Dados ===')
    codigo = input('Digite o código do livro: ')
    indice = buscar_pelo_codigo(biblioteca, codigo)

    if indice == -1:
        print('Livro não encontrado!')
        return biblioteca

    print('O que você gostaria de alterar?')
    print('1 - Titulo')
    print('2 - Autor')
    print('3 - Ano')
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        biblioteca[indice].titulo = input('Digite o novo titulo: ')
        biblioteca = ordenar_por_titulo(biblioteca)
        print('Titulo alterado!')
        return biblioteca

    if opcao == '2':
        biblioteca[indice].autor = input('Digite o novo autor: ')
        print('Autor alterado!')
        return biblioteca

    if opcao == '3':
        biblioteca[indice].ano = int(input('Digite o novo ano: '))
        print('Ano alterado!')
        return biblioteca

    print('Opção inválida.')
    return biblioteca

def remover_livro(biblioteca):  #remove livro pelo código
    print('=== Remover Livro ===')
    codigo = input('Digite o código do livro a remover: ')
    indice = buscar_pelo_codigo(biblioteca, codigo)  

    if indice == -1:
        print('Este livro não foi encontrado!')
        return biblioteca

    biblioteca.pop(indice)  #.pop remove e retorna o elemento do índice informado
    print('Livro removido!')
    return biblioteca

def listar_todos(biblioteca):
    print('=== Lista de livros ===')

    if len(biblioteca) == 0:
        print('Nenhum livro foi cadastrado.')
        return

    for livro in biblioteca:
        print(livro.titulo + " (" + str(livro.ano) + ")")

def realizar_emprestimo(biblioteca):
    print('=== Realizar Empréstimo ===')
    codigo = input('Digite o código do livro escolhido: ')
    indice = buscar_pelo_codigo(biblioteca, codigo)

    if indice == -1:
        print('Livro não encontrado.')
        return biblioteca

    if biblioteca[indice].status == 'emprestado':
        print('Livro já está com empréstimo constando no sistema.')
        return biblioteca

    biblioteca[indice].status = 'emprestado'
    print('Empréstimo efetuado!')
    return biblioteca

def realizar_devolucao(biblioteca):
    print('=== Realizar Devolução ===')
    codigo = input('Digite o código do livro: ')
    indice = buscar_pelo_codigo(biblioteca, codigo)

    if indice == -1:
        print('Livro não encontrado!')
        return biblioteca

    biblioteca[indice].status = 'disponivel'
    print('Devolução concluída!')
    return biblioteca

def exibir_menu():  #menu, primeira opção que irá aparecer para o usuário.
    print('============================')
    print(' Sistema de Biblioteca')
    print('============================')
    print('1- Cadastrar livro')
    print('2- Consultar livro')
    print('3- Alterar dados')
    print('4- Remover livro')
    print('5- Listar todos')
    print('6- Realizar emprestimo')
    print('7- Realizar devolucao')
    print('8- Sair')
    print('============================')


#agora vou criar a def principal, ela controla como o programa vai ser executado.


def main():

    biblioteca = []
    rodando = True

    while rodando:
        exibir_menu()
        opcao = input('Escolha a opcao desejada: ')

        if opcao == '1':
            biblioteca = cadastrar_livro(biblioteca)

        if opcao == '2':
            consultar_livro(biblioteca)

        if opcao == '3':
            biblioteca = alterar_dados(biblioteca)

        if opcao == '4':
            biblioteca = remover_livro(biblioteca)

        if opcao == '5':
            listar_todos(biblioteca)

        if opcao == '6':
            biblioteca = realizar_emprestimo(biblioteca)

        if opcao == '7':
            biblioteca = realizar_devolucao(biblioteca)

        if opcao == '8':
            print("Encerrando o sistema.")
            rodando = False


# Ponto de entrada do programa
main()
