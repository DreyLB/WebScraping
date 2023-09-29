import json

with open('html_bruto.txt', 'r') as arquivo:
    ler = arquivo.read()
    try:
        dados = json.loads(ler)
    except:
        print('Sem chave e valor')
    finally:
        print(dados)
