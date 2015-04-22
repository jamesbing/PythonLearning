"""

the default values are evaluated at the point of function definition
in the defining scope
the default value is evaluated only once

"""
i = 5

def f(arg=i):
 print arg

i = 6
i
f()
i

#this code segment above will print:
6
5
6


"""

heres another example, this following code segement will produce a resutlt as following:
[1]
[1,2]
[1,2,3]


"""

def f(a,L=[]):
 L.append(a)
 return L

print f(1)
print f(2)
print f(3)

#what if you add a print thing inside that function?
