from sys import argv  # 将sys模块导入进来

script, first, second, third = argv  # 设置参数，script, first, second, third 共4个参数，将参数放在argv 变量下

print ("The script is called :", script) # 解包，将参数赋值给变量，打印输出的是ex13-2.py,这是一个参数
print ("Your first variable is:", first) # 解包，将参数赋值给变量，可以自定义任何名称，包括数字
first = input("give a number")  # 结合raw_input 使用
print ("Your second variable is:", second)
second = input("give a number")
print ("Your third variable is :", third)
third = input("give a number")


