state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


# def add_round_key(s, k):
#     A = sum(s, [])
#     B = sum(k, [])

#     result = [x^y for (x,y) in zip(A, B)] 
    
#     flag = ''.join(chr(z) for z in result)

#     return flag

def add_round_key(s, k):
	s = sum(s, [])
	k = sum(k, [])
	for i in range(len(s)):
		s[i] = s[i] ^ k[i]
	return bytes(s).decode()
	
print(add_round_key(state, round_key))