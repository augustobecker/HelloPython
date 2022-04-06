import sys

def ft_is_negative(nbr):
	if nbr < 0:
		print('N')
	else:
		print('P')

if __name__ == "__main__":
	ft_is_negative(int(sys.argv[1]))
