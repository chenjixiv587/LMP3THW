# grep 默认不看路径
# grep test *txt

import argparse
import glob
import os

parser = argparse.ArgumentParser()
# action="store_true" 也就是说  在 只输入 -r 的时候 如果进行条件判断 那么默认的就是  true
parser.add_argument(
    "-r",
    "--regularExpression",
    action="store_true",
    help="在有-r的时候 那么第二个接收的参数 就是路径 如果没有-r 的时候 第二个接受的就是 文件后缀名",
)
parser.add_argument("strToFind", type=str, help="The strig to find")
parser.add_argument("fileToFind", type=str, help="The file to find")

args = parser.parse_args()
strToFind = args.strToFind
fileToFind = args.fileToFind
isR = args.regularExpression


# 判断一个字符串 是否在 文件中
def judgeStrinFile(strNeedFind, filetoCheck):
    with open(filetoCheck) as f:
        contents = f.read()
        if strNeedFind in contents:
            result.append(filetoCheck)


# 找出含有 *txt 的文件 也就是以 txt 结尾的文件
# 如果想要迭代查询的话  就需要在路径前加上 **/   recursive=True
# 　当命令行的参数没有 -r 的时候  就按照这 被查找的字符串  文件名字 来规定参数
if not isR:
    fileList = glob.glob(f"**/{fileToFind}", recursive=True)
    result = []
    for file in fileList:
        judgeStrinFile(strToFind, file)

    print(result)
# 　当命令行的参数有 -r 的时候  就按照这 被查找的字符串  查找路径 来规定参数
# 　也就是获得指定路径里面的　包含需要查找的字符串的所有文件
else:
    result = []
    for paths, dirs, files in os.walk(fileToFind, topdown=True):
        for file in files:
            judgeStrinFile(strToFind, f"{paths}/{file}")
    print(result)
