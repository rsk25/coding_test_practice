
def give_change(N: int) -> int:
	assert N // 10 == 0
	
	count = 0
	coin_types = [500, 100, 50, 10]
	
	for coin in coin_types:
		count += n // coin
		n %= coin
	return count

if __name__ == '__main__':
	