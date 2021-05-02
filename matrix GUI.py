from tkinter import *
from tkinter import ttk
app = Tk()
app.title("matrix")
a1x = IntVar()
b1x = IntVar()
c1x = IntVar()
a2x = IntVar()
b2x = IntVar()
c2x = IntVar()
a3x = IntVar()
b3x = IntVar()
c3x = IntVar()
e1x = IntVar()
f1x = IntVar()
g1x = IntVar()
e2x = IntVar()
f2x = IntVar()
g2x = IntVar()
e3x = IntVar()
f3x = IntVar()
g3x = IntVar()
heading = ttk.Label(text = 'MATRIX CALCULATOR').grid(row = 0,columnspan = 5)
ttk.Label(text = '').grid()
marix1 = ttk.Label(text = 'MATRIX A').grid(row = 1,column = 0)
a1 = ttk.Entry(width = 10, textvariable = a1x)
a1.grid(row = 2, column = 0)
b1 = ttk.Entry(width = 10, textvariable = b1x)
b1.grid(row = 2, column = 1)
c1 = ttk.Entry(width = 10, textvariable = c1x)
c1.grid(row = 2, column = 2)
a2 = ttk.Entry(width = 10, textvariable = a2x)
a2.grid(row = 3, column = 0)
b2 = ttk.Entry(width = 10, textvariable = b2x)
b2.grid(row = 3, column = 1)
c2 = ttk.Entry(width = 10, textvariable = c2x)
c2.grid(row = 3, column = 2)
a3 = ttk.Entry(width = 10, textvariable = a3x)
a3.grid(row = 4, column = 0)
b3 = ttk.Entry(width = 10, textvariable = b3x)
b3.grid(row = 4, column = 1)
c3 = ttk.Entry(width = 10, textvariable = c3x)
c3.grid(row = 4, column = 2)
marix1 = ttk.Label(text = 'MATRIX B').grid(row = 5,column = 0)
#answer = ttk.Label(text = 'Answer = ').grid(row = 5, column = 3)
e1 = ttk.Entry(width = 10, textvariable = e1x)
e1.grid(row = 6, column = 0)
f1 = ttk.Entry(width = 10, textvariable = f1x)
f1.grid(row = 6, column = 1)
g1 = ttk.Entry(width = 10, textvariable = g1x)
g1.grid(row = 6, column = 2)
e2 = ttk.Entry(width = 10, textvariable = e2x)
e2.grid(row = 7, column = 0)
f2 = ttk.Entry(width = 10, textvariable = f2x)
f2.grid(row = 7, column = 1)
g2 = ttk.Entry(width = 10, textvariable = g2x)
g2.grid(row = 7, column = 2)
e3 = ttk.Entry(width = 10, textvariable = e3x)
e3.grid(row = 8, column = 0)
f3 = ttk.Entry(width = 10, textvariable = f3x)
f3.grid(row = 8, column = 1)
g3 = ttk.Entry(width = 10, textvariable = g3x)
g3.grid(row = 8, column = 2)
ttk.Label(text = '').grid()
class Matrix():
	def add():
		global xx1
		global xx2
		global xx3
		global xx4
		global xx5
		global xx6
		global xx7
		global xx8
		global xx9
		#ttk.Label(text = 'ANSWER').grid(row = 3, column = 3)
		x1 = int(a1.get()) + int(e1.get())
		xx1 = ttk.Label(text = x1)
		xx1.grid(row = 4, column = 3)
		x2 = int(a2.get()) + int(e2.get())
		xx2 = ttk.Label(text = x2)
		xx2.grid(row = 5, column = 3)
		x3 = int(a3.get()) + int(e3.get())
		xx3 = ttk.Label(text = x3)
		xx3.grid(row = 6, column = 3)
		y1 = int(b1.get()) + int(f1.get())
		xx4 = ttk.Label(text = y1)
		xx4.grid(row = 4, column = 4)
		y2 = int(b2.get()) + int(f2.get())
		xx5 = ttk.Label(text = y2)
		xx5.grid(row = 5, column = 4)
		y3 = int(b3.get()) + int(f3.get())
		xx6 = ttk.Label(text = y3)
		xx6.grid(row = 6, column = 4)
		z1 = int(c1.get()) + int(g1.get())
		xx7 = ttk.Label(text = z1)
		xx7.grid(row = 4, column = 5)
		z2 = int(c2.get()) + int(g2.get())
		xx8 = ttk.Label(text = z2)
		xx8.grid(row = 5, column = 5)
		z3 = int(c3.get()) + int(g3.get())
		xx9 = ttk.Label(text = z3)
		xx9.grid(row = 6, column = 5)
	def sub():
		#ttk.Label(text = 'ANSWER').grid(row = 3, column = 3)
		global xx1
		global xx2
		global xx3
		global xx4
		global xx5
		global xx6
		global xx7
		global xx8
		global xx9
		x1 = int(a1.get()) - int(e1.get())
		xx1 = ttk.Label(text = x1)
		xx1.grid(row = 4, column = 3)
		x2 = int(a2.get()) - int(e2.get())
		xx2 = ttk.Label(text = x2)
		xx2.grid(row = 5, column = 3)
		x3 = int(a3.get()) - int(e3.get())
		xx3 = ttk.Label(text = x3)
		xx3.grid(row = 6, column = 3)
		y1 = int(b1.get()) - int(f1.get())
		xx4 = ttk.Label(text = y1)
		xx4.grid(row = 4, column = 4)
		y2 = int(b2.get()) - int(f2.get())
		xx5 = ttk.Label(text = y2)
		xx5.grid(row = 5, column = 4)
		y3 = int(b3.get()) - int(f3.get())
		xx6 = ttk.Label(text = y3)
		xx6.grid(row = 6, column = 4)
		z1 = int(c1.get()) - int(g1.get())
		xx7 = ttk.Label(text = z1)
		xx7.grid(row = 4, column = 5)
		z2 = int(c2.get()) - int(g2.get())
		xx8 = ttk.Label(text = z2)
		xx8.grid(row = 5, column = 5)
		z3 = int(c3.get()) - int(g3.get())
		xx9 = ttk.Label(text = z3)
		xx9.grid(row = 6, column = 5)
	def mul():
		#ttk.Label(text = 'ANSWER').grid(row = 3, column = 3)
		global xx1
		global xx2
		global xx3
		global xx4
		global xx5
		global xx6
		global xx7
		global xx8
		global xx9
		x1 = int(a1.get()) * int(e1.get())
		xx1 = ttk.Label(text = x1)
		xx1.grid(row = 4, column = 3)
		x2 = int(a2.get()) * int(e2.get())
		xx2 = ttk.Label(text = x2)
		xx2.grid(row = 5, column = 3)
		x3 = int(a3.get()) * int(e3.get())
		xx3 = ttk.Label(text = x3)
		xx3.grid(row = 6, column = 3)
		y1 = int(b1.get()) * int(f1.get())
		xx4 = ttk.Label(text = y1)
		xx4.grid(row = 4, column = 4)
		y2 = int(b2.get()) * int(f2.get())
		xx5 = ttk.Label(text = y2)
		xx5.grid(row = 5, column = 4)
		y3 = int(b3.get()) * int(f3.get())
		xx6 = ttk.Label(text = y3)
		xx6.grid(row = 6, column = 4)
		z1 = int(c1.get()) * int(g1.get())
		xx7 = ttk.Label(text = z1)
		xx7.grid(row = 4, column = 5)
		z2 = int(c2.get()) * int(g2.get())
		xx8 = ttk.Label(text = z2)
		xx8.grid(row = 5, column = 5)
		z3 = int(c3.get()) * int(g3.get())
		xx9 = ttk.Label(text = z3)
		xx9.grid(row = 6, column = 5)
	def div():
		#ttk.Label(text = 'ANSWER').grid(row = 3, column = 3)
		try:
			global xx1
			global xx2
			global xx3
			global xx4
			global xx5
			global xx6
			global xx7
			global xx8
			global xx9
			x1 = int(a1.get()) / int(e1.get())
			xx1 = ttk.Label(text = x1)
			xx1.grid(row = 4, column = 3)
			x2 = int(a2.get()) / int(e2.get())
			xx2 = ttk.Label(text = x2)
			xx2.grid(row = 5, column = 3)
			x3 = int(a3.get()) / int(e3.get())
			xx3 = ttk.Label(text = x3)
			xx3.grid(row = 6, column = 3)
			y1 = int(b1.get()) / int(f1.get())
			xx4 = ttk.Label(text = y1)
			xx4.grid(row = 4, column = 4)
			y2 = int(b2.get()) / int(f2.get())
			xx5 = ttk.Label(text = y2)
			xx5.grid(row = 5, column = 4)
			y3 = int(b3.get()) / int(f3.get())
			xx6 = ttk.Label(text = y3)
			xx6.grid(row = 6, column = 4)
			z1 = int(c1.get()) / int(g1.get())
			xx7 = ttk.Label(text = z1)
			xx7.grid(row = 4, column = 5)
			z2 = int(c2.get()) / int(g2.get())
			xx8 = ttk.Label(text = z2)
			xx8.grid(row = 5, column = 5)
			z3 = int(c3.get()) / int(g3.get())
			xx9 = ttk.Label(text = z3)
			xx9.grid(row = 6, column = 5)
		except ZeroDivisionError:
			pass
			###ttk.Label(text = 'INPUT A VALUE FOR 0').grid(row = 11, column = 2)
	def clear():
		xx1.destroy()
		xx2.destroy()
		xx3.destroy()
		xx4.destroy()
		xx5.destroy()
		xx6.destroy()
		xx7.destroy()
		xx8.destroy()
		xx9.destroy()
add = ttk.Button(text = 'ADD', command = Matrix.add).grid(row = 10, column = 0)
sub = ttk.Button(text = 'SUBTRACT', command = Matrix.sub).grid(row = 10, column = 1)
mul = ttk.Button(text = 'MULTIPLY', command = Matrix.mul).grid(row = 10, column = 2)
div = ttk.Button(text = 'DIVIDE', command = Matrix.div).grid(row = 10, column = 4)
clear = ttk.Button(text = 'CLEAR',command = Matrix.clear).grid(row = 11, column = 0)
exit = ttk.Button(text = 'QUIT', command = exit).grid(row = 11, column = 1)
app.mainloop()