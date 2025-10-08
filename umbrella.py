import numpy as np
arr = np.full((8,5), '.')      
print(arr)  

#Create an umbrella shape by modifying array
#Top of umbrella a (row 0)

arr[0,0] = '.'
arr[0,1] = '.'
arr[0,2] = '%'
arr[0,3] = '.'
arr[0,4] = '.'

#Second row (row 1)
arr[1,0] = '.'
arr[1,1] = '%'
arr[1,2] = '.'
arr[1,3] = '%'
arr[1,4] = '.'

#Third row (row 2)
arr[2,0] = '%'
arr[2,1] = '.'
arr[2,2] = '.'
arr[2,3] = '.'
arr[2,4] = '%'

#Fourth row (row 3)
arr[3,0] = '%'
arr[3,1] = '%'
arr[3,2] = '%'
arr[3,3] = '%'
arr[3,4] = '%'



            