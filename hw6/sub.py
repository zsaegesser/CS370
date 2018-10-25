# Name: Sam and Sub Strings
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 6
# @file substrings.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledge my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

def substrings(myStr):
	modNum = 1000000007			# The mod number that we're given in the problem
	total = 0					# What will eventually be the total that we return
	strLen=len(myStr)			# The length of the input
	one = 1

	# For however long the string is
	for i in range(strLen):

		# Algorithm is deatiled as follows:
		#	Set total equal to the total plus the index of the string -1,
		#	Multiply by one index further and multiply by the new value of "one"
		#	Follow by modding it
		
		total = (total + int(myStr[strLen - (i + 1 )]) * (strLen - i) * one) % modNum
		one  = ((one * 10) + 1) % modNum

		# Set 'one' to be 1, 11, 111... and so on dependent upon how large "s" is
		# This is because x*1 + x*10 + x*100 is equal to x*1111
		# Results in easier to read code 

	return total

if __name__ == '__main__':
	balls = input().strip()
	result = substrings(balls)
	print(result)