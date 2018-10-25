
#Test Script for SubstringDivision.js
#We pledge our honor that we have abided by the Stevens Honor System.
#Zach Saegesser
#Aimal Wajihuddin
#Ryan Edelstein

import os

print("Output for 0123:\n")
print(str(os.system('java SubstringDivision 0123'))[:-1])
print("Output for 01234:\n")
print(str(os.system('java SubstringDivision 01234'))[:-1])
print("Output for 012355:\n")
print(str(os.system('java SubstringDivision 012355'))[:-1])
print("Output for 0123456:\n")
print(str(os.system('java SubstringDivision 0123456'))[:-1])
print("Output for 01234567:\n")
print(str(os.system('java SubstringDivision 01234567'))[:-1])
print("Output for 012345678:\n")
print(str(os.system('java SubstringDivision 012345678'))[:-1])
print("Output for 0123456789:\n")
print(str(os.system('java SubstringDivision 0123456789'))[:-1])

