import random

start = int(input('請輸入隨機整數開始值：'))

end = int(input('請輸入隨機整數結束值：'))

r = random.randint(start ,end)
count = 0

while True:
	count += 1
	num = int(input('\n請輸入' + str(start) +' - ' + str(end) + '間的整數：'))
	if num == r:
		print('\n恭喜猜對了！')
		print('你總共猜了', count, '次！')
		break
	elif num > r:
		print('比答案大，再猜吧！')
	elif num < r:
		print('比答案小，再猜吧！')
	print('這是你猜的第', count, '次！')
