### TPC5

## Ficheiros importantes
- __init__.py
- abrev.txt


## Resumo

Completando o que foi pedido na aula de terça-feira, continuei a implementação do dicionário de abreviaturas, aumentando o dicionário para suportar variadas linguas, sendo que apenas adicionei inglês. Através do flit consegui tornar a aplicação num comando de terminal utilizável em qualquer diretoria do meu computador. A partir do mesmo coloquei uma flag que permite escolher a lingua do texto de modo a que o dicionário de abreviaturas seja o correto. Depois de selcionada a lingua e o ficheiro de input, obtenho a lista de abreviaturas dessa língua e através de regex identifico no texto de input as abreviaturas de modo a não ficarem desformatadas pelas outras formatações. Tudo o resto de formatação já estava realizada do tpc anterior. Por fim depois de toda a implementação não consegui fazer o teste do flit, pois não ao instalar o programa deu me o seguinte erro: "ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: '/home/private/.local/lib/python3.8/site-packages/tokenizador/__init__.py'" que não consegui resolver, portanto vou tirar esta duvida na aula e depois verificarei o código implementado.