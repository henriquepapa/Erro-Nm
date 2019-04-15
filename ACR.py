from nltk.tokenize import word_tokenize,sent_tokenize
import glob,os
import wikipedia
import requests
import re

def contarpalavras(frase):

    return frase.count(' ')+1 # retorna a quantidade de espaços na frase





def dividetexto(senteca):
        ax=word_tokenize(senteca)#tokeniza aas sentenças, gerando uma lista
        frase=[]



        for palavras in ax: #percorre todas as palavras da lista
            palavras=palavras.replace('-',' - ')#coloca espaços entre os hifem


            if ' ' in palavras:# se encontrar um espaço na palavra
                k=word_tokenize(palavras)# divide a palavra em uma lista
                for pa in k:
                    frase.append(pa)#coloca as partes em uma lista final
            else:
                frase.append(palavras)


        return frase



def listadeabreviacao():


    page=requests.get("http://www.academia.org.br/nossa-lingua/reducoes",stream=True)#pesquisa a pagina

    texto=(page.text)#pega todo HTML da pagina

    texto = re.sub('<[^>]+?>', '', texto)#remove marcações HTML

    indice= texto.find('A ampere(s), ampère(s)')#acha o fim do texto inicial

    texto=texto.replace(texto[0:indice],'')#remove texto inicial

    indice= texto.find('Voltar')#acha o começo do texto final

    texto=texto.replace(texto[indice:len(texto)],'')#retira texto final
    ax=texto.split('\n')# divide as abreviações

    lista=[]
    ret=[]
    retira=[]


    for palavras in ax:


      x=palavras.split(' ')# divide palara e explicação

      if len(x)<3:

        palavra=x[0]# pega apenas explicacao



        if len(palavra)>1:

          if palavra[len(palavra)-1]=='.':#veifica se a palavra tem '.' no final

            palavra=palavra.replace(palavra[len(palavra)-1], palavra[len(palavra)-1]+';')#marca o ponto no final com ';'

            palavra=palavra.replace('.;','')#remove apenas o ultimo '.'

        lista.append(palavra)
      else:
        if len(x[0])==2:#verifica ambiguidade
          ret.append(x[0])


    for i in ret:# tira palavras com ponto
      if not('.' in i):
        retira.append(i)





    lista=set(lista)#tira palavras repetidas

    saida=[]
    for i in lista:
      if len(i) > 1 and not('.' in i):#retira palavras com '.' no meio
        saida.append(i.upper())#deixa as palavras em caixa alta

    retorno=[]

    Estados=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    Partido=['PT','PV','PP','PR','SD','PL']

    naodeve=Estados+retira+Partido

    for i in saida:# retirando os estados
      if not(i in naodeve) and len(i)==2:
        retorno.append(i)

    return retorno


def pesquisasigla(sigla1):
    sigla = sigla1.upper()
    s = wikipedia.search(sigla)#LISTA DE PESQUISA
    cont=0
    for explicacao in s: #PARA CADA SIGNIFICADO

        if sigla1 in pesquisadas: #palavra ja foi identificada como sigla
            return 1
        if sigla1 in pesquisadasnao: #palavra ja foi identificada como nao sigla
            return 0


        if cont==1: #numero maximo de sumarios
            pesquisadasnao.append(sigla1)
            return 0

        try:
            try :
                sumario = wikipedia.summary(explicacao, sentences = 1) #BUSCO O SUMARIO
            except (wikipedia.exceptions.PageError,wikipedia.exceptions.DisambiguationError) as g:

                try:
                    sumario = wikipedia.summary(s[cont],sentences=1)
                except wikipedia.exceptions.DisambiguationError as j:#so nomes causam esse erro
                    return 0

        except wikipedia.exceptions.DisambiguationError as e:
            try:
                if len(e.options)>0:
                    sumario = wikipedia.summary(e.options[0], sentences = 1)#SE TIVER MAIS DE UM, PEGO O PRIMEIRO
            except wikipedia.exceptions.DisambiguationError as f:
                if len(e.options)>0:
                    sumario = wikipedia.summary(e.options[1], sentences = 1)
        if ' ' in sumario: #verifica se os sumario contém espaços
         sumario = sumario.split(" ")#divide o sumario em palavras

         for i,palavra in enumerate(sumario):

        #objeto entre parentesês---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if palavra == '('+sigla+')' or palavra == '('+sigla+').' or palavra=='('+sigla+'),' or palavra == " ("+sigla+") " or palavra == ' ('+sigla+'),' or palavra=='('+sigla1+')' or palavra == '('+sigla or palavra == '('+sigla+'s)':
                pesquisadas.append(sigla1)#coloca na lista de pesquisadas sendo sigla
                return 1
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------

            if(palavra == sigla+')' or palavra == sigla+'),' or palavra == sigla+').'):
                pesquisadas.append(sigla1)#coloca na lista de pesquisadas sendo sigla
                return 1

         #Caso 2-Explicação padrao---------------------------------------------------------------------------------------------------------------------------------------------
            if(palavra == sigla or palavra==sigla1):
                if(sumario[i+1]!=''):
                    if sumario[i+1][0]=='(' and sumario[i+1]=="(sigla" or sumario[i+1]=="(anteriormente" :
                        pesquisadas.append(sigla1)#coloca na lista de pesquisadas sendo sigla
                        return 1

                else:

                    if sumario[i+2][0]=='(' and sumario[i+2]=="(sigla" or sumario[i+2]=="(anteriormente":
                       pesquisadas.append(sigla1)
                       return 1
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        cont=cont+1
    return 0


