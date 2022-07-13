'''
#nested if condition
#user id = venkatesh and pw =56789
uid=input("enter a user name:")
if(uid=="venkatesh"):
    print("valid user name")
    pw=int(input("enetr password:"))
    if(pw==56789):
        print("vali password")
    else:
        print("invalid password")

else:
    print("invalid user id")
'''
'''
l1=[23,556,45,78,69]
for i in l1:
    print(l1)
'''
'''  
l1=[23,556,45,78,69]
#print(sum(l1))
s=0
for i in l1:
      s=s+1
print("sum :",s)
'''
'''
l1=[23,556,45,78,69]
sr=int(input("enter a number to search:"))
if(sr in l1):
    print ("%s is found"%sr)
else:
    print("%s is not found"%sr)
'''
'''

l1=[23,556,45,78,69]
sr=int(input("enter a number to search:"))
for i in l1:
    if(i==sr):
        search=True
        
if(search==True):
    print ("%s is found"%sr)
else:
    print("%s is not found"%sr)
'''
'''
name="venkatesh"
sr=int(input("enter a letter to search:"))
for i in name:
    if(i==sr):
        search=True
        
if(search==True):
    print ("%s is found"%sr)
else:
    print("%s is not found"%sr)
'''
'''
n=int(input("enter a number;"))
for i in range (1,n+1):
    print(i)
'''

n=int (input("enter a number:"))
f=1
for i in range(1,n+1):
    f=f+i
print("factorial :",f)





























    
