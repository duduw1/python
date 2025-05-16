import csv

# 1. cria o arquivo
f = open('numero_dobro_triplo.csv','w', newline='', encoding='utf-8')

#2. cria objeto de gravação
w = csv.writer(f)

#3. grava as linhas
for i in range(10):
    w.writerow([i, i*2, i*3])

#4. Fechando arquivo
f.close()
