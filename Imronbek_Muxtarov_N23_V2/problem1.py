import os; os.system('cls')
def right_join(lst : list):
    st = ''
    for i in lst:
        st += i.replace('left', 'right') + ', '
    return st[ : -2 ]
print(right_join([input(f"{i + 1} - ma'lumotni kiriting: ") for i in range(int(input("Necha marta ma'lumot kiritasiz: ")))]))