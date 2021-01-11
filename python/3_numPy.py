# NumPy is a Python library used for working with arrays.
# NumPy stands for Numerical Python.

import numpy as np


# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))
# # array in numpy is called ndarray


# # DIMENSIONS
# # 0-D array
# arr0 = np.array(1)
# print(arr0)
# # 1-D array
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)
# # 2-D array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)
# # 3-D array
# arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3)
# # check how many dimensions : ndim attribute
# print(arr0.ndim)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
# # When array created, you can define the number of dimension with ndim argument
# arr5 = np.array([1, 2, 3], ndmin=5)
# print(arr5)
# print(arr5.ndim)


# # ARRAY INDEXING
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1[0])
# print(arr1[4])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2[0][1])
# print(arr2[0, 0])


# ARRAY SLICING
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1[1:2])
# print(arr1[0:7])
# print(arr1[0::2])
# print(arr1[-3:-1])


# # COPY AND VIEW
# # The copy owns the data and any changes made to the copy will not affect original array,
# # and any changes made to the original array will not affect the copy.
# # The view does not own the data and any changes made to the view will affect the original array,
# # and any changes made to the original array will affect the view.
# arr = np.array([1, 2, 3, 4, 5])
# arrCopy = arr.copy()
# arr[0] = 12
# print(arr)
# print(arrCopy)
# arrView = arr.view()
# arr[0] = 15
# print(arr)
# print(arrView)
# arrView[0] = 1
# print(arr)
# print(arrView)
# # Check an array owns it's data or not:
# print(arr.base)
# print(arrCopy.base)
# print(arrView.base)


# # ARRAY SHAPE
# arr1 = np.array([1, 2, 3, 4, 5, 6])
# arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr1.shape)
# print(arr2.shape)
# newArr = arr1.reshape(3,2)
# print(newArr)
# print(arr1)


# # ARRAY ITERAING
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#     print(x)
# arr = np.array([1, 2, 3, 4, 5])
# for index, x in np.ndenumerate(arr):
#     print(index, x)


# ARRAY SEARCH
arr = np.array([1, 2, 3, 4, 5])
x = np.where(arr == 2)
y = np.where(arr % 2 == 1)
# the return is index, not the value
print(x)
print(y)
