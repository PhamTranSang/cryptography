p = 29
int = [14, 6, 11] # chỉ có 6 là số squadratic Residues 

# tìm căn bậc 2
for x in range(p):
	if(pow(x, 2, 29) == 6):
		print(x)