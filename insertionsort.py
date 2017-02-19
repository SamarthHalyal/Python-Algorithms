def insertionSort(arr):
	i = 0
	while i < len(arr):
		j = i
		while j > 0 and arr[j] < arr[j-1]:
			t = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] = t
			j -= 1
		#j loop end
		i += 1
	return arr
	#i loop end

print [1,3,2,6,4,5,9,7,8]
print insertionSort([1,3,2,6,4,5,9,7,8])
