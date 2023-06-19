import os; os.system('cls')
morse = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : "q", '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '---.' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z'}
n = 1
for i in input("Kiriting: ").split('  '):
    a = ''
    for j in i.split():
        if n:
            a = morse.get(j).upper()
            n = 0
        else:
            a = morse.get(j)
        print(a, end = '')
    print(end = ' ')