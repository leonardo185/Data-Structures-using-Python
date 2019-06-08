"""
    Implementation of arrays in Python.
"""
import array as arr
a = arr.array('d', [1, 3, 4])

#Print array elements:
for i in a:
    print(i)
print("")

#Access Array elements:
print(a[0])
print(a[1])
print("")

#Slicing Arrays:
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
for i in numbers_array:
    print(i)
print("")

  #Prints elements from start_index to end_index - 1.
print(numbers_array[2:5])
print(numbers_array[:-5])
print(numbers_array[5:])
print(numbers_array[:])

#Changing or adding elements in array:
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

    # changing first element
numbers[0] = 0
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])

    # changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])



#Appending Elements:
    #append
numbers.append(4)
print(numbers)     # Output: array('i', [1, 2, 3, 4])

    # extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

#Remove or Delete elements:
del number[2] # removing third element
print(number) # Output: array('i', [1, 2, 3, 4])

del number # deleting entire array
print(number) # Error: array is not defined

numbers = arr.array('i', [10, 11, 12, 12, 13])

numbers.remove(12)
print(numbers)   # Output: array('i', [10, 11, 12, 13])

print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])
