'''tokenizador'''


__version__ = "0.3"

import argparse
import sys
import fileinput
import re
import os

def main():

    parser = argparse.ArgumentParser(
                        prog='tok',
                        description='tokenizador',
                        epilog='')
    parser.add_argument('filename', help="input")
    parser.add_argument('-l','--ling',default='pt', help="lingua(pt,en)")
    args = parser.parse_args()

    dir = os.path.abspath(__file__)
    dir = dir[:dir.rfind('/')]
    

    def remove_empty(l):
        return [x.strip() for x in l if x.strip() != '']

    def load_abrev():
        file = open(dir + "/conf/abrev.txt", "r")
        txt = file.read()
        in_list = txt.split('#')
        abrev_dic = {}
        for lan in in_list:
            ln,*abrevs = lan.split('\n')
            if len(abrevs) > 0:
                abrevs = remove_empty(abrevs)
                abrev_dic[ln] = abrevs
        file.close()
        return abrev_dic
    
    def abrev_identifier(abrev_dic,lang):
        abrevs = abrev_dic[lang]
        abrevs = '|'.join(abrevs)
        for abrev in abrevs:
            regex = r'(\w+)( )('+abrev+r')(\.)(\s)'

        return regex

        

    text = ""

    
    file = open(args.filename, "r")
    text = file.read()
    file.close()

    abrev_dic = load_abrev()

    if args.ling in abrev_dic:
        abrev_regex = abrev_identifier(abrev_dic,args.ling)
        text = re.sub(abrev_regex, r'<abrev>\3</abrev>', text)

    #0 quebras de pagina    done
    #1 seprar pontuação das palavras  done
    #2 marcar capítulos      done
    #3 separar paragrafos linhas pequenas  ?????
    #4 Juntar linhas da mesma frase  done
    #5 uma frase por linha done




    regex_pont = r'(\W)([-–—.:;!?,])(\w)'
    text = re.sub(regex_pont, r'\1\2 \3', text, flags=re.UNICODE)



    regex_cap = r".*(CAP[ÍI]TULO( )+\w+).*\n(.*)\n"
    text = re.sub(regex_cap, r"\1<paragrafo>--->\3<paragrafo>", text)



    regex_nl = r"([a-z0-9,;-])\n\n([a-z0-9])"
    text = re.sub(regex_nl, r"\1\n\2", text)



    reg_par = r'([.:!?]”?)(\s*?)\n'
    text = re.sub(reg_par,r'\1</paragrafo><paragrafo>',text)


    text = re.sub(r'\n',r' ',text)
    reg_frase=r'([.:!?]”?)\s*([A-Z0-9“–])'
    text = re.sub(reg_frase,r'\1\n\t\2',text,flags=re.UNICODE)

    text = re.sub(r'<paragrafo>',r'\n\n',text)
    text = re.sub(r'</paragrafo>',r'',text)
    text = re.sub(r'</?abrv>',r'',text)


    arr_poemas = []

    def guarda_poema(match):
        arr_poemas.append(match.group(1))
        return f">>{len(arr_poemas)}<<"
    

    


    regex_poema = r"<poema>(.*?)</poema>"

    text = re.sub(regex_poema, guarda_poema, text, flags=re.S)




    print(text)
