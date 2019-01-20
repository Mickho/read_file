# Read file
data = [] #建立資料清單 
with open('autotest.txt', 'r') as log: #with: 當程式迴圈結束時 檔案讀取會自動結束
	for test in log:
		data.append(test.strip())#將Test 裡面的資料append到data資料清單 strip 取消斷行
print(data) #並且將資料清單的資料印出來
