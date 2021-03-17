'''
	x ≡ 2 mod 5
	x ≡ 3 mod 11
	x ≡ 5 mod 17

	find a => x ≡ a mod 935
'''

from Crypto.Util.number import inverse

a1, a2, a3 = 2, 3, 5
m1, m2, m3 = 5, 11, 17

M = m1 * m2 * m3
M1 = int(M / m1)
M2 = int(M / m2)
M3 = int(M / m3)

y1 = inverse(M1, m1)
y2 = inverse(M2, m2)
y3 = inverse(M3, m3)

a = a1*M1*y1 + a2*M2*y2 + a3*M3*y3

result = a % M

print(result)