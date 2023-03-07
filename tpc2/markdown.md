### TPC2

## Ficheiros importantes
- lex.py
- yacc.py
- exemplo.txt


## Resumo

Depois de idealizada a minha gramática, passei á implementação do lexer e do parser. Para o lexer utilizei o módulo ply.lex e para o parser utilizei o módulo ply.yacc. Para testar o meu código utilizei o ficheiro exemplo.txt, que é um exemplo retirado do dicionário feito no tpc1.

Sendo esta a gramática utilizada:
```
dic : Es

Es : E LINHA_B Es
    | E

E : Itens

Itens : Item '#' Itens
    | Item

Item : AtrC
    | Ling

AtrC : ID ':' VALOR

Ling : IDL ':' Ts

Ts : Ts T
    | T

T : '-' VALOR AtrTs

AtrTs : AtrTs2
    |

AtrTs2 : AtrTs2 AtrT
      | AtrT

AtrT : '+' ID ':' VALOR
```
