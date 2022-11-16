from time import sleep

louvores = list()
louvor = list()

with open('utils/hcp.txt',encoding="utf8") as f:
    content = f.readlines()

for x in content:
    louvores.append(x.rstrip('\n'))
louvores = filter(None, louvores)

cont_pdf = 361
l_l = 362


for l in louvores:
    if f'{l_l}.' not in l:
        louvor.append(l) 

    if f'{l_l}.' in l:
        with open(f'utils/hinos2/{cont_pdf}.txt', 'w') as arquivo:
            arquivo.write("\n".join(louvor))
            cont_pdf += 1
            louvor.clear()
        l_l += 1