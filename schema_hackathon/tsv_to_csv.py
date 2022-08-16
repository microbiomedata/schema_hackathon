import csv
import sys

csv.writer(sys.stdout).writerows(csv.reader(sys.stdin, dialect='excel-tab'))
