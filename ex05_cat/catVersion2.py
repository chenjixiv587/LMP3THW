# 接受被写出的文件的个数不确定
# 被写入的只有一个
import argparse

parser = argparse.ArgumentParser(description="repalce the cat command")

parser.add_argument(
    "fileFrom", nargs="+", type=argparse.FileType("r"), help="accept many files"
)
parser.add_argument("--fileTo", type=argparse.FileType("a"), help="write to this file")


args = parser.parse_args()
# 将被接受的文件 存在一个列表中 args.fileFrom
# 遍历列表 得到每个文件的内容
contentAll = ""
for singleFile in args.fileFrom:
    contentAll += singleFile.read()

args.fileTo.write(contentAll)
