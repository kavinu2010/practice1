'''base=int(input('enter base eleement'))
exponent=int(input('enter exponent element'))
print(base,exponent)
result=1
for _ in range(exponent):
  result=result*base
print(result)


tup=(1,3,5,6,7)
print(sum(tup))


tup=(1,3,5,6,7,8,4,2)
result=[ i for i in tup if(i%2==0)]
print(tuple(result))

dict1={
  'key1':'one',
  'key2':'two',
  'key3':'onee',
  'key4':'two0'
}

dict2={
  'keyss1':'one',
  'keyss2':'two',
  'key33':'onee',
  'key4':'twre'
}

print({**dict1,**dict2})

list=[]
while(True):
 user_input=input('enter the value of type exist >>')
 if(user_input=='exist'):
  break
 else:
  list.append(int(user_input))
print(list)

even=[even for even in list if(even%2==0)]
print(even)


user_input=input('enter any string >> ')
print(user_input[::-1])'''

