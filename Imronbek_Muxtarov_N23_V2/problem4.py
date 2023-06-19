import os; os.system('cls')
f, fk, fa = open('tovar.txt', 'w+'), open('Kharfli.txt', 'w'), open('Aharfli.txt', 'w')
f.write("ruchka\nalbom\nkonstovar\nqalam\nkitob\nmix\narra\narava\nko'ylak")
f.seek(0)
for i in f.read().split():
    if 'K' in i or 'k' in i:
        fk.write(i + ' ')
    if 'A' in i or 'a' in i:
        fa.write(i + ' ')