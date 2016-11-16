import math

array = [0, 3, 4, 5, 6, 15, 18, 22, 25, 27, 31, 33, 34, 35, 37, 42, 53, 60]

def binarySearch(array, number):
	lowerBound = 0
	upperBound = len(array)

	while lowerBound < upperBound:
		middleIndex = int(math.floor(lowerBound + (upperBound - lowerBound) / 2))
		if array[middleIndex] == number:
			return True
		elif array[middleIndex] < number:
			lowerBound += 1
		elif array[middleIndex] > number:
			upperBound = middleIndex
	return False

_bool = binarySearch(array, 22)
print _bool