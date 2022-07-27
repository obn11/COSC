from tkinter import *
import random
import time
import csv
from tkinter.ttk import *

ds = [64, 128, 256, 512]
ws = [8, 16, 32]
dw = []
for i in ds:
	for j in ws:
		dw.append((i, j))
reps = 8
random.shuffle(dw)
i = 0
name = 'Oliver'
allLogs = []


def swap(event):
	global i
	global t0
	i += 1
	t1 = time.time() - t0
	global d
	global w
	allLogs.append([name, d, w, i, t1])
	t0 = time.time()
	if i < reps:
		tgc = c.coords('goal')
		tbc = c.coords('bad')
		c.coords('goal', tbc)
		c.coords('bad', tgc)
	elif len(dw) > 0:
		global cw
		global ch
		d, w = dw.pop()
		ts = d + w
		m = (cw - ts) / 2
		c.coords('goal', (m, 0, m + w, ch))
		c.coords('bad', (m + d, 0, m + w + d, ch))
		i = 0
	else:
		c.coords('goal', (0, 0, 0, 0))
		c.coords('bad', (0, 0, 0, 0))
		c.create_text(cw/2, ch/2, fill="darkblue", font="Times 80 italic bold", text="YOU WIN!")
		with open('csv_out.csv', 'w', encoding='UTF8', newline='') as f:
			writer = csv.writer(f)
			writer.writerows(allLogs)


master = Tk()
cw = 1024
ch = 512
c = Canvas(master, width=cw, height=ch)
c.pack()
d, w = dw.pop()
ts = d+w
m = (cw - ts)/2
c.create_rectangle(m, 0, m+w, ch, tag="goal", fill="green")
c.create_rectangle(m+d, 0, m+w+d, ch, tag="bad", fill="blue")
c.tag_bind("goal", "<Button-1>", swap)
t0 = time.time()


master.mainloop()




