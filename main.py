from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort


root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 700)
root.config(bg='black')

#variables
selected_algo = StringVar()
data = []

def Draw(data, colorArray):
  canvas.delete('all')
  canva_h = 380
  canva_w = 680
  x_width = canva_w / (len(data)+1)
  offset = 30
  spacing = 10

  normalized_data = [i/max(data) for i in data]

  for i, height in enumerate(normalized_data):
    #top left
    x0 = i * x_width + offset + spacing
    y0 = canva_h - height * 300
    #top right
    x1 = (i+1) * x_width + offset
    y1 = canva_h
    canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
    canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
  
  root.update_idletasks()


def Generate():
  global data
  minVal = int(minEntry.get())
  maxVal = int(maxEntry.get())
  size = int(sizeEntry.get())

  data = []
  for _ in range(size):
    data.append(random.randrange(minVal, maxVal+1))

  Draw(data, ['red' for x in range(len(data))])

def Algorithm():
  global data
  bubble_sort(data, Draw, speedScale.get())

#Frame
UI_frame = Frame(root, width=700,height=200, bg='grey')
UI_frame.grid(row=0,column=0,padx=10,pady=5)

#Canvas
canvas = Canvas(root, width=700, height=380, bg='white')
canvas.grid(row=1, column=0,padx=10, pady=5)

#UI Area
#Row[0]
Label(UI_frame, text='Algorithm: ', bg='grey').grid(row=0,column=0,padx=5,pady=5, sticky=W)
algomenu = ttk.Combobox(UI_frame, textvariable=selected_algo, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label='Select speed')
speedScale.grid(row=0, column=2, padx=5, pady=0)
Button(UI_frame, text='Start', bg='red', command=Algorithm).grid(row=0, column=3, padx=5,pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label='Size')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=20, resolution=1, orient=HORIZONTAL, label='Min Value')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label='Max values')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text='Generate', bg='lawn green', command=Generate).grid(row=1, column=3, padx=5,pady=5)

root.mainloop()
