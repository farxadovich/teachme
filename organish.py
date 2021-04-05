
li = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for i in li:
    print(i)

while True:
    x = int(input('birinchi foydalanuvchidan : '))

    if x == 1:
        li[0][0] = 'x'
    elif x ==2:
        li[0][1] = 'x'
    elif x == 3:
        li[0][2] = 'x'
    elif x == 4:
        li[1][0] = 'x'
    elif x == 5:
        li[1][1] = 'x'
    elif x == 6:
        li[1][2] = 'x'
    elif x == 7:
        li[2][0] = 'x'
    elif x == 8:
        li[2][1] = 'x'
    elif x == 9:
        li[2][2] = 'x'

    else:
        print("Iltimos \n Togri son kiriting")

    for i in li:
        print(i)

    O = int(input('ikkinchi foydalanuvchidan : '))
    if O == 1:
        li[0][0] = 'O'
    elif O == 2:
        li[0][1] = 'O'
    elif O == 3:
        li[0][2] = 'O'
    elif O == 4:
        li[1][0] = 'O'
    elif O == 5:
        li[1][1] = 'O'
    elif O == 6:
        li[1][2] = 'O'
    elif O == 7:
        li[2][0] = 'O'
    elif O == 8:
        li[2][1] = 'O'
    elif O == 9:
        li[2][2] = 'O'

    else:
        print("Iltimos \n Togri son kiriting")

    for i in li:
        print(i)

    if li[0][0] == 'x' and li[0][1] == 'x' and li[0][2] == 'x':
        print('X  win')
    if li[1][0] == 'x' and li[1][1] == 'x' and li[1][2] == 'x':
        print('X  win')
    if li[2][0] == 'x' and li[2][1] == 'x' and li[2][2] == 'x':
        print('X  win')
    if li[0][0] == 'x' and li[1][0] == 'x' and li[2][0] == 'x':
        print('X  win')
    if li[0][1] == 'x' and li[1][1] == 'x' and li[2][1] == 'x':
        print('X  win')
    if li[0][2] == 'x' and li[1][2] == 'x' and li[2][2] == 'x':
        print('X  win')
    if li[0][0] == 'x' and li[1][1] == 'x' and li[2][2] == 'x':
        print('X  win')
    if li[0][2] == 'x' and li[1][1] == 'x' and li[2][0] == 'x':
        print('X  win')


    if li[0][0] == 'O' and li[0][1] == 'O' and li[0][2] == 'O':
        print('O  win')
    if li[1][0] == 'O' and li[1][1] == 'O' and li[1][2] == 'O':
        print('O  win')
    if li[2][0] == 'O' and li[2][1] == 'O' and li[2][2] == 'O':
        print('O  win')
    if li[0][0] == 'O' and li[1][0] == 'O' and li[2][0] == 'O':
        print('O  win')
    if li[0][1] == 'O' and li[1][1] == 'O' and li[2][1] == 'O':
        print('O  win')
    if li[0][2] == 'O' and li[1][2] == 'O' and li[2][2] == 'O':
        print('O  win')
    if li[0][0] == 'O' and li[1][1] == 'O' and li[2][2] == 'O':
        print('O  win')
    if li[0][2] == 'O' and li[1][1] == 'O' and li[2][0] == 'O':
        print('O  win')
