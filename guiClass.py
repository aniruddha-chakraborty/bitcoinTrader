import tkinter as tk

class SeaOfBTCapp(tk.Tk):

	def __init__(self,*args,**kwargs):

		tk.Tk.__init__(self,*args,**kwargs)
		container = tk.Frame(self)
		container.pack(side="top",fill="both",expand=True)

		container.grid_rowconfigure(0,weight=1)
		container.gridcolumnconfigure(0,weight=1)

		self.frames	= {}
		
		frame = StartPage(container,self)
		self.frames[StartPage] = frame
		frame.grid(row = 0, column= 0,sticky="nsew")

		self.show_frame(StartPage)