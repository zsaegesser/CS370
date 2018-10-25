from subprocess import Popen, PIPE, STDOUT

file = open("testcases.txt", "r")
str = file.read()
strArr = str.split("\nBREAK\n")

#Test 1
print "------------ Test 1 ------------"
print "Expected:"
print "1"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[0])[0]
print out.decode()

#Test 2
print "------------ Test 2 ------------"
print "Expected:"
print "1\n2"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[1])[0]
print out.decode()


#Test 3
print "------------ Test 3 ------------"
print "Expected:"
print "0"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[2])[0]
print out.decode()


#Test 4
print "------------ Test 4 ------------"
print "Expected:"
print "1\n2"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[3])[0]
print out.decode()


#Test 5
print "------------ Test 5 ------------"
print "Expected:"
print "1"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[4])[0]
print out.decode()


#Test 6
print "------------ Test 6 ------------"
print "Expected:"
print "1"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[5])[0]
print out.decode()


#Test 7
print "------------ Test 7 ------------"
print "Expected:"
print "1\n2"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[6])[0]
print out.decode()

#Test 8
print "------------ Test 8 ------------"
print "Expected:"
print "0\n1"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[7])[0]
print out.decode()

#Test 9
print "------------ Test 9 ------------"
print "Expected:"
print "0\n0\n1"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[8])[0]
print out.decode()

#Test 10
print "------------ Test 10 ------------"
print "Expected:"
print "0\n0"
print "Actual:"
p = Popen('./contacts', stdout=PIPE, stdin=PIPE, stderr=STDOUT)
out = p.communicate(input= strArr[9])[0]
print out.decode()