import pandas as pd
import csv
import math

REPS = 8
# key:value (amp, wid): [list of trys]
dicty = {}
out = []


def idx(tup):
	return math.log2((tup[0]/tup[1]) + 1)


data = pd.read_csv('csv_out.csv').values.tolist()

print(data)
for i in data:
	key = round(idx((i[1], i[2])), 3)
	tv = dicty.get(key)
	if data[3] != 1 and data[3] != 2:
		if tv is not None:
			tv.append(round(i[4], 5))
			dicty[key] = tv
		else:
			dicty.update({key: [round(i[4], 5)]})

print(dicty)
for key, value in dicty.items():
	avg = sum(value)/len(value)
	lis = [round(key, 3), round(avg, 3)]
	out.append(lis)


with open('summary.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(out)