import tkinter as tk
import tkinter.ttk as ttk

from textarea import TextArea

class MainWindow(tk.Tk):
	def __init__(self):
		super().__init__()
		self.text_area = TextArea(self,bg="white",fg="black",undo=True)
		self.scrollbar = ttk.Scrollbar(orient="vertical",command=self.scroll_text)
		self.text_area.configure(yscrollcommand = self.scrollbar.set)

		self.line_numbers = tk.Text(self, bg="black", fg="white")
		first_100_numbers = [str(n) for n in range(1,101)]
		self.line_numbers.insert(1.0,"\n".join(first_100_numbers))
		self.line_numbers.configure(state="disabled", width=3,yscrollcommand=self.scrollbar.set)

		self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
		self.text_area.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1 )
		self.bind_events()
	def scroll_text(self, *args):
		if len(args) > 1:
			self.text_area.yview_moveto(args[1])
			self.line_numbers.yview_moveto(args[1])
		else:
			event = args[0]
			if event.delta:
				move = -1 * (event.delta / 120)
			else:
				if event.num == 5:
					move=1
				else:
					move=-1
			self.text_area.yview_scroll(int(move), "units")
			self.line_numbers.yview_scroll(int(move), "units")

	def bind_events(self):
		self.text_area.bind("<MouseWheel>", self.scroll_text)
		self.text_area.bind("<Button-4>", self.scroll_text)
		self.text_area.bind("<Button-5>", self.scroll_text)

		self.line_numbers.bind("<MouseWheel>", lambda e: "break")
		self.line_numbers.bind("<Button-4>", lambda e: "break")
		self.line_numbers.bind("<Button-5>", lambda e: "break")

if __name__ == '__main__':
	MainWindow().mainloop()
