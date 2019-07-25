# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:56:17 2019

@author: henri
"""

def coletaDados(dicionario):
	nomes = []
	for i in dicionario:
		if dicionario[i] == 'prop':
			nomes.append(i)
	return nomes


def erro_nomes(texto, dicionario):
	erros =[]

	nomes = coletaDados(dicionario)

	for i in nomes:
		if '_' in i:
			x = i.split('_')
			nome = x[0]
			sobrenome = i[1]

			if texto.count(nome)> 1 or texto.count(sobrenome) > 1:
				erros.append(i)

		elif texto.count(i)> 1:
			erros.append(i)

	return erros