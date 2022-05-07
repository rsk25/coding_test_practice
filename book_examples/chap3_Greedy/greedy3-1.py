import sys

def give_change(N: int) -> int:
	assert N % 10 == 0
	
	count = 0
	coin_types = [500, 100, 50, 10]
	
	for coin in coin_types:
		count += N // coin
		N %= coin
	return count

if __name__ == '__main__':
	change = give_change(int(sys.argv[1]))
	print(change)