def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    input_array.sort()
    while (low <= high):
	    mid = (low + high) / 2
	    if (input_array[mid] == value):
		    return value
	    elif (input_array[mid] < value):
		    low = mid + 1
	    else:
		    high = mid - 1
    return -1

test_list = [1,9,3,11,15,19,29]
test_val1 = 25
test_val2 = 15

print binary_search(test_list, test_val1)
# 25 not found, returns - 1

print binary_search(test_list, test_val2)
# returns 15
