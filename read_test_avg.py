data = []
count = 0 
with open('reviews.txt', 'r') as log: 
	for test in log:
		data.append(test.strip())
		count += 1 # count = count + 1
		if count + 10000000 == 0:
			print(len(data))

x = print(len(data)) #印出清單資料
sum_len=0
for d in data:
	sum_len += len(d)
print(sum_len)
print('avg=', sum_len / len(d))

#print(x)
new = [] # 篩選程式
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', good, '筆資料')
print(good[0])