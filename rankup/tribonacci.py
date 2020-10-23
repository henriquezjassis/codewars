#!/bin/python3

def tribonacci(signature, n):
	aux = signature

	if n < 1:
		return []

	elif n < 4:
		return signature[:n]
	else:
		for i in range(3,n,1):
			x = aux[i-1] + aux[i-2] + aux[i-3]
			aux.append(x)
		return aux
