data = []
count = 0 
with open('reviews.txt', 'r') as log: 
	for test in log:
		data.append(test.strip())
		count += 1 # count = count + 1
		if count + 100000 == 0:
			print(len(data))

x = print(len(data)) #印出清單資料
sum_len=0
for d in data:
	sum_len += len(d)
	print(sum_len)
print('avg=', sum_len / len(d))
#print(x)
