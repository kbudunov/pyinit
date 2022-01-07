x = float('2.1')  # не принимает x = '2.1' из за того что сигнатура float(x=0, /)
print(x)

help(float)


# навязывание позиционных аргументов
def avg(a, b, c):
    return (a + b + c) / 3


print(avg(1, 2, 3))
print(avg(c=4, a=1, b=2))  # так тоже нормально работает


# с 3.8 появилось возможность принуждать к позиционным аргументам
#POSITIOPNAL ONLY ARGUMENTS
def avg2(a, b, c, /):
    return (a + b + c) / 3


print(avg2(1, 2, 3))


# print(avg2(c=4, a=1, b=2)) так уже нельзя

def avg3(a, b, c, /, d, s): #то что позже слеша является позиционным
    return (a + b + c + d + s) / 3

print(avg3(1, 2, 3, d=1, s=2))


#KEYWORD only arguments
def copy(*, source, destination, override=False):
    print('done!')

copy(source='d', destination='s', override=True)
#copy('d', 's', True)  так уже нельзя