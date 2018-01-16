#!/usr/bin/python
import sys

string = sys.argv[1]
max_lenght = len(string)
encoded = 'eval(String.fromCharCode('

a = 1
for x in string:
	encoded += str(ord(x))
	
	if a < max_lenght:
		encoded += ', '
		a += 1

encoded += '));'
print encoded	
