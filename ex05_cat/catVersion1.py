import argparse

parser = argparse.ArgumentParser(description="Write the cat commnd with python")
# 接受用于写出的文件
parser.add_argument("--fileA", type=argparse.FileType("r"), help="Read the fileA")
parser.add_argument("--fileB", type=argparse.FileType("r"), help="Read the fileB")
# 接受用于写入的文件
parser.add_argument("--fileC", type=argparse.FileType("a"), help="Write to the fileC")

args = parser.parse_args()
fileA = args.fileA
fileB = args.fileB
fileC = args.fileC
# 读取文件
contentOfFileA = fileA.read()
contentOfFileB = fileB.read()
# 写入文件
fileC.write(contentOfFileA)
fileC.write(contentOfFileB)
