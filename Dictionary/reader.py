import csv
import re


reader = csv.reader(open('dist.male.first','rb'))

for line in reader:
	name, num1, num2, rank = re.split(' +', line[0])
	print name, rank