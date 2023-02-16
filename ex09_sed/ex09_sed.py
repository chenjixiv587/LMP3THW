import argparse
import re

parser = argparse.ArgumentParser(description="sed")
parser.add_argument("-e", "--expression", type=str, help="type the expression")

parser.add_argument("file", type=argparse.FileType("r"))

args = parser.parse_args()

expression = args.expression
print(expression.split("/")[1])

fileContent = args.file.read()
print(fileContent.replace(expression.split("/")[1], expression.split("/")[2]))
print(fileContent)
