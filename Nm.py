import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
import spacy
import warnings
import nltk
warnings.filterwarnings("ignore")

# carregue o modelo
nlp = spacy.load('pt')

def erros_NM(frase,listaPossiveis):
	erros =[]
	frase_np = nlp(frase)
	lista_entidades = frase_np.ents
	errosx = []
	for entidades in lista_entidades:
		for possivel in listaPossiveis:
			porcentagem=fuzz.partial_ratio(str(entidades),str(possivel))
			if porcentagem>=80 and  possivel not in errosx:
				errosx.append(str(possivel))

	for i in errosx:
		lista_token=(nltk.word_tokenize(i))
		if len(lista_token) > 1:
			possivel_erro = frase[(frase.index(lista_token[0])):(frase.index(lista_token[(len(lista_token)-1)]) + len(lista_token[(len(lista_token)-1)]))]
			if ',' in possivel_erro or '(' in possivel_erro :
				if '(' in possivel_erro and ')' not in  possivel_erro :
					possivel_erro = possivel_erro + ')'
				erros.append(possivel_erro)
	return erros

def minera_Erros(lista):
	erros =[]
	for i in lista:
		doc= nlp(i)
		for entity in doc.ents:
			erros.append(str(i))
	return erros

def listaPossiveis(lista):
	saida = []
	temporario = ''
	lista_possiveis_x= []
	lista_possiveis = []
	for i in lista:
		if i != '_':
			if temporario != '':
				temporario = temporario + ' ' + i
			else:
				temporario = i
		else:
			if temporario != '':
				lista_possiveis_x.append(temporario)
				temporario = ''
	if temporario != '':
		lista_possiveis_x.append(temporario)
	for termos in lista_possiveis_x:
		if len(nltk.word_tokenize(termos)) > 1:
			lista_possiveis.append(termos)
	return minera_Erros(lista_possiveis)
	

	
	

def redundancias (frases1,frases2):
	palavras = frases1
	palavras2 = frases2


	# insira o input sempre em unicode                
	dados=[]
	for palavra1 in palavras:
	    for palavra2 in palavras2:
	        dados.append(palavra1.similarity(palavra2))    # aqui eu testo a similaridade

	# organização dos dados
	dados = np.asarray(dados).reshape(len(palavras),len(palavras2))
	rotulo1 = [str(palavra) for palavra in palavras]
	rotulo2 = [str(palavra) for palavra in palavras2]
	dados = pd.DataFrame(dados,rotulo1,rotulo2)
	similares=[]
	for palavra1 in palavras:
		trava = ''
		for palavra2 in palavras2:
			if str(palavra2) != '':
				if str(dados.loc[(str(palavra1)),(str(palavra2))] >= 0.8)== 'True':
		    		#print (str(palavra1) + ' : '+ str(palavra2))
					similares.append(str (palavra2))
					trava = 'Y'
		if trava != 'Y':
			similares.append('_')
	return (listaPossiveis(similares))


def similaridade(frases,indicador,texto):
	sentenca = ''
	erro_sent= []
	for indice,sent in enumerate(frases):
		indices = []
		sentenca =  (' '.join(sent))
		for i,ax in enumerate(frases[(indice+1):(len(frases))]):
			restante =  (' '.join(ax))
			indice2 = indice +2 + i
			similares = redundancias(nlp(sentenca),nlp(restante))
			lista_erros = erros_NM (texto[(indice2-1)],similares)
			for i in lista_erros:
				print('Sentenças S['+ str(indice2)+'] redundate com', end="")
				print('  ['+str((indice+1))+'] '+ 'Termo:'+i, end="")
				print('\n\n')