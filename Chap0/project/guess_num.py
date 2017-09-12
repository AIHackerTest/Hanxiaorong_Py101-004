print ("这是一个猜数字小游戏，欢迎你来尝试")

from random import randint
from sys import exit

target = randint(0,20)
max_count = 10

print ("请猜一个20以内的数字，做好准备，你将有 %d 次机会,请把握好！" % max_count)

i = 0
while i < 10:
	i += 1
	guess = int(input("请输入你的数字："))
	if guess == target:
		print ("恭喜你答对了，正确答案就是%d!" %target)
		exit(0)
	elif guess > target:
		print ("比正确答案大了")
	elif guess < target:
		print ("比正确答案小了")
	else:
		print ("您输入的不是数字，请重新输入")
	print ("你还有 %d 次机会可以使用" %(max_count -i))
print ("你已经花掉了所有的%d 次机会了，游戏结束！谢谢参与！" %max_count)