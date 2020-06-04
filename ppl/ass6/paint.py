from tkinter import *
import tkinter.font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

class PaintApp:
	drawing_tool = "pencil"
	left_button = 'up'
	x_pos,y_pos = None ,None
	x1_line_pt,y1_line_pt,x2_line_pt,y2_line_pt = None ,None ,None ,None 

		
	def __init__(self,root):
		self.drawing_area = Canvas(root)
		root.title("My Paint")
		root.geometry('1200x700')
		self.drawing_area.pack()
		self.drawing_area.bind("<Motion>", self.motion)
		self.drawing_area.bind("<ButtonPress-1>", self.left_button_down)
		self.drawing_area.bind("<ButtonRelease-1>", self.left_button_up)
		self.drawing_area.bind('<Control-w>', self.exit)
		self.drawing_area.pack(side = tkinter.LEFT, expand=True, fill=tkinter.BOTH)
		
		self.root = root
		self.filename = None
#menubar
		menubar = Menu(self.root)
		self.root.config(menu = menubar)#creates menubar
		dropdown = Menu(menubar, tearoff=0)#, font=fonts)#tearoff used to separate menus from menubar
		menubar.add_cascade(label="File", menu=dropdown)#add name to the dropdownmenu
		dropdown.add_command(label="New file", command = self.new_file,accelerator='Ctrl+N')
		dropdown.add_command(label="Open file", command = self.open_file,accelerator='Ctrl+O')
		dropdown.add_command(label="Save", command = self.save_file,accelerator='Ctrl+S')
		dropdown.add_command(label="Save As", command = self.save_as_file,accelerator='Ctrl+Shift+S')
		dropdown.add_separator()
		dropdown.add_command(label="Exit", command = self.root.destroy,accelerator='Ctrl+W')
		about_dropdown = Menu(menubar, tearoff=0)
#	menubar.add_cascade(label="About", menu=about_dropdown)
#	about_dropdown.add_command(label='Release notes', command = self.release_message)
#	about_dropdown.add_separator()
#	about_dropdown.add_command(label='About',command = self.about_message)


#options in menubar
	def window_title(self,name=None):
		if name:
			self.root.title(name+"My Paint")
		else:
			self.root.title("My Paint")

               
	def new_file(self,*args):
		self.drawing_area.delete(1.0, tkinter.END)
		self.window_title()


	def open_file(self,*args):
		self.filename = filedialog.askopenfilename(
		defaultextension=".odg",
		filetypes=[("All files","*.*"),
				("Java files","*.java"),
				("C files","*.c"),
		    		("Python scripts","*.py"),
		   		("CSS documents","*.css"),
		    		("Html documents","*.html")
		    		("Text files",".txt")
		    	]
		)
		if self.filename:
			self.drawing_area.delete(1.0,tkinter.END)
			with open(self.filename,'r') as fn:	
				self.drawing_area.insert(1.0,fn.read())
			self.window_title(self.filename)
			
			
	def save_file(self,*args):
		if self.filename:
			try:
				text_content = self.drawing_area.get(1.0, tkinter.END)	
				with open(self.filename, 'w') as fh:
					fh.write(text_content)
					fh.close()
			except Exception as e:
				print(e)
		else:
			self.save_as_file()
	
	def save_as_file(self,*args):
		try:
			files = [("All files","*.*"),
					("Java files","*.java"),
					("C files","*.c"),
			    		("Python scripts","*.py"),
			    		("CSS documents","*.css"),
			    		("Html documents","*.html"),
			    		("Text files","*.txt"),
			    	]
			file = filedialog.asksaveasfile(filetypes=files, defaultextension = '.odg')
			btn = ttk.Button(self.root, text='Save', command = lambda: save_as_file(self.filename))
			btn.pack(side =TOP, pady=20)
			
			
			
			
#			text_content = self.drawing_area.get(1.0, tkinter.END)
			with open(file,'w') as f:
				f.write(text_content)
				f.close()
			self.window_title(new_file)
			self.filename = new_file
		except Exception as e:
			print(e)
		
	def exit(self,*args):
		answer = messagebox.askyesno('Question','Do you really want to quit?')
		if answer == True:
			self.root.destroy()



#Mouse_Down
	def left_button_down(self, event=None):
		self.left_button = "down"
		self.x1_line_pt = event.x
		self.y1_line_pt = event.y
		self.root = event.y

#Mouse_Up
	def left_button_up(self, event=None):
		self.left_but = "up"
		self.x1_pos = None
		self.y1_pos = None
		self.x2_line_pt = event.x
		self.y2_line_pt = event.y

		if self.drawing_tool == "line":
			self.line_draw(event)
		if self.drawing_tool == "arc":
			self.arc_draw(event) 
		if self.drawing_tool == "oval":
			self.oval_draw(event) 
		if self.drawing_tool == "rectangle":
			self.rectangle_draw(event) 
		if self.drawing_tool == "text":
			self.text_draw(event) 


#Catch_Mouse_move
	def motion(self,event = None):
		if self.drawing_tool == 'pencil':
			self.pencil_draw(event)


	def pencil_draw(self,event=None):
		if self.left_button == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=True)
			self.x_pos = event.x
			self.y_pos = event.y



	def line_draw(self,event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
			event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=True, fill='red')
		


#Draw_Arc
	def arc_draw(self,event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):		
			coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

			event.widget.create_arc(coords, start =0, extent=150, style=ARC)#PIESLICE/CHORD)
			
#Draw_Oval
	def oval_draw(self,event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):					
			event.widget.create_oval(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill ='midnight blue', outline=yellow,width=2)
	
	
			
#Draw_Rectangle
	def rectangle_draw(self,event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):		
			event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, fill ='midnight blue', outline=yellow,width=2)
			

#write text
	def text_draw(self):
		if None not in (self.x1_line_pt, self.y1_line_pt):
			text_font = tkinter.font.Font(family="Helvetica", size=20, weight='bold',slant='italic')
			event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill="green", font=text_font, text='amazing')
			
		
	def shortcuts(self):	
		self.drawing_area.bind('<Control-n>', self.new_file)
		self.drawing_area.bind('<Control-o>', self.open_file)
		self.drawing_area.bind('<Control-s>', self.save_file)
		self.drawing_area.bind('<Control-S>', self.save_as_file)
		self.drawing_area.bind('<Control-w>', self.exit)
		
					
root =Tk()
paint_app = PaintApp(root)
root.mainloop()
		
		
		

