def ft_print_comb():
	num1 = 0
	
	while (num1 <= 7):
		num2 = num1 + 1
		while (num2 <= 8):
			num3 = num2 + 1
			while (num3 <= 9):
				print("%d%d%d" % (num1, num2, num3), end = '')
				if (num1 != 7 or num2 != 8 or num3 != 9):
					print(", ", end = '')
				else:
					print()
				num3 = num3 + 1
			num2 = num2 + 1	
		num1   = num1 + 1

if __name__ == "__main__":
	ft_print_comb()
