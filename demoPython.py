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
