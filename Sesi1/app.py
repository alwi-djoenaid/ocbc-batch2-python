#print(10 + 11)

# name = "Hacktiv8"
# age = 22
# hasLaptop = True

# print(name, age, hasLaptop)

# a = 4
# b = 3
# print(a == b)

# s = 'foo'
# t = 'bar'
# print(s + t)
# print(s * 4)

a = 'Aaaaa'
i = 90
j = 122

print('Umur : {} {}'.format(i, j))
print('Umur : {nilai_i} {nilai_j}'.format(nilai_j = j, nilai_i =i))
print(f'Umur : {i} {j}')
print(f"Umur : {i} {j}")

#Slicing
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[2:5])
# a[m:n] --> return from index m to n, but exclude n
# 2 3 4
 
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#kosong di depan
print(a[:5])
print(a[0:5])
# 0 1 2 3 4
# a b c d e
 
#kosong di belakang
print(a[3:])
print(a[3:7]) #--> length of a = 7
# 3 4 5 6
# d e f g

