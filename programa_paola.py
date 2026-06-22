#TRABALHO FINAL - ALGORÍTMOS E PROGRAMAÇÃO 2026.1 
#Discente: Paola Weber Turma:02.

#SISTEMA DE CONTROLE DE BIBLIOTECAS COM A STRUCT: CLASS

class Livro:   #aqui vou deixar os dados necessários p/livros.
	
	titulo=''
	autor=''
	ano=0
	codigo=''
	status=''
	
#aqui vou listar as funções necessárias e as solicitadas para o trabalho.
#não vou comentar todas pois já algumas já estão com nome auto explicativo.

	
def criar_Livro(titulo, autor, ano, codigo, status):
	livro=Livro()
	livro.titulo=titulo
	livro.autor=autor
	livro.ano=ano 
	livro.codigo=codigo
	livro.status=status
	return livro
	
def buscar_pelo_codigo(biblioteca,codigo):
	for i in range(len(biblioteca)):
		if biblioteca[i].codigo==codigo:
			return i
	return -1   #retorna o indice (-1) se não encontrar o indice na linha acima
	
def exibir_livro(livro):
	print("Codigo  : " + livro.codigo)
    print("Titulo  : " + livro.titulo)
    print("Autor   : " + livro.autor)
    print("Ano     : " + str(livro.ano))
    print("Status  : " + livro.status)
    print("----------------------------")
    
    
	
	
	
	
	
	
	




