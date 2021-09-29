student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])

#Does not exists
#print(student['phone'])

print(student.get('phone')) #it returns None
print(student.get('phone', 'Not Found')) #it returns 'Not Found


#add
student['phone'] = '55555-5555'
student['name'] = 'Petr'

print(student)


student.update({'name': 'Jane', 'age': 26, 'phone': '32345-324'})
print(student)


#del
del student['age']
print(student)

#pop
phone = student.pop('phone')
print(phone)

#keys \ values \ items
print(len(student))
print(student.keys())
print(student.values())
print(student.items()) #dict_items([('name', 'Jane'), ('courses', ['Math', 'CompSci'])])

#for
for key, value in student.items():
    print(key, value)






