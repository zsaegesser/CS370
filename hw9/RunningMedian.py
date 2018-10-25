# Name: Find the Running Median
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 9
# @file RunningMedian.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledges my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

from heapq import heappush, heappop

def main(nums):
	'''
	This is the main function of this file. It iterates over
	however many times we have to (N) and inserts, gets the median,
	and prints the value N times.
	'''
	median = 0
	for i in range(nums):		#for N inputs
		num = int(input())		#get the new input
		insert(num, median)		#insert the new number
		median = findMedian()	#find the median
		print(median)			#print the median

def insert(num, median):
	'''
	The purpose of this function is to add the number
	given by the user and add it to its respective heap,
	and then to balance the heaps if one gets too large
	'''
	#if the number is bigger than the current median
	#then add it to the maxHeap
	if num > median:
		heappush(maxHeap, num)
	#else, add it to the minHeap
	else:
		heappush(minHeap, -num)

	#If minHeap is more than 1 element bigger
	#than maxHeap than balance the heaps
	if len(minHeap) > len(maxHeap) + 1:
		heappush(maxHeap, -heappop(minHeap))
	#Vice versa, if maxHeap is more than 1 element
	#bigger than minHeap, balance the heaps
	if len(maxHeap) > len(minHeap) + 1:
		heappush(minHeap, -heappop(maxHeap))

def findMedian():
	'''
	The purpose of this function is to find the median
	after we have added the new number to its respective
	heap
	'''
	#If minHeap has one more value than maxHeap,
	#that extra value is the median. Obtain it 
	#and return it so that it may be printed
	if len(minHeap) == len(maxHeap) + 1:
		medianVal = -heappop(minHeap)
		heappush(minHeap, -medianVal)
		median = float(medianVal)
	#Vice versa, in maxHeap has one more value
	#than minHeap, that one extra value is the 
	#median. Obtain it and return so that it
	#may be printed
	elif len(minHeap) + 1 == len(maxHeap):
		medianVal = heappop(maxHeap)
		heappush(maxHeap, medianVal)
		median = float(medianVal)
	#If they both have equal lengths, get the 
	#values from both of the heaps, calcualte
	#the median, and put the values back. 
	else:
		minMedian = -heappop(minHeap)
		heappush(minHeap, -minMedian)
		maxMedian = heappop(maxHeap)
		heappush(maxHeap, maxMedian)
		median = (minMedian + maxMedian) / float(2)
	return median

if __name__ == '__main__':
	NUMS = int(input())
	minHeap = []
	maxHeap = []
	main(NUMS)