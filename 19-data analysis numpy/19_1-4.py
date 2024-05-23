import numpy as np

#### intro
list1 = [1,2,3,4,5,6,7,8,9]
np_array = np.array(list1)              # 1D array

list2 = [[1,2,3],[4,5,6],[7,8,9]]
np_multi_array = np_array.reshape(3,3)  # 3D array 3x3 matrix


dimension = np_array.ndim               # array dimension
# print(dimension)                      # -> 1
# print(np_multi_array.ndim)            # -> 2


shape = np_array.shape                  # array shape
# print(shape)
shape = np_multi_array.shape
# print(shape)


#### methods
result = np.arange(1,10)                # make array from range (exclude last bound)
result = np.arange(10,100,3)            # make array from range with step size
result = np.zeros(10)                   # make zero array with 10 elements
result = np.ones(10)                    # make ones array with 10 elements
result = np.linspace(0,100,5)           # slice 0 , 100 in  5 equal plces
result = np.linspace(0,5,5)             # make array from range grouping
result = np.random.randint(0,7)         # return a random int exclude last bound
result = np.random.randint(7)           # same as randint(0,7)
result = np.random.randint(0,10,5)      # return an array of 5 rnd number ex:[1,5,9,2,1]
result = np.random.rand()               # return a random number between [0 -> 1]
result = np.random.rand(5)              # return an array of x random number between [0 -> 1]
result = np.random.randn(5)             # return an array of x random number between [0 -> 1] include negative numbers
np_array = np.arange(50)                # araay 0 -> 50
np_multi = np_array.reshape(5,10)       # reshape the array 5x10

result = np_multi.sum(axis=1)
result = np_multi.sum(axis=0)

rand_array = np.random.randint(0,100,10)
result = rand_array.max()               # return max
result = rand_array.min()               # return min
result = rand_array.mean()              # return mean
result = rand_array.argmax()            # the index of max
result = rand_array.argmax()            # the index of min
# print(result)

#### indexing
numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]     # get number in index [x]
result = numbers[-1]    # get last element
result = numbers[0:3]   # get number between index [x:y] [0,5,10] exclude last index always
result = numbers[:3]    # same as [0:3]
result = numbers[3:]    # same as [3:last]
result = numbers[::]    # all the list
result = numbers[::2]   # step size go 2 2 
result = numbers[::-1]   # reverse the array, go back 1 1 from the end
result = numbers[::-2]   # reverse the array, go back 2 2 from the end

numbers = np.array([[0,5,10],[15,20,25],[50,75,100]]) # 3x3 matrix
# print(numbers)
result = numbers[0]         # first elemnt  (row)
result = numbers[2]         # second elemnt  (row)
result = numbers[0,2]       # 1 row , 3 col ,same as nmbers[0][2]
result = numbers[2,1]       # 1 row , 3 col ,same as nmbers[0][2]
result = numbers[:,:]       # all rows and cols [row : to row , col : to col ]
result = numbers[0:1,:]     # row 1 col all
result = numbers[1:2,:]     # row 2 col all
result = numbers[:2,:2]     # row 2 col 2
result = numbers[:,1]       # row all , col 2
result = numbers[2,:]       # row 2 , col all
result = numbers[-1,:]      # last row all col
result = numbers[:2,:2]     #  2x2 matrix from 0 0
result = numbers[:1,:1]     #  1x1 matrix from 0 0

#### referance & coppy
arr = np.arange(0,10)
arr2 = arr                  # referance
# print(id(arr),id(arr2))   # address 2526327599152

# arr2[2] = 100             # changing arr through arr2
# print(arr , arr2)         # el[2] been changed in both arrys

arr2 = arr.copy()           # copy arr to arr2 different address 
arr2 [1] = 100
# print(arr , arr2)         # arr2 been changed but not arr



#### array operations
arr = np.random.randint(10,100,6)
arr2 = np.random.randint(10,100,6)
# print(arr)
# print(arr2)

result = arr + arr2         # sum 2 arrays(matrices), works with multi dimensions too
result = arr + 10           # add 10 to all the elements in the matrix
result = arr - arr2         # sub arr from arr2
result = arr - 10           # sub 10  from arr
result = arr * arr2         # mul arr by arr2
result = arr * 10           # mul arr by 10
result = arr / arr2         # div arr on arr2
result = arr / 10           # div arr on 10
result = np.sin(arr)        # get sin of arr
result = np.cos(arr)        # get com of arr
result = np.sqrt(arr)       # get sqrt of arr
result = np.log(arr)        # get log of arr         

arr = arr.reshape(2,3)      # make the amtrices 3x3
arr2 = arr2.reshape(2,3)    # make the amtrices 3x3
print(arr)
# print(arr2)

result = np.vstack((arr , arr2))    # stack matrices vertically
result = np.hstack((arr , arr2))    # stack matrices horizontally
result = arr > 50                   # chek all elements in the arr if they match the condition -> true false false ...
result = arr % 2 == 0               # check if the elentas are even numbers
result = arr[result]                # boolen indexing (it flattens both arr and the boolean array result, then it picks only those elements from arr that correspond to True in the boolean array.)
print(result)