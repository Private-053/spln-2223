import sys
import fileinput
import re

text = ""
for line in fileinput.input():
    text += line

#0 quebras de pagina    done
#1 seprar pontuação das palavras  done
#2 marcar capítulos      done
#3 separar paragrafos linhas pequenas  ?????
#4 Juntar linhas da mesma frase  done
#5 uma frase por linha done

regex_sr = r'(Sr(t?)(a?)(s?))\s*(\.)'
text = re.sub(regex_sr, r'<sr>\1\4</sr>', text)



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
text = re.sub(r'<sr>',r'',text)
text = re.sub(r'</sr>',r'',text)

arr_poemas = []

def guarda_poema(match):
    arr_poemas.append(match.group(1))
    return f">>{len(arr_poemas)}<<"

regex_poema = r"<poema>(.*?)</poema>"
text = re.sub(regex_poema, guarda_poema, text, flags=re.S)


print(text)
