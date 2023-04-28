from tkinter import *
from frame import *


frame = create_frame()
canvas = Canvas(width=400, height=600, background='#232323')
cell = create_cell(canvas)
# text = create_text("cc", frame, 100, 100)

frame.mainloop()
