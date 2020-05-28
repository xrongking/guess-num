import random

x = input('請輸入隨機整數下限值：')
x = int(x)
y = input('請輸入隨機整數上限值：')
y = int(y)

r = random.randint(x ,y)
count = 0

while True:
	count = count + 1
	num = int(input('請輸入' + str(x) +' - ' + str(y) + '間的整數：'))
	if num == r:
		print('恭喜猜對了！')
		print('你總共猜了', count, '次')
		break
	elif num > r:
		print('比答案大，再猜吧！')
	elif num < r:
		print('比答案小，再猜吧！')
