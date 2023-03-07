import ply.yacc as yacc
from lex import tokens,literals

def p_1(p):
    "dic : Es"
    pass

def p_2(p):
    "Es : E LINHA_B Es"
    pass

def p_3(p):
    "Es : E"
    pass

def p_4(p):
    "E : Itens"
    pass

def p_5(p):
    "Itens : Item '#' Itens"
    pass

def p_6(p):
    "Itens : Item"
    pass

def p_7(p):
    "Item : AtrC"
    pass

def p_8(p):
    "Item : Ling"
    pass

def p_9(p):
    "AtrC : ID ':' VALOR"
    pass

def p_10(p):
    "Ling : IDL ':' Ts"
    pass

def p_11(p):
    "Ts : Ts T"
    pass

def p_12(p):
    "Ts : T"
    pass

def p_13(p):
    "T : '-' VALOR AtrTs"
    pass

def p_14(p):
    "AtrTs : AtrTs2"
    pass

def p_15(p):
    "AtrTs : "
    pass

def p_16(p):
    "AtrTs2 : AtrTs2 AtrT"
    pass

def p_17(p):
    "AtrTs2 : AtrT"
    pass

def p_19(p):
    "AtrT : '+' ID ':' VALOR"
    pass

def p_error(p):
    print('Erro sintático: ',p)
    parser.sucess = False

parser = yacc.yacc()
parser.sucess = True
f = open("exemplo.txt","r")
program = f.read()

parser.parse(program)
if parser.sucess:
    print("Programa bem estruturado")
else:
    print("Programa Inválido")