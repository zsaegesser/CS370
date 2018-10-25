# Name: Sam and Sub Strings
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 7
# @file trip.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledge my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

def findBestTrip(aliceTrip, bobTrip, dic):
	# If either Alice or Trip have run out of cities in their trip, return
	# No more calculation in this branch
	if aliceTrip == '' or bobTrip == '':
		return [0, {""}]
	
	# If we have already calculated this set of input's result, get result from dictionary
	elif (aliceTrip, bobTrip) in dic:
		return dic[(aliceTrip, bobTrip)]
	
	# If we have a common city in this path
	elif aliceTrip[0] == bobTrip[0]:
		# Use it or Lose it approach
		# Find calculation for if both lose this city
		bothCompromise = findBestTrip(aliceTrip[1:], bobTrip[1:], dic)
		# Use this list as a result builder
		# First element represents length of maximum length substring
		# Second element represents all of the substrings found of that length (in its final iteration)
		resultBuilder = [0,{''}]

		# Only keep results that have been added to as compared to before in this new result
		# Add the next potential city to all of the new paths generated by bothCompromise
		filtered = list(filter(lambda x: len(x) == bothCompromise[0], bothCompromise[1]))
		for index, val in enumerate(filtered):
			filtered[index] = aliceTrip[0] + val

		# Add 1 to the number that represents the length of longest substring we have found
		resultBuilder[0] = 1 + bothCompromise[0]
		# Make the result the set of the filtered output calculated above
		resultBuilder[1] = set(filtered)

		# Add current calculated result to dictionary and return the result
		dic[(aliceTrip, bobTrip)] = resultBuilder
		return resultBuilder
	
	else:
		# Standard Use it or Lose it approach
		# Calculate Losing A, Losing B, and union of both losing
		# This is done to make things easier later on
		# Result builder using same logic as above
		aliceCompromises = findBestTrip(aliceTrip[1:], bobTrip, dic)
		bobCompromises = findBestTrip(aliceTrip, bobTrip[1:], dic)
		compromiseUnion = aliceCompromises[1].union(bobCompromises[1])
		resultBuilder = [0,{''}]

		# Set the result builder's first element to the maximum found from alice's compromise and bob's compromise 
		# (alice's lose it and bob's lose it)
		# Get all elements from compromiseUnion that are of the max length
		# Whether they be from alice's compromise or bob's compromise doesn't matter
		# As long as they are the max length found
		resultBuilder[0] = max(aliceCompromises[0], bobCompromises[0])
		resultBuilder[1] = set(filter(lambda x: len(x) == resultBuilder[0], compromiseUnion))

		# Add current calculated result to dictionary and return the result
		dic[(aliceTrip, bobTrip)] = resultBuilder
		return resultBuilder


if __name__ == '__main__':
	# Get number of cases to run 
	testCases = int(input())
	for _ in range(testCases):
		# Get input for alice's and bob's proposed trips in this test case
		aliceTrip = input()
		bobTrip = input()

		# Get answer and the resultant trips of that max length
		answer = findBestTrip(aliceTrip, bobTrip, {})
		result = sorted(answer[1])

		# Print out the resultant trips that we found
		for val in result:
			print(val)