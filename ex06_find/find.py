"""
实现 find 的部分功能 
包括 -name  -type  -print 
-exec
"""

import argparse
import os

parser = argparse.ArgumentParser(description="make find")
parser.add_argument("path", type=str, help="路径")
parser.add_argument("-name", "--filename", type=str, help="文件名称", required=False)
parser.add_argument("-type", "--filetype", type=str, help="显示所有的文件夹", required=False)
args = parser.parse_args()
# 展示当前目录下所有以xxx结尾的文件（包括子目录里面的文件，一路到底）
# 展示当前目录下所有的目录（包括子目录，一路到底）


def findAllFilesAndDirs(path, filename, filetype):
    for paths, dirs, files in os.walk(path, topdown=True):
        if filename != None:
            for file in files:
                if file.endswith(filename[1:]):
                    print(f"{paths}/{file}")
        if filetype == "d":
            for fold in dirs:
                print(f"{paths}/{fold}")
        if filetype == "f":
            for file in files:
                print(f"{paths}/{file}")


# print(filename)


filename = args.filename
path = args.path
filetype = args.filetype
# print(filetype)

findAllFilesAndDirs(path, filename, filetype)
