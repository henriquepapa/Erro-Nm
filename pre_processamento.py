#!/usr/bin/python
# -*- coding: UTF-8 -*-


import glob,os,shutil
import re
import csv
import xml.etree.ElementTree as ET

def lerXml(file): #le os arquivos no formato XML

    with open(file, 'r') as xml_file: # Abre XML
        tree = ET.parse(xml_file)
        root = tree.getroot() # pega a raiz do arquivo
        
    lista = [] 
    dicionario = {}
    for t in root.iter('t'): 
        lista.append(t.attrib) # pega as palavras do texto
    for palavras in lista:
        dicionario[palavras['word']] = palavras['pos'] # cria o discionario com as e sua analise

    return dicionario;



def CleanHTML(text): # retira marcações HTML
     cleanr = re.compile('<.*?>')
     cleantext = re.sub(cleanr, '', text)
     return cleantext

def limpar_Marcacoes(file): # limpa o texto
    texto=[]

    for i in range(1,51):
        os.chdir ("C:\\Users\\henri\\OneDrive\\Documentos\\corpus marcado\\C"+str(i))
        for file1 in glob.glob("*.txt"):

            if file == file1:

                file= open(file,'r',encoding='UTF-8') # abre o arquivo

    arq= [[]]

    txt=file.read()
    raw = txt.split('[') # divide em frase
    #raw= sent_tokenize(txt)#divide o arquivo em frases  
    
    for linha in raw:
        linha = CleanHTML(linha) # tira as marcações das frases
        if "S" in linha:
            linha = linha[linha.index("]")+1:].strip() 
            linha.replace('\n','')
        arq.append (linha+'\n')

    arq.remove(arq[0]) # tira lixo das duas primeras posições
    arq.remove(arq[0])

    file.close()

    return arq # retorna o texto limpo dividido em frases




def pre_Processamento(file):

    discionario ={} # discionario do palavras

    linhas = limpar_Marcacoes(file) # texto limpo


    for i in range(1,51): #percorre todo o Córpus
        os.chdir ("C:\\Users\\henri\\OneDrive\\Erro nM\\Textos XML\\Corpus\\C"+str(i))

        for arq in glob.glob("*.xml"):
            if file.replace('.txt','_palavras.xml') == arq: # ve se o texto .txt corresponde com o XML
                discionario = lerXml(file.replace('.txt','_palavras.xml')) # pega o XML correspondente
            

    return linhas, discionario # retorna o texto limpo dividido em linhas e o discionario do palavras

os.chdir('C:\\Users\\henri\\OneDrive\\Documentos\\corpus marcado\\C1')






