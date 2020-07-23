
star = '*'
for i in range(0, 4):
    for j in range(4, i, -1):
        print(' ', end='')
    print(star)
    star = star + '**'
for i in range(0, 5):
    for x in range(1, i + 1):
        print(' ', end='')
    for y in range(8, (i * 2 - 1), -1):
        print('*', end='')
    print(' ')
        