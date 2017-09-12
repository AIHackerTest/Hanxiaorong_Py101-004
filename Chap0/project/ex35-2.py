from sys import exit # 导入 exit 模块

def gold_room():
	print ("This room is full of gold. How much do you take?")
	
	next = input("> ")
	if "0" in next or "1" in next: # 如果输入的数字里面有0或者1
		how_much = int(next) # 定义变量 how_much
	else:
		dead("Man, learn to type a number.") # 运行dead() 后程序结束
	
	if how_much < 50:
		print ("Nice, you're not greedy, you win!")
		exit(0) # 程序正确运行后退出
	else:
		dead("You greedy bastard!") # 运行dead() 后程序结束
		
		
def bear_room():
	print ("There is a bear here.")
	print ("The bear has a bunch of honey.")
	print ("The fat bear is in front of another door.")
	print ("How are you going to move the bear?")
	bear_moved = False # 如果一行 bear_moved = True ， 第一个 elif 不执行
	
	while True: # 建立一个无线循环
		next = input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")#运行dead()函数后程序结束
		elif next == "taunt bear" and not bear_moved: # 调用的是前面的 bear_moved
			print ("The bear has moved from the door. You can go through it now.")# 打印字符串后，程序继续运行
			bear_moved = True # 运行完第一个elif后才生效
		elif next == "taunt bear" and bear_moved: # 调用前面的最近的 bear_moved
			dead("The bear gets pissed off and chews your leg off.")# 运行dead()函数后退出
		elif next == "open door" and bear_moved:# 为什么一开始输入 open door 打印的是 else，连续输入open door 程序不结束。
			gold_room()
		else:
			print ("I got no idea what that means.")
			
			
def cthulhu_room():
	print ("Here you see the great evil Cthulhu.")
	print ("He, it, whatever stares at you and you go insane.")
	print ("Do you flee for your life or eat your head?")
	
	next = input() # 输入内容
	
	if "flee" in next: # 也可以写成 if next == "flee": 
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cehulhu_room()
		
		
def dead(why): # 定义函数 dead()
	print (why, "Good job!")
	exit(0) # 执行完dead()函数退出
	
def start():
	print ("You are in a dark room.")
	print ("There is a door to your right and left.")
	print ("Which one do you take?")
	
	next = input("> ")
	
	if next == "left":
		bear_room()
	if next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

		
start()
