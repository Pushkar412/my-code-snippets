from array import array
from ast import comprehension

array = [1,5,2,9,3]
square_array = array[i * i for i in array] 
multiply_by_5 = [i *5 for i in array]

arr = [19,34,32,16,89,903,43,45,83,92]
for i in range (len(arr)):
    arr[i] % 2 != 0:
    arr[i] = 2 * arr[i]
print(arr)


--Using List comprehension
arr = [19,34,32,16,89,903,43,45,83,92]
new_arr = [[x, 'odd'] if x % 2 !=0 else [x, even] for x in arr]

arr = [19,34,32,16,89,903,43,45,83,92]
new_arr = [[x, 'odd'] if x % 2 !=0 else [x, even] for x in arr] 

name = 'united states of america'
name.split()
