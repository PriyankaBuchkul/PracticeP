""" Write a function which takes input as a list of elements
and merge all strings seperated by '#' and add all numbers. Handle exceptions
"""
input_list =["Hello",4,"i",6,"know","Python","2",7]

total=0

s1=[]

for i in input_list:
      try:
            if type(i)==str:
                  s1.append(i)
            else:
                  total=total+i
      except Exception as e:
            print(e)

l1="#".join(s1)
print(l1)
print("total",total)

