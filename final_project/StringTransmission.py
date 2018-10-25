# Name: String Transmission
# Course: CS 370
# Professor: Borowski
# Assignment: Final Project
# @file StringTransmission.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledges my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein
import os
import sys
from math import factorial, sqrt
import math



# Output T lines, one for each test case. Since the answers can be really big,
# output the numbers modulo 1000000007.
MOD = 1000000007
'''
	Pascals Rule
'''
def pascalRule(n, k):
	# Simple variable. Set answer equal to -1.
    ans = -1
    for i in range(0, k+1):
		# // is integer division in python3
        ans = ans + factorial(n) // ( factorial(i) * factorial(n-i) )
    return ans

def countZeroes(myStr, counter, strlen, divisor):
	# for j in range of the offset, n, and d, we check to see if
	# index at j is a 0 or not, and add to the counter.
	# else continue
	zeros = 0
	for j in range(counter, strlen, divisor):
		if myStr[j] == "0":
			zeros += 1
	return zeros

'''
	Definition: findDivisors
	Function: find all the divisors of n
'''
def findDivisors(n):
	# # Only go up to square root of n+1 because no factor of n
	# # will be bigger than that
	# # Start from 2 because 1 is already added
	# # Plus this is faster...
	divSet1 = [1]
	divSet2 = []
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			divSet1.append(i)
			if i * i != n:
				divSet2.append(n // i)
	divSet1.extend(divSet2[::-1])
	return divSet1

'''
For i in range of the number of test cases "T".
'''
def main():
	# get the input for the number of test cases, check that it is an int
	try:
		test_cases = int(input())
	except:
		print("Test cases must be an int")
		return

	for test_case_number in range(test_cases):

		# nk is the line input with n and k
		try:
			nk = input()
			# split nk on space, the first element will be n and the second k
			n = int(nk.split(" ")[0])
			k = int(nk.split(" ")[1])
		except:
			print("Something went wrong with the formatting, please check the instructions")
			return

		# the transimitted string
		try:
			s_trans = input()
		except:
			# might as well stick with the pattern.. but doubt would ever hit this
			print("something went wrong with the input")

		# if n == 1 then the only cases you have are 0 and 1 possible for k
		if n == 1:
			print(1 + k)
			continue

		# set the total to equal the pascalRule +1
		total = pascalRule(n, k)+1

		# set div to be equal to the divisors of N
		div = findDivisors(n)
		nkSum = (n + k + 1)

		# create a matrix of values in which the 0th value is multiplied by
		# (n+k+1) or the length of N transmitted by Alice, and k bits, plus 1, for i in range
		# of the length of the array of divisors and does it dynamically
		result = [[0]*(nkSum) for i in range(len(div))]

		# A value in order to designate whether or not the input value is, in fact,
		# a periodic value.
		isPeriodic = 0

		# scroll through the divisors list
		for i,d in enumerate(div):


			# set the first index of the ith value of each sub list in the matrix to 1
			result[i][0] = 1

			# for the offset in range of d, or element in the divisors list
			for offset in range(d):

				#count zeros in the string at indexes described by range(offset, n, d)
				zeros = countZeroes(s_trans, offset, n, d)

				# neat trick to get ones in the same fashion
				ones = n//d - zeros

				# previous value is simply the list value of the result at i.
				prev = list(result[i])

				# set result[i][and all the elements in each sub list] equal to
				# the 0th element multiplied by n+k+1
				# reinitialized to all 0's and then multiplied by the nkSum or the length
				# of the sublist
				result[i][:] = [0] * (nkSum)
				# print(result)
				# return
				# for k in the range of k+1, k being the number of possible errors
				# or inverted bits in the string
				for x in range(k+1):
					if prev[x]:

						# add k to the zeros counter
						k0 = x + zeros

						# add k to the ones counter
						k1= x + ones

						# set result at each respective kz or ko to the sum
						# of the result plus prev at k
						result[i][k0] = result[i][k0] + prev[x]
						result[i][k1] = result[i][k1] + prev[x]

			# if the first index of the ith element in the result,
			# set the isPeriodic equal to true.
			# a if condition else b
			isPeriodic = 1 if result[i][0] else isPeriodic

			# for z in range of i, set the divTemp variable equal to the value of the zth element
			# in the list of divisors found by the findDivisors function.
			for z in range(i):
				divTemp = div[z]

				# if the modulo of d and divTemp is equal to 0, iterate through k and adjust the result
				# matrix.
				if d % divTemp == 0:
					for k in range(k+1):
						result[i][k] = result[i][k] - result[z][k]

			# the total value is adjusted using the most updated result matrix, found by the
			# modulo of d and divTemp. This updates the total value and gives the final answer.
			for k in range(1, k+1):
				total = total - result[i][k]

		# print the total value
		print((total-isPeriodic) % MOD)

if __name__ =="__main__":
	main()
	# print(findDivisors(4))