def verificasigla(palavra,frase,i):
    veri=0
    vogais= ['À','Á',"Â","Ã",'É','È','Ê','Ì','Í','Î','Ò','Ó','Ô','Õ','Ù','Ú','Û']# Vogais com acento
    numeros=['1','2','3','4','5','6','7','8','9','0']
    posi=i


#Abreviações

    if palavra in abreviacao:
        return 0

#---------------------------------------------------------------------------------------------

#Regra das cidades

    if i<2: #elimina cidades no começo da frase
        while (posi<len(frase)-1):
            if frase[posi]=='-':
                return 0
            if not(frase[posi][0].isupper()) and frase[posi]!='e':
                break

            posi=posi+1


#----------------------------------------------------------------------------

#Regra da moeda

    if i<len(frase)-1:
        if frase[i+1]=='$': #se houver um $ na frente, não e sigla
            return 0
#-----------------------------------------------------------------------------

#Regra do projeto de lei

    if i<len(frase)-2:
        if frase[i+1]=='-':
            for letra in frase[i+2]:# se hover letras e numeros separados por hifen, nao e sigla.Ex(PAC-9014)
                if letra in numeros:
                    return 0
#--------------------------------------------------------------------------------

#Regra dos Nomes
    #if i>1 and i<len(frase)-1:
        #if frase[i-1][0].isupper() or frase[i+1][0].isupper() and  frase[i-2][0]!='.' :# se a proxima palavra ou a anterior começar com letra maiuscula nao é sigla
            #return 0
#---------------------------------------------------------------------------------------------------------------


#Todas maiusculas--------------------------------------------------------------------------------------------------------------

    for letra in palavra:
        if letra.isupper():
            veri=veri+1#conta letras maiusculas
        if letra in vogais or letra in numeros:# se tiver acento ou numeros na palavra, nao e sigla
                return 0

    if veri== len(palavra) and len(palavra)>1:# se todas palavras forem  maiuscula é uma sigla
            return 1
#Pesquisa wikipedia---------------------------------------------------------------------------------------------------------------
    if (i<len(frase)-1) and i>0:

        if frase[i+1]!='(' and palavra[0].isupper() and len(palavra)>2 and frase[i-1]!='.':
            if pesquisasigla(palavra):
                return 1

    else:
        return 0



def verificadepois(palavra,token,i):
    tamanho= len (token)# Tamanho da Frase
    letras=[]



    for letra in palavra:
        if letra.isupper():
            letras.append(letra)


    if  token[i+1] == "("  :
        cont=i+2# caminha pra frente na frase

        while cont!= tamanho:

            if verificasigla(token[cont],token,cont)or token[cont] ==',' or token[cont]=='.':# se encontar uma , ou . ou outra sigla ele para a verificação.
                return 0

            p=token[cont]

            if p[0].lower() == letras[0] or p[0].upper() ==letras[0] :# verifica se a palavra começa com letra maiuscula
                letras.remove(letras[0])

                if len(letras)==0:
                    return 1

            cont=cont+1
        if len(letras)==0:# se o total de palavras começando com letra maiuscula for igual ao total de letras da sigla o significado foi dado
            return 1


        else:
            return 0

    else:
        return 0



