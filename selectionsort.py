def selectionSort(arr):
	i = 0
	while i < len(arr):
		j = i
		k = i + 1
		while k < len(arr):
			if arr[k] < arr[j]:
				j = k
			#if end
			k += 1
		#k for loop
		t = arr[i]
		arr[i] = arr[j]
		arr[j] = t
		i += 1
	return arr
	#i for loop

print [1,3,2,6,4,5,9,7,8]
print selectionSort([1,3,2,6,4,5,9,7,8])
