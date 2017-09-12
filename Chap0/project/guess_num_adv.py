print("欢迎来到猜数字游戏，请猜测一个四位数，首位不含零且每位数字不想等，你有10次机会，请好好把握")
print("准备好了吗？Let's go!")
import random
from sys import exit
import math

digit_list = random.sample(range(10),4)
target = "".join(str(x)for x in digit_list)

max_count = 10

for i in range(max_count):
	while True:
		try:
			guess_str = input("请输入你的数字：")
			guess = int(guess_str)
			log_val = math.log10(guess)
			if 4 <= log_val or log_val <=0:
				raise ValueError
			guess_digit_list = [int(x) for x in guess_str]
			if len(guess_digit_list) !=4:
				raise ValueError
			break
			
		except ValueError:
			print("请确保你输入的是四个数字！")
			continue
			
	a_count = 0
	b_count = 0
	for j in range(4):
		if guess_digit_list[j] == digit_list:
			# 判断数字正确且位置正确的个数
			a_count += 1
		elif guess_digit_list[j] in digit_list:
			# 判断数字正确但位置错误的个数
			b_count += 1
		else:
			continue
	if a_count == 4:
		print("恭喜你答对了，正确答案就是%d!" %target)
		exit()
	else:
		print("您本次猜测的结果是%d A %d B" %(a_count,b_count))
		print("您还有%d 次机会可以输入" %(max_count - i -1))
print("抱歉，您已经用掉了所有的%d 次机会了，游戏结束，谢谢参与" % max_count)