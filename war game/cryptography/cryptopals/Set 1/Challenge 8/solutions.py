def count_repetitions(ciphertext, block_size):
	chucks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
	number_of_repetitions = len(chucks) - len(set(chucks))
	result = {
		'ciphertext': ciphertext,
		'repetitions': number_of_repetitions
	}

	return result

ciphertext = [bytes.fromhex(line.strip()) for line in open('8.txt')]
block_size = 16
repetitions = [count_repetitions(cipher, block_size) for cipher in ciphertext]
most_repetitions = sorted(repetitions, key=lambda x: x['repetitions'], reverse=True)[0]

print('Ciphertext: {}'.format(most_repetitions['ciphertext']))
print('Repeating Blocks: {}'.format(most_repetitions['repetitions']))
