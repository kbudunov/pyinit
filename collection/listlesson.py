#LIST IS MUTABLE

courses = ['History', 'Math', 'COmpSci']

print(courses[0])
print(courses[-1]) #last one element gonna be shown

print(len(courses))
print(courses[0:2]) #take 2 elements start at 0
print(courses[1:]) #from 1 to end


#add
courses.append('Art') #appent to end
courses.insert(0, 'Art') #insert on position
courses_2 = ['Education', 'Art']
#courses.insert(0, courses_2) #[['Art', 'Education'], 'Art', 'History', 'Math', 'COmpSci', 'Art']
courses.extend(courses_2)
print(courses)


#remove
courses.remove('Math')
popped = courses.pop() #it takes and removes las value as in stack
print(popped)

#sort
courses.reverse() #it revers cources
courses.sort() #it is gonna sort ASC
nums = [10,12,3,100,5,6]
nums.sort() #is changes the source list
print(nums)
nums.sort(reverse=True)
print(nums)

sorted_courses_2 = sorted(courses_2) #it does not change the source list
print(courses_2)
print(sorted_courses_2)


#getindex
print(courses.index('Art'))

#exists ?
result = 'Art' in courses
print(result)

#for example
for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)


#join and split
courses = ['History', 'Math', 'COmpSci']

courses_str = ', '.join(courses) #History, Math, COmpSci
print(courses_str)

new_list = courses_str.split(', ')
print(new_list)