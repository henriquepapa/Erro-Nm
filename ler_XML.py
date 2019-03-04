import xml.etree.ElementTree as ET

def lerXml(file):

	with open(file, 'r') as xml_file:
	    tree = ET.parse(xml_file)
	    root = tree.getroot()
		
	lista = []
	dicionario = {}
	for t in root.iter('t'):
		lista.append(t.attrib)
	for palavras in lista:
		dicionario[palavras['word']] = palavras['pos']

	return dicionario;
