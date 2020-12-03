# print("Curs3")
#
# my_var = 9
#
# if my_var < 6:
#     print('Var mai mica decat 6')
# elif my_var < 10:
#     print('Var mai mica decat 10')
# elif my_var < 25:
#     print('Var mai mica decat 25')
# else:
#     print('Var mai MARE decat 25')
#
# apples = 0
# has_apples = 'Are mere' if apples else 'Nu are mere'
# print(has_apples)
#
# for i in range(10):
#     print(i)
#
# import random
#
# l = []
# for x in range(11):
#     l.append(x)
# print(l)
# # Sau se poate scrie asa:
# choises = [x for x in range(11)]
# print(choises)
#
# while True:
#     random_choice = random.choice(choises)
#     if random_choice % 3 == 0:
#         break
#     print(f'Random choice is {random_choice}')
# print(f'Exit Random choice is {random_choice}')
#
# for i in range(11):
#     if i % 2 != 0:
#         continue
#     print(f'{i} este par')
#
#
# def my_function(list_param):
#     local_list_param = list(list_param)
#     # sau list_param[:] sau list_param.copy()
#     local_list_param.append(4)
#     print('list_param inside function', local_list_param)
#
#
# list_param = [1, 2, 3]
# print(list_param)
# my_function(list_param)
# print('list_param outside function', list_param)


# def my_function1(name, age, job_name='Student', has_car=True):
#     has_car_str ='a car' if has_car else 'no car'
#     print(f'My name is {name} and my age is {age}.\nI\'m a {job_name}'
#           f' and I have {has_car_str}')
#     print('-' * 80)
#
#
# my_function1('John', 21, 'Web')
# my_function1('Rebeca', 31, has_car=False, job_name='Developer')


# def my_function2(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print('-' * 50)
#     for arg in args:
#         print(f'arg is {arg}')
#     for key in kwargs.keys():
#         print(f'key {key} has value {kwargs[key]}')
#     print('#' * 80)
#
#
# my_function2('Ana')
# my_function2('Ana', 'are', 'mere')
# my_function2(name='Ana', verb='are', complement='mere')
# my_function2(1, 2, 3, name='Ana', verb='are', complement='mere')


# while True:
#     my_var = input("Introduceti un nr: ")
#     try:
#         my_int = int(my_var)
#         # print(mi_int) # pentru NameError
#     except ValueError as e:
#         print('Va rog introduecti un nr intreg', e)
#     except NameError as e:
#         # print('Ai folosit o variabila nedefinita!\n',e)
#         pass
#     else:
#         print('Nici o exceptie nu a fost aruncata')
#     finally:
#         print('Se executa tot timpul')


# def my_function3():
#     global msg
#     msg = 'Hello World!'
#     print(msg)
#
#
# my_function3()
# print(msg)


def my_function4():
    def my_second_function4():
        print(f'my_second_function4 {msg}')

    msg = 'Hello World!'
    my_second_function4()
    print(f'my_function4 {msg}')


my_function4()
