import re 
from fuzzywuzzy import process 
from fuzzywuzzy import fuzz 

def separaSigla(tupla):
	match = re.findall('[(][\w,\s]+[)]', tupla[0])
	if tupla [1] == 1:
		sigla= match[0].replace('(', '')
		sigla= sigla.replace(')', '')
		if ' ' in sigla:
			sigla = sigla.replace(' ','')
		explicacao = tupla[0].replace(match[0], '')

	else:
		explicacao= match[0].replace('(', '')
		explicacao= explicacao.replace(')', '')
		sigla = tupla[0].replace(match[0], '')
		if ' ' in sigla:
			sigla = sigla.replace(' ','')

	if explicacao[len(explicacao)-1] == ' ':
		explicacao = explicacao[0:(len(explicacao)-1)]

	
	return sigla,explicacao

def VerificaLista(texto, Lista_de_parenteses):
	erros = []
	for siglas in Lista_de_parenteses:
	 	trecho = ''
	 	for i,linha in enumerate(texto):
	 		if i < siglas[2]:
	 			trecho = trecho + linha
	 	si, ex = separaSigla(siglas)
	 	if (si in trecho) or (ex.lower() in trecho) or (ex in trecho):
	 		erros.append((siglas[0],siglas[2]+1))

	return erros


def obtemExplicacao(texto,lista_de_parenteses,semelha, explicaAntes_acr ,explicaDepois_acr):
	
	erros= []
	erros_ax = []
	lista = []
	auxiliar = semelha
	semelhantes = []

	for erro in VerificaLista(texto,lista_de_parenteses):
		erros.append(erro)
	for i in semelha:
		semelhantes.append(i[0])


	for parenteses in lista_de_parenteses :
		if semelhantes != []:
			lista = (process.extract( parenteses[0],semelhantes, scorer= fuzz.ratio))

		for cont,i in enumerate (lista) : 
			if i[1] < 80:
				lista.remove(i)

		for i in lista:
			erros_ax.append(i[0])

		for erro in erros_ax:
			for i in auxiliar  :
				if erro == i[0] and (not (erro,(i[1]+1)) in erros ):
					erros.append((erro,(i[1] + 1)))
	return erros

'''
		lista_sem_indices=[]

		for exp in explicaAntes_acr:
			lista_sem_indices.append(exp[0])
		
	for i in explicaDepois_acr :
		if lista_sem_indices != []:
			lista = (process.extract( i[0],lista_sem_indices, scorer= fuzz.ratio))
			for erros_possiveis in lista:
				if erros_possiveis[1]> 80:
					if i [1] >= erros_possiveis[1]:
						erros.append(i[0])
					else:
						erros.append(erros_possiveis[0])
'''




def verifica_Parenteses(texto):

	frases =[]

	for senteca in texto:
		frases.append(senteca.split(' '))#tokeniza o texto
	
	lista_de_parenteses = [] 
	eliminacao = []
	semelhantes = []
	explicaAntes_acr= []
	explicaDepois_acr = []

	for indices,linhas in enumerate(frases):
		match = (re.findall('[(][\w,\s]+[)]', (' '.join(linhas))) ) # busca palavras entre parentese como (Palavra)
		
		if len (match) != 0:
			
			for achados in match:
				
				if achados.islower():
					break;
				if (not(' ' in achados)):

						explicacao_Depois = re.findall('\s'+achados[1]+'[\w,\s]*[(]\w+[)]', (' '.join(linhas)))
						#explica = (str(explicacao_Antes)).split("'")
						if explicacao_Depois != []:
                             
                            
							if explicacao_Depois[0][0] == ' ':

								aux = explicacao_Depois[0].replace(' ','',1)

								if not (achados in eliminacao) :

									eliminacao.append(achados)
									lista_de_parenteses.append((aux, 1, indices ))
									if not ((aux, indices ) in explicaDepois_acr ):
										explicaDepois_acr.append((aux, indices ))
								else:
									semelhantes.append((explicacao_Depois[0], indices))
							
							elif not (achados in eliminacao):

								eliminacao.append(achados)
								lista_de_parenteses.append((explicacao_Depois[0], 1, indices ))

				elif  (' ' in achados):
						explicacao_Antes = re.findall( '\s'+achados[1]+'[\w,\s]+'+'[(][\w,\s]+[)]', (' '.join(linhas)))
						#explica = (str(explicacao_Antes)).split("'")
						if explicacao_Antes != []:
							if explicacao_Antes[0][0] == ' ':

								aux = explicacao_Antes[0].replace(' ','',1)

								if not (achados in eliminacao):

									eliminacao.append(achados)
									lista_de_parenteses.append((aux, -1, indices ))

									if not ((aux, indices ) in explicaAntes_acr ):
										explicaAntes_acr.append((aux, indices ))
								else:
									semelhantes.append((explicacao_Antes[0],indices))

							elif not (achados in eliminacao):
								eliminacao.append(achados)

								lista_de_parenteses.append((explicacao_Antes[0], -1, indices ))
				else:
					pass
	return (obtemExplicacao(texto,lista_de_parenteses,semelhantes, explicaAntes_acr ,explicaDepois_acr))
