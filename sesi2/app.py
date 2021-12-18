# x = 10 - 15 --> tampil
x = 13
sunny = True
# sunny = False
# if x >= 10 and x <= 15 and sunny == False:
# if x >= 10 and x <= 15 and not sunny:
 
# if x >= 10 and x <= 15 and sunny == True:
if x >= 10 and x <= 15 and sunny:
    print(x)


total_purchase = 1000
# if 'a' in 'bar':
if 'aa' in 'bar':
    print('foo')
elif total_purchase >= 850:
    print('discount 30%')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

raining = False
print("Let's go to the", 'beach' if not raining else 'library')
# prin("a", "haaia")
 
# 'beach' if not raining else 'library'
# <expr1> if <conditional_expr> else <expr2>
# if not raining --> if raining == False
#                        False  == False ==> True ==> Beach // expr1
# output:
# Let's go to the


#Ternary if #1
# # raining = False # --> 'beach
raining = True    # --> library
print("Let's go to the", 'beach' if not raining else 'library')
# if not raining:
#     print("Let's go to the beach")
# else:
#     print("Let's go to the library")
# # prin("a", "haaia")
 
# # 'beach' if not raining else 'library'
# # <expr1> if <conditional_expr> else <expr2>
# # if not raining --> if raining == False
# #                        False  == False ==> True ==> Beach // expr1
# # output:
# # Let's go to the


#Ternary if #2
age = 12
s = 'teen' if age < 21 else 'adult'
# if age < 21:
#     s = 'teen'
# else:
#     s = 'adult'
print(s)
 
 



# # #Ternary if #3
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
 
# if ('qux' in ['foo', 'bar', 'baz']):
#     print('yes')
# else:
#     print('no')


# # #Ternary if #4
a = 1
b = 0
m = a if a > b else b
 
m = b
if a > b :
    m = a
 
m = 0
if a > b:
    m = a
else:
    m = b



n = 5
while n > 0: #5 4 3 2 1 0xxxx
    n -= 1 # n = n - 1  # 4 3 2 1 0
    print(n)    #4 3 2 1 0


i = 1
while i < 6: # 1 2 3 4 5 6xxxx
  print(i)   # 1 2 3 4 5
  i += 1     # 2 3 4 5 6


#break
i = -1
while i < 6:
    print(i)
    if i == 2:
        break
    i += 1
 
print('print yang di luar loop')


# continue
n = 5
while n > 0:       # 5 4 3 2 1 0
    n -= 1         # 4 3 2 1 0
    if n == 2:     # x x 2 x x
        continue   #     2
    print(n)       # 4 3 x 1 0
print('Loop ended.')


# while else
n = 5
while n > 0:       # 5 4 3 2 1 0xxx
    n -= 1         # 4 3 2 1 0
    print(n)       # 4 3 2 1 0
else:              #                [v] executed
    print('Loop done.')



#while else met with break
n = 5
while n > 0:        # 5 4 3
    n -= 1          # 4 3 2
    print(n)        # 4 3 2
    if n == 2:      # x x 2
        break       #     2terminates a loop entirely
else:               
    print('Loop done.')



d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d: # equals to d.keys()
    print(k)



d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():  # -->  (value1, value2)
                        #       'foo', 1
                        #       'bar', 2
                        #       'baz', 3
    print(k, ":", v)



# for k, v in d.items():
# for kunci, nilai d.items():



# x = range(5)
# x = range(1,5)
# x = range(2,20)
x = range(0,10, 4) # in java, php, c++ // for ( i=0, i<10; i+=4)
for n in x :
    print(n)
