import os; os.system('cls')
dct = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}
lst = input("Sanani kiriting: ").split()
date, time = lst[0].split('.'), lst[1].split(':')
print(f"{int(date[0])} {dct.get(int(date[1]))} {date[2]} year {int(time[0])} {'hour' if int(time[0]) == 1 else 'hours'} {int(time[1])} {'minute' if int(time[1]) == 1 else 'minutes'}")