### TPC1

## Ficheiros importantes
- ex.py
- medicina.txt
- medicina.json

## Resumo

Primeiramente, comecei por transformar o ficheiro xml em ficheiro txt, utilizando o xml2html com a flag para tornar o ficheiro em texto.
Depois de obtido o ficheiro texto, fui substituindo as diferentes ocorrências, de modo a organizar toda a informação. As substituições foram realizadas consoante a sintaxe dada na aula.
Depois de feita a organização, coloquei o dicionário num ficheiro JSON, sendo este composto por duas chaves principais 'R' e 'C' para as entradas remissivas e completas. As entradas remissivas são compostas por um nome e uma string. As entradas completas são compostas por uma id e o valor é um dicionário com os seguintes campos:
  -  nome (string)
  -  info (lista)
  -  genero (lista)
  -  areas (lista)
  -  linguas (dicionario)
  -  nota (string)
O campo linguas é um dicionario em que as chaves são as línguas e o valor é a lista das palavras naquela língua.