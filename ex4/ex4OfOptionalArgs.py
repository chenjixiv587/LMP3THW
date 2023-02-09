import argparse

parser = argparse.ArgumentParser(description="传入一个数字")
# nargs = "+" 表示至少传入一个参数

"""
参数nargs：
nargs='*' 　表示参数可设置零个或多个
nargs='+' 表示参数可设置一个或多个
nargs='?'　表示参数可设置零个或一个
"""
# 当我们使用 -- 位置参数时 metavar 就是别名
parser.add_argument("--integers", type=int, help="传入一个数字", nargs="+", metavar=int)
args = parser.parse_args()
print(sum(args.integers))
