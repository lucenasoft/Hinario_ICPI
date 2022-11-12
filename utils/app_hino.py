from time import sleep

import pdfplumber as pdf

louvor = list()

cont_pdf = 1
cont_louvor = 2
cont_pag = 3

pdf_open = pdf.open('utils/hcp.pdf')

while cont_pag < 401:
    page = pdf_open.pages[cont_pag]
    text = page.extract_text()
    pagina = text.split('\n')

    for l in pagina:

        while f'{cont_louvor}.' not in l:
            louvor.append(l)
            break   

        if f'{cont_louvor}.' in l:
            with open(f'utils/hinos/{cont_pdf}.txt', 'w') as arquivo:
                arquivo.write("\n".join(louvor))
                cont_pdf += 1
                louvor.clear()
            cont_louvor += 1
            cont_pag += 1