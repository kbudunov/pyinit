cs_courses = {'History', 'Math', 'Math',  'COmpSci'} #unordered but elements are uniq
print(cs_courses)

result = 'Math' in cs_courses
print(result)

art_courses = {'History', 'Art', 'Design'}

#set operations
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


