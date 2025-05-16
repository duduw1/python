import csv
import time


# 1. abrir o arquivo 
with open ('0_dados_history.csv', encoding='utf-8') as arquivo_referencia:
    # 2. Ler a tabela
    tabela = csv.reader(arquivo_referencia, delimiter=',')
    # 3. navegar pela tabela
    for l in tabela:
        id_autor =l[0]
        nome = l[1]

        print(id_autor, nome)
        time.sleep(2)
