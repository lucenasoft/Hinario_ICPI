from time import sleep

import pdfplumber as pdf

louvor = list()

pdf_open = pdf.open('utils/hcp.pdf')

page = pdf_open.pages[329]
text = page.extract_text()
pagina = text.split('\n')

for l in pagina:
    if '407. ' not in l:
        louvor.append(l)
    else:
        break

with open('Louvores.txt', 'w') as arquivo:
    arquivo.write("\n".join(louvor))