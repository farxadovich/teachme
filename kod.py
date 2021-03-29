# y = 5
#
#
# if y == 1:
#     print('y 1 ga teng')
#
# elif y == 2:
#     print('y 2 ga teng')
#
# elif y == 3:
#     print('y 3 dan teng')
# else:
#     print('y hammasidan katta')



# a = 2
# if a > 1 or a >0:
#     print('aaa')
#




# my_list = [[1, 2, 3]
#            [4, 5, 6]
#            [7, 8, 9]]
# x = int(input('birinchi odam kiriting'))
# x =  int(input('ikkinchi odan kiriting'))


# from beautifulTable import BeautifulTable
# https://beautifultable.readthedocs.io/en/latest/quickstart.htmlbuilding-the-table
#
# table = BeautifulTable()
# table.rows.apeend(["A", "B", "C", "C", "E", "F", "J", "I", "J"])
# table.rows.apeend(["A", "B", "C", "C", "E", "F", "J", "I", "J"])
# table.rows.apeend(["A", "B", "C", "C", "E", "F", "J", "I", "J"])
# table.rows.apeend(["A", "B", "C", "C", "E", "F", "J", "I", "J"])
# table.rows.apeend(["A", "B", "C", "C", "E", "F", "J", "I", "J"])
# table.rows.apeend(["A", "B", "C", "C", "E", "F", "J", "I", "J"])
#
# table.set_style(BeautifulTable.STYLE_BOX)
# print(table)
# table.rows[5][1] = 'A'
# print(table)




# def is_leap(year):
#     if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#         return True
#     return False
#
#
# print(is_leap(400))
# print(is_leap(300))
# print(is_leap(44))
# print(is_leap(100))
# print(is_leap(1200))
# print(is_leap(900))



# def get_lines(file):
#     with open(file, 'r') as reader:
#         return reader.readlines()
#
# print(get_lines('data.txt'))


# def my_func(a, b, c):
#     print(a+b+c)
#
#
# my_func(b=5, a=7, c=3)


# def my_func(ismi='mehmon', familiyasi=':)'):
#     print(f'{hi} {ismi} {familiyasi}')
#
# my_func('salom', 'aziz')




# def my_func(*a):
#     print(a)
#
# my_func(1, 2, 3, 5, 6, )
#





# def my_func(a,b,*c):


# def teskari_satr(txt):
#     res = ''
#     for i in txt:
#        res = i + res
#     return res
#
#
# print(teskari_satr('abbbbbos szi'))

# def fatoriyal(n):
#     if n == 1:
#         return 1
#     return  fatoriyal(n-1) * n
#
#
# print(fatoriyal(3))

# li = ['a', 'b', 'c', 'd', 'g']
#
# print(li[ ::-1])
# def my_func(func, x):
#     return func(x)
# def kvadrat(x):
#     return x * x
#
#
# def kubi(x):
#     return x ** 3
#
# result = my_func(kubi, 1)
# print(result)
# def my_func(usul):
#
#
#     def kvadrat(x):
#         return x * x
#
#     def kubi(x):
#         return x ** 3
#
#
#     if usul == 'kubi':
#         return kubi
#     else:
#         return kvadrat
#
#
# kub_finc = my_func('kvadrat')
#
# print(kub_finc(3))
# def my_func(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f'{k} {v}')
#
#
# my_func(a='AAA', b='BBB', c='CCC', d='DDD', e='EEE')

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# list2 = [i for i in li if i % 2 == 0]
#
# print(list2)
# list2 = [i for i in range(100) if i % 7 == 0]
#
# print(list2)

# def my_func(li):
#     return [ i*i for i in li]
# li = [6, 7, 8, 9, 45, 67, 89]
# print(my_func(li))de





# li = [1 ,2]
# try:
#     x = 'abc'
#     y = 5
#     z = x + li[6]
#     print(z)
#
#
# except TypeError as error:
#     print(error)
# except IndexError as indexda_xatolik:
#     print(indexda_xatolik
# while True:
#     li =[0,'nol',
#          1, 'bir',
#          2, 'ikki',
#          3, 'uch',
#          4, 'tort',
#          5, 'besh',
#          6, 'olti']
#     try:
#         li = input('raqam kiriting: ')
#     except Exception:
#         print('iltimos togri son kiriting')
#
# li = ['bir',  'ikki', 'uch', 'tort']
#
#
# while True:
#     try:
#         print(li[int(input('raqam kiriting: '))-1])
#     except IndexError:
#         print(f'listning max uzunligi {len(li)}')
#     except ValueError:
#         print('tugri yoz')
# try:
#     x = 'abs'
#     y = 5
#     b = x + z
#     print(b)
#
# except NameError:
#     print('mavjud bolmagan ozgaruvchi kiritdingiz: ')


# li =  {1: 'I',
#        2: 'II',
#        3: 'III',
#        4: 'IV',
#        5: 'V',
# }
# x = int(input('raqamkiriring='))
# print(li[x])
# def my_func():
#     while True:
#         return
# key = {1: 'I',
#        2: 'II',
#        3: 'III',
#        4: 'IV',
#        5: 'V',
#        6: 'VI',
#        7: 'VII',
#        8: 'VIII',
#        9: 'IX',
#        10: 'X'
#        }
# x = int(input('raqam kiriting: '))
# print(key[x])
#




# def xarflar():
#     x = input('satr yuboring: ')
#     b = input('yana satr kiriting:')
#     z = []
#     for i in x:
#         if i in b:
#             z.append(i)
#     print(z)
# xarflar()

' namespase - nomlar koiniti'


# def func(a, x):
#     if a > x:
#         return a
#     else:
#         return x
def my_func(x):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    for i in range(len(val)):
        roman += symbol[i] * (x // val[i])
        x = x % val[i]

    return roman
print(my_func(1))





















































































































































































































































