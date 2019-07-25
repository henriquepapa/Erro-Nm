import glob
import os
import ACR
import wikipedia
import pre_processamento
import parentese
import nomes
import re
def main ():
    # direto de textos
    os.chdir('C:\\Users\\henri\\OneDrive\\Documentos\\GitHub\\Erro-Nm\\Textos')

    file = open('treino.txt', 'r')  # textos as serem analisados

    arquivos = file.read().split('\n')

    file.close()

    #for arq in arquivos:
    arq = 'C11_erro_sumarizador1.txt'
    if 1==1:
        print(arq)

        print('\n\n')

        texto, dicionario = pre_processamento.pre_Processamento(arq)
        
        dicionario_valor = ';'.join(list (dicionario.values()))
        print(dicionario_valor)
        print('\n\n')

        dicionario_keys = ';'.join(list (dicionario.keys()))
        print(dicionario_keys)

        print('\n\n')

        print(dicionario)

        #match = re.findall('[(][\w,\s]+[)]', dicionario_valor)




'''
        lista=((teste.verifica_Parenteses(texto)))

        valor = valor + len(lista)

        print(lista)
'''
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
