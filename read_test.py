data = []
with open('computer.txt', 'r') as log: 
	for test in log:
		data.append(test.strip())
print(data)
