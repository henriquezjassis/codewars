#!/bin/python3

def descending_order(num):
	listNum = list(str(num)) 
	listNum.sort(reverse=True)
	return int("".join(listNum))

print(descending_order(123))