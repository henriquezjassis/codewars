def count_bits(n):
    list_bits = list(f"{n:b}") # transform number in list
    count = 0

    # See if the number is equal a 1 and increment
    for i in list_bits:
    	if int(i,10) == 1:
    		count += 1
    

    return count



count_bits(1521)