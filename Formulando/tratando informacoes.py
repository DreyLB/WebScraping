with open('html_bruto.txt', 'r+') as arquivo:
    listar_arquivo = []
    for c in arquivo:
        listar_arquivo.append(c)


componentes_listados = []
lista_final = []
with open('tratando_html.txt', 'w+') as arquivo:
    fonte = enumerate(listar_arquivo)
    for c in fonte:
        arquivo.write(str(c))

