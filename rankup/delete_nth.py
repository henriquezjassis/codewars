#!/bin/python3
def count_array_element(array, number): # Already exists a function for that that is List.count(element)
	count = 0

	for i in array:
		if(i == number):
			count += 1
	
	return count


def delete_nth(order,max_e):
	aux = list()

	for i in order:
		if(count_array_element(aux, i) < max_e):
			aux.append(i)

	return aux;


lista = delete_nth([20,37,20,21], 1)

print(lista)