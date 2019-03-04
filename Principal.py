import glob,os
import ler_XML
from nltk.tokenize import word_tokenize,sent_tokenize
import pre_processamento

def main():
	
	os.chdir('C:\\Users\\henri\\OneDrive\\Documentos\\GitHub\\Erro-Nm\\Textos')

	file = open('treino.txt','r')

	arquivos = file.read().split('\n')

	file.close()

	for arq in arquivos:
		linhas, discionario = pre_processamento.pre_Processamento(arq)
		print (linhas[0])
		print (discionario)

main()