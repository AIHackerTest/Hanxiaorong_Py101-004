from sys import argv  # 将sys模块导入进来

script, first, second, third = argv  # 设置参数，script, first, second, third 共4个参数，将参数放在argv 变量下

script = input("The script is called:")
first = input("Your first variable is:")
second = input("Your second variable is:")
third = input("Your third variable is :")

print (script)
print (first)
print (second)
print (third)
