# shell cut -f -d 必须一起使用
import argparse

parser = argparse.ArgumentParser(description="cut the file line")
parser.add_argument("-f", "--fragment", type=str, help="give the number, from 1")
parser.add_argument("-d", "--delimiter", type=str, help="give the delimiter")
parser.add_argument("file", type=argparse.FileType("r"), help="give the file name")
args = parser.parse_args()
fragment = args.fragment.split(",")
# print(fragment[0], fragment[1])
startFrom = int(fragment[0])
endTo = int(fragment[1])
delimiter = args.delimiter
file = args.file
fileContents = file.readlines()
# print(fileContents)
for content in fileContents:
    # print(content.split(delimiter))
    result = content.split(delimiter)[startFrom - 1 : endTo]
    print(" ".join(result))
