#we can't modify tuples (IMMUTABLE)

list_1 = ['History', 'Math', 'COmpSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


tuple_1 = ('History', 'Math', 'COmpSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art' #tuples are immutable

print(tuple_1)
print(tuple_2)







