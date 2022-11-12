from time import sleep

import pdfplumber as pdf

titulo = list()

pdf_open = pdf.open('utils/hcp.pdf')


v_t = []
cont = 3

def v_titulo():
    global cont
    global pagina
    global titulo
    while cont < 399:
        page = pdf_open.pages[cont]
        text = page.extract_text()
        pagina = text.split('\n')
        for l in pagina:
            if l[0:3].isdigit() == True:
                v_t.append(f'{l[0:3]}. ')
        
        for i in sorted(set(v_t)):
            for l in pagina:
                if i in l:
                    titulo.append(f'{l}')
        cont += 1

v_titulo()

with open('1-9.txt', 'w') as arquivo:
    arquivo.write("\n".join(titulo))