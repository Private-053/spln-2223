### TPC5

## Ficheiros importantes
- __init__.py
- abrev.txt


## Resumo

Completando o que foi pedido na aula de terça-feira, continuei a implementação do dicionário de abreviaturas, aumentando o dicionário para suportar variadas linguas, sendo que apenas adicionei inglês. Através do flit consegui tornar a aplicação num comando de terminal utilizável em qualquer diretoria do meu computador. A partir do mesmo coloquei uma flag que permite escolher a lingua do texto de modo a que o dicionário de abreviaturas seja o correto. Depois de selcionada a lingua e o ficheiro de input, obtenho a lista de abreviaturas dessa língua e através de regex identifico no texto de input as abreviaturas de modo a não ficarem desformatadas pelas outras formatações. Tudo o resto de formatação já estava realizada do tpc anterior. Por fim depois de toda a implementação realizei o build e o install da aplicação para que possa ser utilizada em qualquer diretoria do meu computador.