"""
在命令行 中进行 加减乘除等操作
"""
import argparse

# 初始化
parser = argparse.ArgumentParser(description="在命令行里进行运算")
# 接受三个参数  两个数字 一个运算符
parser.add_argument("--num1", type=float, help="数字1")
parser.add_argument("--num2", type=float, help="数字2")
parser.add_argument("--operation", type=str, help="运算符", default="*")

# 结果初始化
result = None
args = parser.parse_args()
num1 = args.num1
num2 = args.num2
operation = args.operation
# 判断运算符
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "pow":
    result = pow(num1, num2)
else:
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("num2不能为0")
        exit(1)

print(result)
