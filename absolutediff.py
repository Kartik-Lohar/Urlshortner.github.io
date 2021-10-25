def findMax(arr,start,end):
	max=arr[start]
	for i in range(start+1,end+1):
		if max < arr[i]:
			max=arr[i]
	return max

def findMin(arr,start,end):
	min=arr[start]
	for i in range(start+1,end+1):
		if min>arr[i]:
			min=arr[i]
	return min

def replaceArray(arr):
	tarr=[]
	l=len(arr)
	tarr.append(findMax(arr,1,l-1))
	for i in range(1,l-1):
		max=findMax(arr,i+1,l-1)
		min=findMin(arr,0,i-1)
		tarr.append(abs(max-min))
	tarr.append(findMin(arr,0,l-2))
	return tarr


arr=[1,5,2,4,3]
print(arr)
tarr=replaceArray(arr)
print(tarr)


time complexity --> O(n*n)
space complexity --> O(n)
