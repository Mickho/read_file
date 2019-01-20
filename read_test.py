data = []
with open('computer.txt', 'r') as log: 
	for test in log:
		data.append(test.strip())
print(data) #印出清單資料
print(len(data)) #印出有多少筆資料
print(data[0]) #印出第一筆資料
print('111111111111111')
print(data[1]) #印出第二筆資料