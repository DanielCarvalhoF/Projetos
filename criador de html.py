import os
folder = '.\Python PRO'
name_arquivo = input('qual o nome do arquivo \n')
extencao_arquivo = input('digite a extencão do arquivo\n')
arquivo = name_arquivo + extencao_arquivo
with open(arquivo,'w') as document:
    print(f'Agora digite o conteudo do arquivo {extencao_arquivo}')
    title = input('digite o titulo do arquivo\n')
    header = input('digite o Header do arquivo\n')
    print(f'Agora você vai escrever o coteudo do corpo do arquivo, lembrese que o arquivo se trata de um {extencao_arquivo}\n')
    body = input('Agora você vai escrever o coteudo do corpo do arquivo\n')
    document.write(f'<title>{title}</title>')
    document.write(f'<header>{header}</header>')
    document.write(f'<body>{body}<body>')
    print(f'aquivo {arquivo} foi criado com sucesso.')
