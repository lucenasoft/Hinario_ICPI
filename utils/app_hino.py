from time import sleep

louvores = list()
louvor = list()

with open('utils/hcp.txt',encoding="utf8") as f:
    content = f.readlines()

for x in content:
    louvor.append(x.rstrip('\n'))
print(louvor[0:10])


'''
cont_pdf = 1
l_l = 2


for l in louvores:
    if f'{l_l}.' not in l:
        louvor.append(l) 

    if f'{l_l}.' in l:
        with open(f'utils/hinos/{cont_pdf}.txt', 'w') as arquivo:
            arquivo.write("\n".join(louvor))
            cont_pdf += 1
            louvor.clear()
        l_l += 1'''