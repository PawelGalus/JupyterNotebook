a = [1, 2, 3, 4]

a.append(5)
print(a)
print(a[0])

a.insert(2, 8)
print(a)

# a.insert(4, "Text")
# print(a)

a.reverse()
print(a) # Before sort
a.sort()
print(a)

last_element = a.pop()
print(last_element)
print(a)

a.clear
print(a)

a = [1, 1]
a = a * 5
print(a)

a = [1, 2]
b = [3, 4]
print(a + b)

a = [1, 2, 3, 4, 5, 6]
print(a[1:4]) # a[1:4] return the list a[1] to a[3]
print(a[:4])

a2 = a.copy()
a2.append(7)
print(a)
print(a2)

a2 = a
a2.append(7)
print(a)
print(a2)

tuple1 = (1, 2, 3)
print(tuple1[0])
# tuple[0] = 5 # ERROR

list1 = [1, 2, 3]
list1[0] = 5
print(list1)

tuple2 = (1,)
list2 = list(tuple2)
print(list2)

list2 = [1]
tuple2 = tuple(list2)
print(tuple2)