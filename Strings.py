Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1="ananad"
>>> s2="kumar"
>>> print(s1+s2)
ananadkumar
>>> print(s1+" "+s2)
ananad kumar
>>> print(len(s2))
5
>>> min(s2)
'a'
>>> max(s2)
'u'
>>> "k" in s2
True
>>> s1 is s2
False
>>> print(s1+"\t"+s2)
ananad	kumar
>>> s1=s2
>>> s1 is s2
True
>>> #python  list
>>> #python  list [mentions different varibles into single entity]
>>> #python  list[a list can be defined as a collection of values or items of different types.the items int he list are seperated with the comma(,) and enclosed with the square brackets[]
>>> l1[123,"venkatesh",'male","lead",34566.77]
   
SyntaxError: EOL while scanning string literal
>>> l1[123,"venkatesh","male","lead",34566.77]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l1[123,"venkatesh","male","lead",34566.77]
NameError: name 'l1' is not defined
>>> l1[123,"venkatesh","male","lead",34566.77]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l1[123,"venkatesh","male","lead",34566.77]
NameError: name 'l1' is not defined
>>> k1[123,"venkatesh","male","lead",34566.77]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    k1[123,"venkatesh","male","lead",34566.77]
NameError: name 'k1' is not defined
>>> k1=[123,"venkatesh","male","lead",34566.77]
>>> k1[3]
'lead'
>>> k1[0:4]
[123, 'venkatesh', 'male', 'lead']
>>> k1[ : ]
[123, 'venkatesh', 'male', 'lead', 34566.77]
>>> type(k1)
<class 'list'>
>>> id(k1)
2346151614656
>>> k1[3]="sr lead"
>>> k1
[123, 'venkatesh', 'male', 'sr lead', 34566.77]
>>> id(k1)
2346151614656
>>> #list is mutable
>>> #string is unmutable
>>> #we can modify data
>>> #we can delete data,and add
>>> #append means adding at last of list,insert adding at particular place
>>> #pop always delete element at last of list
>>> l1[23,34,45,56,67]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l1[23,34,45,56,67]
NameError: name 'l1' is not defined
>>> l1=[23,34,45,56,67]
>>> l1.append(12)
>>> l1
[23, 34, 45, 56, 67, 12]
>>> l1.insert(3,90)
>>> l1
[23, 34, 45, 90, 56, 67, 12]
>>> del l1[2]
>>> l1
[23, 34, 90, 56, 67, 12]
>>> l1.remove(34)
>>> l1
[23, 90, 56, 67, 12]
>>> l1.pop()
12
>>> l1.pop(90)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    l1.pop(90)
IndexError: pop index out of range
>>> l1.pop(2)
56
>>> #negative index
>>> l1=[12,23,34,45,56]
>>> l1[0:5]
[12, 23, 34, 45, 56]
>>> l1[0:4:2]
[12, 34]
>>> l1[-2:-4:1]
[]
>>> # string
>>> s="venkatesh"
>>> s[::-1]
'hsetaknev'
>>> s[::-2]
'heanv'
>>> # string reversal
>>> s="venkatesh"
>>> s[::-1]
'hsetaknev'
>>> 
>>> list
<class 'list'>
>>> #list
>>> l1=[14,23,34,45,43]
>>> l2=[98,67,67,98,75]
>>> print(l1+l2)
[14, 23, 34, 45, 43, 98, 67, 67, 98, 75]
>>> print(l1*3)
[14, 23, 34, 45, 43, 14, 23, 34, 45, 43, 14, 23, 34, 45, 43]
>>> min(l1)
14
>>> max(l1)
45
>>> sum(l1)
159
>>> sum(l1+l2)
564
>>> div(l1&l2)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    div(l1&l2)
NameError: name 'div' is not defined
>>> len(l1)
5
>>> 
