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
print(tuple(result))'''

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