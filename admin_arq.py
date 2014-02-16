#-*- coding:utf-8 -*-
#asdasdadsdasdasdasd
#CRIA ARQUIVO
'''cria = open('arquivo.txt','w')

for linha in range(1,11):
	cria.write('Linha nÃºmero: %i\n' %linha)
cria.close()'''

#LER ARQUIVO
'''arq = open('arquivo.txt','r')
for i in arq.readlines():
	print (i.rstrip())
arq.close()'''

#FORMA PYTHôNICA
'''with open('arquivo.txt') as f:
	print (f.read())'''

def menu():
	print ('O que deseja: \n')

	for i,k in enumerate(['Criar Arquivo','Editar','Visualizar','Remover'],start=1):
		print ('%d - %s' %(i,k))
	opc = ''

	while True:
		opc = str(input('\nOPÇÃO: '))
		if opc == '1':#CASO DE CRIAR ARQUIVO
			arq = str(input('Nome do Arquivo: '))
			criar(arq)

		elif opc == '2': #CASO DE EDITAR ARQUIVO
			arq = str(input('Nome do Arquivo: '))
			editar(arq)

		elif opc == '3': #CASO DE VISUALIZAR O ARQUIVO
			arq = str(input('Nome do Arquivo: '))
			visualizar(arq)

		elif opc == '4': #CASO DE APAGAR O ARQUIVO
			arq = str(input('Nome do Arquivo: '))
			apagar(arq)

		elif opc not in ['1','2','3','sair']:
			print ('Opção Inválida')

		elif opc == 'sair':
			exit()

def verifica(arq):
	try:
		arquivo = open(arq)
		arquivo.close()
		return True
	except:
		return False
		
def criar(arq):
	arquivo = open(arq,'w')
	print ('Criado com sucesso')
	arquivo.close()

def editar(arq):
	if not verifica(arq):
		print ('Primeiro crie o arquivo ')
	else:
		texto = str(input('Digite o texto: '))
		with open(arq,'a') as arquivo:	
			import os
			if os.path.getsize(arq) != 0:
				arquivo.write('\n'+texto)
				print ('Inserido com sucesso')
				arquivo.close()
			else:
				arquivo.write(texto)
				print ('Inserido com sucesso')
				arquivo.close()
				

def apagar(arq):
	if not verifica(arq):
		print ('Primeiro crie o arquivo ')
	else:
		import os
		if arq not in os.listdir(path='.'):
			print ('Arquivo não encontrado')
		else:
			os.remove(arq)
			print ('Removido com sucesso.')

def visualizar(arq):
	if not verifica(arq):
		print ('Primeiro crie o arquivo ')
	else:
		with open(arq,'r') as arquivo:
			for i in arquivo.readlines():
				print (i.rstrip())
			arquivo.close()
	
#CHAMANDO AS FUNÇÕES
menu()








