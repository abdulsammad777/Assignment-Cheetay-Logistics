
def candyStore(arr, N, K):
	if N == 1:
		return candies[0]
	min, max = 0, 0
	i = 0
	j = N-1

	while(i <= j):

		min += arr[i]
		i += 1
		j = j - K

	i = 0
	j = N - 1
	while (j >= i):
		max += arr[j]

		i = i + K
		j -= 1


	print(min, max)

"""List sort method by default an implementation of Timesort that takes O(n * log n)"""
# candies.sort()
"""We can also apply quick sort to achieve O(n * log n) complexity"""
# quick sort

def QuickSort(candies,start,end):
	if start<end:
		PIndex=Partition(candies,start,end)
		QuickSort(candies,start,PIndex-1)
		QuickSort(candies,PIndex+1,end)
def Partition(candies,start,end):
	PIndex= start
	pivot=candies[end]
	for i in range(start,end):
		if candies[i] <= pivot:
			candies[i],candies[PIndex] = candies[PIndex],candies[i]
			PIndex +=1
	candies[PIndex],candies[end]=candies[end],candies[PIndex]
	return PIndex


candies = [3, 2, 1, 4, 5]

QuickSort(candies, 0,len(candies)-1)
N = len(candies)
K = 4
candyStore(candies, N, K)































# Python implementation
# to find the minimum
# and maximum amount

# Function to find
# the minimum amount
# to buy all candies
#
#
# def findMinimum(arr, n, k):
#
# 	res = 0
# 	i = 0
# 	while(n):
#
# 		# Buy current candy
# 		res += arr[i]
#
# 		# And take k
# 		# candies for free
# 		# from the last
# 		n = n-k
# 		i += 1
# 	return res
#
# # Function to find
# # the maximum amount
# # to buy all candies
#
#
# def findMaximum(arr, n, k):
#
# 	res = 0
# 	index = 0
# 	i = n-1
# 	while(i >= index):
#
# 		# Buy candy with
# 		# maximum amount
# 		res += arr[i]
#
# 		# And get k candies
# 		# for free from
# 		# the starting
# 		index += k
# 		i -= 1
#
# 	return res
#
# # Driver code
# arr = [3, 2, 1, 4, 5, 8]
#
# candies = arr
# N = len(candies)
# k = 2
#
# """List sort method by default an implementation of Timesort that takes O(n * logn)"""
# candies.sort()
#
# # Function call
# print(findMinimum(candies, N, k), " ",
# 	  findMaximum(candies, N, k))
#