def verificaantes(palavra,token,i):
    letras=[]


#cria lista com letras da sigla
    for letra in palavra:
        if letra.isupper():
            letras.append(letra)


    if token[i-1] == "(" :
        cont=i-2 # caminha para tras na frase

        while cont !=0 and cont > (i-(len(palavra)+5)):# para quando chegar no inicio ou atingir o limite

            if verificasigla(token[cont],token,cont) or token[cont]==',' or token[cont]=='.': # se encontar uma , ou . ou outra sigla ele para a verificação.
                return 0

            p= token[cont]

            if p[0].lower() == letras[len(letras)-1] or p[0].upper() ==letras[len(letras)-1] :# verifica se a palavra começa com letra maiuscula
                letras.remove(letras[len(letras)-1])
                if len(letras)==0:
                    return 1
            cont=cont-1
        if len(letras)==0:
            return 1
        else:
            return 0
    else:
        return 0

def verificarmaiusculo(frase,n):#chama os dois metodos de verificaçao



    frase =dividetexto(frase)#divide a frase em palavras
    maiusculas=0#numero de siglas
    sigla=""#explicação da sigla
    for i, palavra in enumerate(frase):


        if verificasigla(palavra,frase,i) and not(palavra in explicada) and not(palavra in nexplicada) :
            maiusculas=maiusculas+1
            sigla=sigla+ "\n"+palavra +" Encontrada em S"+str(n+1)



            nexplicada.append(palavra)

            if i< len(frase)-2:

                if verificadepois(palavra,frase,i):


                    explicada.append(palavra)


                    if palavra in nexplicada:
                        nexplicada.remove(palavra)



            if i>2:

                   if verificaantes(palavra,frase,i):

                       explicada.append(palavra)

                       if palavra in nexplicada:
                            nexplicada.remove(palavra)

            if palavra in nexplicada:
               sigla= sigla+"- Erro acrônimo sem explicação"

    return (maiusculas,sigla);




def saidaDeDados(i):
    i.replace( '.txt',"")
    nome=i
    arq=open(nome,'w')
    arq.write('Resultado da análise do arquivo' +"\n\n\n")
    Totalp=0
    totalm=0
    siglas=[]


    for i in range(len(txt)):#percorre todas as posiçoes de meu vetor de frases

        arq.write(' S')
        arq.write(str(i+1)+"- ")
        arq.write(txt[i])
        arq.write('\n')
        Totalp=Totalp+contarpalavras(txt[i])#conta as palavras
        ax1,ax2=verificarmaiusculo(txt[i],i)
        totalm=totalm+ax1
        siglas.append(ax2)


    arq.write("\n \n O total de palavras é =")
    arq.write(str(Totalp))
    arq.write("\n \n O total de Siglas é =")
    arq.write(str(totalm))
    arq.write("\n\n As siglas encontradas foram"+"\n")

    for i in siglas:
        arq.write(i)
    arq.close

#Começa o main ----------------------------------------------------------
def main ():
    cont=1
    lista=[]
    os.chdir("C:\\Users\\henri\\Documents\\IC\\textos")
    wikipedia.set_lang('pt')
    pesquisadas=[]
    pesquisadasnao=[]

    abreviacao=listadeabreviacao()

    for i in glob.glob("*.txt"):

        print('Analisando: '+i)
        print('\n\n\n')


        arquivo=open(i,'r',encoding='utf-8');

        texto=arquivo.read()#le o aqrquivo todo


        txt=sent_tokenize(texto)#divide o arquivo em frases
        explicada=[]
        nexplicada=[]

        saidaDeDados(i)
        cont+=1

def funcao_ACR(texto):
    quantidade=0
    siglas = []
    for numero,linhas in enumerate(texto):
        ax1,ax2 = verificarmaiusculo(linhas, numero)

        
        if ax2 != '':
            siglas.append(ax2)
        quantidade = quantidade + ax1

    return quantidade,siglas;

#-------------------------------------------------- GLOBAIS-------------------------------
wikipedia.set_lang('pt')
abreviacao= listadeabreviacao()
pesquisadas=[]
pesquisadasnao=[]
explicada=[]
nexplicada=[]