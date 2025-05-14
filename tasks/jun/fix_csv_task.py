import argparse
import csv

parser = argparse.ArgumentParser("Turns a pipe-delimited file into a comma-delimited file.")
parser.add_argument('old_file', type=str, help="Specify old file name")
parser.add_argument('new_file', type=str, help="Specify new file name")
parser.add_argument('--in-delimiter', type=str, dest="delim", default="|")
parser.add_argument('--in-quote', type=str, dest="quote", default="'")
args = parser.parse_args()


with open(args.old_file) as old_file:
    reader = csv.reader(old_file, delimiter=args.delim, quotechar=args.quote)
    rows = list(reader)

with open(args.new_file, mode="wt", newline="") as new_file:
    writter = csv.writer(new_file)
    writter.writerows(rows)


# 2012,Lexus,"""LFA"""
# 2009,GMC,Yukon XL 1500
# 1995,"""Mercedes-Benz""",C-Class
