import pdfplumber as pdf

titulo = list()

pdf_open = pdf.open('utils/hcp.pdf')


v_t = []
cont = 0

page = pdf_open.pages[383]
text = page.extract_text()
pagina = text.split('\n')

while cont < 400:
    cont += 1

def v_titulo():
    for l in pagina:
        if l[0].isdigit() == True:
            v_t.append(f'{l[0]}. ')

        if l[0:2].isdigit() == True:
            v_t.append(f'{l[0:2]}. ')

        if l[0:3].isdigit() == True:
            v_t.append(f'{l[0:3]}. ')

    for i in v_t:
        for l in pagina:
            if i in l:
                print(l)

v_titulo()