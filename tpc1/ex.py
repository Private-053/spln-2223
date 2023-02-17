# ZEP -> E*
# E -> EC
#    | ER
# EC -> num pals pos CORPO
# CORPO -> area LINGUAS
# LINGUAS -> pt pals
#          | en pals
#          | es pals
# ER -> pals VID
# VID -> Vid.- pals

import re

texto = open('medicina.xml', 'r').read()

def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'___', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    texto = re.sub(r'<.xml.*',r'',texto)
    texto = re.sub(r'<.DOCTYPE.*', r'', texto)
    texto = re.sub(r'<pdf2xml.*', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaE(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)</b></text>', r'###C \1', texto)
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="11"><b>\s*(\S.*)</b></text>', r'###R \1', texto)  
    return texto

texto = marcaE(texto)


def marcaLinguas(texto):
    texto = re.sub(r'<text.* font="0">\s*(\S+)\s*</text>', r'@ \1', texto)
    texto = re.sub(r'@ ;', r';', texto)
    texto = re.sub(r'<text.* font="7"><i>(.*)</i></text>', r'\1', texto)
    return texto

texto = marcaLinguas(texto)

def removeEspacobranco(texto):
    texto = re.sub(r'<text.* font="\d*">\s*</text>', r'', texto)
    texto = re.sub(r'<text.* font="\d*"><b>\s*</b></text>', r'', texto)
    return texto

texto = removeEspacobranco(texto)

def removeFontspec(texto):
    texto = re.sub(r'<fontspec.*', r'', texto)
    return texto

texto = removeFontspec(texto)

def marcaArea(texto):
    texto = re.sub(r'<text.* font="6"><i>\s*(.*)\s*</i></text>', r'£ \1', texto)
    return texto

texto = marcaArea(texto)

def marcaSin(texto):
    texto = re.sub(r'<text.* font="5">\s*(SIN.*)</text>', r'\1', texto)
    texto = re.sub(r'<text.* font="0">\s*(SIN.*)</text>', r'\1', texto)
    return texto

texto = marcaSin(texto)

def marcaVar(texto):
    texto = re.sub(r'<text.* font="5">\s*(VAR.*)</text>', r'\1', texto)
    texto = re.sub(r'<text.* font="0">\s*(VAR.*)</text>', r'\1', texto)
    return texto

texto = marcaVar(texto)

def marcaVid(texto):
    texto = re.sub(r'<text.* font="\d*">\s*(Vid\..*)</text>', r'\1', texto)
    return texto

texto = marcaVid(texto)

def marcaNota(texto):
    texto = re.sub(r'<text.* font="9">(.*)</text>', r'\1', texto)
    return texto

texto = marcaNota(texto)

def limpaParagrafo(texto):
    texto = re.sub(r'<text.* font="5">(.*)</text>', r'\1', texto)
    return texto

texto = limpaParagrafo(texto)

def limpaFonte10(texto):
    texto = re.sub(r'<text.* font="10"><i><b>(.*)</b></i></text>', r'\1', texto)
    return texto

texto = limpaFonte10(texto)

def limpaFonte2(texto):
    texto = re.sub(r'<text.* font="\d+">\s*(\d+)\s*</text>\n###R(.*)', r'###C \1 \2', texto)
    return texto

texto = limpaFonte2(texto)

def elementosQuimicos(texto):
    texto = re.sub(r'<text.* font="13"><b>\s*(\d+)\s*</b></text>', r'_\1', texto)
    texto = re.sub(r'<text.* font="15"><i>\s*(\d+)\s*</i></text>', r'_\1', texto)
    texto = re.sub(r'<text.* font="14">\s*(\d+)\s*</text>', r'_\1', texto)
    return texto

texto = elementosQuimicos(texto)

def limpaFonte0(texto):
    texto = re.sub(r'<text.* font="0">\s*(\S.*)</text>', r'\1', texto)
    return texto

texto = limpaFonte0(texto)


file = open('medicina2.txt', 'w')

file.write(texto)
