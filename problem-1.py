# multiples of 3 or 5

sum3_list = []
sum5_list = []

i = 1
while 3 * i < 1000:a
	sum3_list.append(3*i)
	i += 1

n = 1
while 5 * n < 1000:
	sum5_list.append(5*n)
	n += 1

sum_list = list(sum3_list)
sum_list.extend(x for x in sum5_list if x not in sum_list)
print(sum(sum_list))
