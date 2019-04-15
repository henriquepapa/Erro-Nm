import glob
import os
import ACR
from nltk.tokenize import word_tokenize, sent_tokenize
import pre_processamento
import wikipedia
import nltk
import teste

def main():

    # direto de textos
    os.chdir('C:\\Users\\henri\\OneDrive\\Documentos\\GitHub\\Erro-Nm\\Textos')

    file = open('treino.txt', 'r')  # textos as serem analisados

    arquivos = file.read().split('\n')

    file.close()
    valor =0

    for arq in arquivos:

        print(arq)

    	#print('\n\n')

        texto, dicionario = pre_processamento.pre_Processamento(arq)

        lista=((teste.verifica_Parenteses(texto)))

        valor = valor + len(lista)

        print(lista)

    print(valor)

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


#-------------------------------------------------------------------------

main()
