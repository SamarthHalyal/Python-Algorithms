def quickSort(arr,lo,hi): # main quicksort function
	if lo < hi:
		p = partition(arr,lo,hi)
		quickSort(arr,lo,p-1)
		quickSort(arr,p+1,hi)
	return arr

def partition(arr,lo,hi): #partition function helps to get divisions
	pivot = arr[hi]
	i = lo - 1
	j = lo
	while j <= (hi - 1):
		if arr[j] <= pivot:
			i += 1
			t = arr[i]
			arr[i] = arr[j]
			arr[j] = t
		j += 1
		#if end
	#while loop end
	t = arr[i+1]
	arr[i+1] = arr[hi]
	arr[hi] = t
	return (i + 1)

a = [1,3,2,6,4,5,9,7,8]
print a
print quickSort(a,0,(len(a)-1))
