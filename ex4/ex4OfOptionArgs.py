import argparse

parser = argparse.ArgumentParser(description="传入参数，打印出姓名")
# required = True   表示参数必须要有
# 当有required = True 时，deafult 就失效了
parser.add_argument("--family", type=str, help="姓", required=True, default="ce")
# default 表示默认 如果命令行里没有提供 那么就显示默认的
# 如果提供 就显示提供的值
parser.add_argument("--name", type=str, help="名", default="帅哥")
# 参数是以字典的形式 存储在 args 里面的
args = parser.parse_args()
# 打印姓名
print(args.family + args.name)

# 在命令行 输入的时候 要加上  --family=zhang --name=san
