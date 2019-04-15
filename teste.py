import re 
from fuzzywuzzy import process 
from fuzzywuzzy import fuzz 


def obtemExplicacao(texto,lista_de_parenteses,semelhantes):
	
	frases = []
	erros= []
	lista = []
	auxiliar = []


	for linhas in texto:
		frases.append((' '.join(linhas)))

	for parenteses in lista_de_parenteses :
		auxiliar.append(parenteses[0])
		if semelhantes != []:
			lista = (process.extract( parenteses[0],semelhantes, scorer= fuzz.ratio))

		for i in lista : 
			if i[1] < 80:
				lista.remove(i)

		for i in lista:
			erros.append(i[0])
	return erros
'''
		for i in lista_de_parenteses:
			if len(auxiliar) == 1:
				break
			else: 
				x= auxiliar [0]
				auxiliar.remove(auxiliar[0])

			lista = (process.extract( x,auxiliar, scorer= fuzz.ratio))

			
			for i in lista : 
				if i[1] > 50:
					erros.append(i[0])
'''	

def verifica_Parenteses(texto):

	frases =[]

	for senteca in texto:
		frases.append(senteca.split(' '))#tokeniza o texto
	
	lista_de_parenteses = [] 
	lista_de_erros = []
	encontrados = []
	eliminacao = []
	semelhantes = []
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
								else:
									semelhantes.append(explicacao_Depois[0])
							
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
								else:
									semelhantes.append(explicacao_Antes[0])

							elif not (achados in eliminacao):
								eliminacao.append(achados)

								lista_de_parenteses.append((explicacao_Antes[0], -1, indices ))
				else:
					pass
	return (obtemExplicacao(frases,lista_de_parenteses,semelhantes))
