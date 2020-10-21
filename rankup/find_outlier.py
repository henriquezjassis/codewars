#!/bin/python3

def find_outlier(integers):
	odd = [];
	even = [];
	for i in integers:
		if(i % 2 == 0):
			even.append(i)
		else:
			odd.append(i)

	if(len(odd) == 1):
		return odd[0]
	else:
		return even[0]

x = find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
print(x)