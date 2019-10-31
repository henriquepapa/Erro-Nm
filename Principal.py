import glob
import os
#import ACR
#import wikipedia
import pre_processamento
#import parentese
import Nm
#import re

def main ():

	# Debug
	#import ipdb; ipdb.set_trace()
	# direto de textos
	os.chdir('C:\\Users\\henri\\OneDrive\\Documentos\\GitHub\\Erro-Nm\\Textos')

	file = open('NM_Teste.txt', 'r')  # textos as serem analisados

	arquivos = file.read().split('\n')
	file.close()

	lista_arq = []
	quantidade = 0

	arquivos = ['C22_erro_sumarizador2.txt']
	for arq in arquivos:
	#arq = 'C14_erro_sumarizador2.txt'
	#if 1==1:
		
		print(arq) 

		print('\n\n')

		texto, dicionario = pre_processamento.pre_Processamento(arq)
		frases = pre_processamento.Remove_stop_pu(texto)
		#lista_prop = Nm.Buscafrases(frases,dicionario)
		
		Nm.similaridade(frases,'NM',texto)

		


		
'''
		dicionario_valor = ';'.join(list (dicionario.values()))
		print(dicionario_valor)
		print('\n\n')

		dicionario_keys = ';'.join(list (dicionario.keys()))
		print(dicionario_keys)

		print('\n\n')

		print(dicionario)
		

		#match = re.findall('[(][\w,\s]+[)]', dicionario_valor)





		lista=((teste.verifica_Parenteses(texto)))

		valor = valor + len(lista)

		print(lista)

	#quantidade_ACR,siglas = ACR.funcao_ACR(texto)

	#print ('foram encotradas : '+str(quantidade_ACR)+ ' siglas')

	# for i in siglas :
	# print(i)
	#texto_palavaras = map(texto.remove('\n'),texto)

	#texto_palavras = pre_processamento.preparaTexto(texto)

	
		#print('\n\n')

		#print(dicionario)





	#print(texto_palavras)

	#print(pre_processamento.sincroniza_Palavras(texto_palavras, (list(dicionario))))

	#------------ variavel globais para ACR-----------------------------------

'''
#-------------------------------------------------------------------------

main()
