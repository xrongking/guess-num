import random

r = random.randint(1 ,100)
count = 0

while True:
	count = count + 1
	num = input('請輸入1 - 100間的整數：')
	num = int(num)
	if num == r:
		print('恭喜猜對了！')
		print('你總共猜了', count, '次')
		break
	elif num > r:
		print('比答案大，再猜吧！')
	elif num < r:
		print('比答案小，再猜吧！')
