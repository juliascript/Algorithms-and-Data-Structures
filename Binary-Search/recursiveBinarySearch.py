import math

array = [0, 3, 4, 5, 6, 15, 18, 22, 25, 27, 31, 33, 34, 35, 37, 42, 53, 60]

def binarySearch(array, number):
	middleIndexOfArray = int(math.floor(len(array) / 2))
	if middleIndexOfArray == 0:
		return False

	if array[middleIndexOfArray] == number:
		return True
	elif array[middleIndexOfArray] > number:
		return binarySearch(array[:middleIndexOfArray], number)
	elif array[middleIndexOfArray] < number:
		return binarySearch(array[middleIndexOfArray:], number)

_bool = binarySearch(array, 47)
print _bool