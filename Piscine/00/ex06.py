def ft_print_comb2():
	num1 = 0
	num2 = 0
	while (num1 <= 98):
		num2 = num1 + 1
		while (num2 <= 99):
			if (num1 < 10):
				print("0%d" % num1, end=" ")
			elif (num1 != 98):
				print("%d" % num1, end=" ")
			if (num2 < 10):
				print("0%d" % num2, end=", ")
			elif (num1 != 98):
				print("%d" % num2, end=", ")
			else:
				print("98 99", end="")
			num2 = num2 + 1
		num1 = num1 + 1

if __name__ == "__main__":
	ft_print_comb2()
