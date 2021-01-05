#                   ----- String -----
# x = 'This is a string!'
# print(x)
# print(x.upper())
# print(x.lower())
# print(x.strip())
# print(x.replace(' is ',' is '))
# print(x.split())

# x = 'Hello, my name is {1} . In 2020, I"m {0} years old.'
# name = "Tu"
# year = 24
# print(x.format(year, name))

# x = 'He\'s name is \nJohn'
# print(x)

#                   ----- list, tuple, set, dict -----
# ['apple', 'samsung', 'nokia'] list : ordered and changeable. Allows duplicate members.
# ('apple', 'samsung', 'nokia') tuple : ordered and unchangeable. Allows duplicate members.
# {'apple', 'samsung', 'nokia'} set :  unordered and unindexed. No duplicate members.
# {'name': 'Tu', 'age': 20} dict :  unordered and unindexed. No duplicate members.

# x = ['apple', 'samsung', 'nokia']
# y = ['xiaomi', 'redmi']
# z = ('Bkav', 'microsoft soft')
# x.append('huawei')
# x.insert(0, 'google')
# y.extend(z)
# x.extend(y)
# x.remove('redmi')
# x.pop(7)
# x.pop()
# del x[3]
# x.clear()
# for ele in x:
#     print(ele)

# [expression for item in iterable if condition == True]
# [print(ele) for ele in x]
# newList = [ele for ele in x if 'a' in ele]
# print(newList)
# print(x)
# listFromZeroToNine = [x for x in range(10)]
# print(listFromZeroToNine)

# x = [2, 3, 1, 4, 21, 13]
# y = ['banana', 'apple', 'Orange']
# x.sort(reverse=True)
# x.reverse()
# y.sort(key = str.lower)
# print(x)
# print(y)

# x = [1, 2, 3]
# y = x.copy()
# z = list(x)
# t = y + z
# print(y)
# print(z)
# print(t)

# x = ('apple')
# print(type(x)) #string
# y = ('apple',)
# print(type(y)) #tuple

# tuple is unchangeable, so you need to turn it to list, then turn it to tuple :
# x = ('apple', 'banana', 'orange')
# y = list(x)
# y[1] = ('kiwi')
# x = tuple(y)
# print(x)

# When we create a tuple, we normally assign values to it
# fruits = ('apple', 'banana', 'orange')
# (apple, banana, orange) = fruits
# print(apple)
# print(banana)
# print(orange)
# fruits2 = ('apple', 'banana', 'orange', 'apple', 'banana', 'orange')
# (apple, banana, *orange) = fruits2
# print(apple)
# print(banana)
# print(orange)

# set
# x = {'apple', 'banana', 'orange'}
# print(x)
# Once a set is created, you cannot change its items, but you can add new items.
# x.add('kiwi')
# y = {'appl', 'banan', 'orang'}
# x.update(y)
# print(x)

# dictonary
# x = {
#     'name': 'Tu',
#     'age': 24,
#     'open': False
# }
# print(x.keys())
# print(x.values())
# print(x.items())
# x['dev'] = ['nodejs', 'python']
# x.pop('open')
# x.popitem()
# print(x)

#                   ----- Else If -----
# else if
# x = 1
# y = 2
# if x == y:
#     print('x is equal to y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x is less than y')
# print('x is equal to y') if x == y else print(
#     'x is greater than y') if x > y else print('x is less than y')


#                   ----- Function -----
# def my_function():
#     print('Hello World!')


# my_function()

# def my_function(*key):
#     print(key[1])


# my_function('apple', 'banana', 'orange')

# def my_function(**key):
#     print('He name is ' + key['name'])
#     print('He age is ' + key['age'])


# my_function(name='Tu', age='20')

# lambda
# def my_function(x): return lambda a: a+x
# print(my_function(1)(2))

#                   ----- Class -----
# class Person:
#     name = 'Tu'
#     age = 20
# Iam =  Person()
# print(Iam.name)
# print(Iam.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def hello(self):
#         print('My name is: ' + self.name)


# person1 = Person('Tu', 20)
# print(person1.name)
# print(person1.age)
# person1.hello()

# class Student(Person):
#     pass
# stu = Student('Tu',20)
# stu.hello()

# class Student(Person):
#     def __init__(self, name, age):
#         Person.__init__(self, name, age)
#         self.nameAndAge = name + str(age)


# stu = Student('Ha Dinh Tu', 20)
# stu.hello()
# print(stu.nameAndAge)

# import platform
# import datetime
# import json
# print(platform.system())
# print(datetime.datetime.now())
# x = '{"name" : "Tu", "age" : 20}'
# y = json.loads(x) # y is a dict
# x = {'name': 'Tu', 'age': 20}
# y = json.dumps(x) # y is a string


#                   ----- Input -----
# username = input('Enter User Name: ')
# print('user name is: ' + username)

# word = "bananana"
# i = word.find("na")
# print(i)

# counts = {'quincy': 1, 'mrugesh': 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))
# print(counts)
