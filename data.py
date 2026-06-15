import json

# Copie aqui as listas de questões dos temas 1 a 6 dos arquivos que criamos antes.
# Exemplo (apenas estrutura):
# questoes_tema1 = [ {...}, {...} ]
# questoes_tema2 = [ ... ]
# ...
# Depois una tudo:

todas_questoes = []
for lista in [questoes_tema1, questoes_tema2, questoes_tema3, questoes_tema4, questoes_tema5, questoes_tema6]:
    todas_questoes.extend(lista)

# Exportar para JS
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('window.questoesData = ')
    json.dump(todas_questoes, f, ensure_ascii=False, indent=2)
    f.write(';')
print("data.js gerado com sucesso!")