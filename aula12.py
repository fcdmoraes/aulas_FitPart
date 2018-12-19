from tkinter import *
import aula12blp

root = Tk()
root.title("BLPAPI CONFIG")
# root.geometry("400x300")
root.config(background = "#00005f")
### usando pack()
# b1 = Button(root, text = "Click 1")
# b1.pack(side = "top") #side tem 4 opções: top, botton, left, right

# b2 = Button(root, text = "Click 2")
# b2.pack(side = "left")


### usando Frame
# f = Frame(root)
# f.pack(side = "top", fill = X) # fill tem 3 opções: X (horizontal), Y (vertical), BOTH (ambos)

# b1 = Button(f, text = "Click 1")
# b1.pack(side = "left")

# b2 = Button(f, text = "Click 2")
# b2.pack(side = "left")

# f2 = Frame(root)
# f2.pack(fill = X)

# b3 = Button(f2, text = "Click 3")
# b3.pack(side = "right")


### usando grid
# b1 = Button(root, text = "Click 1")
# b2 = Button(root, text = "Click 2")
# b3 = Button(root, text = "Click 3")

# b1.grid(row = 0, column = 0)
# b2.grid(row = 2, column = 1)
# b3.grid(row = 1, column = 0, columnspan = 2, sticky = "we")

### Widgets

# def altera_texto(texto):
# 	b["text"] = texto

# f = Frame(root, width = 30, height = 50, bg = "red")
# f.pack()

# b1 = Button(root, text = "teste", command = lambda: altera_texto("novo"))
# # command não aceita parãmetros. Para poder passar uma função com parâmetros, precisamos usar a função lambda
# # def função(x):
# # 	print(x)
# # lambda x: print(x)

# # filtrado = filter(lambda x: x>12, lista) -> filtra os elementos da lista que são maiores do que 12 

# b = Button(f, width = 6, height = 6, text = "CLICK", font = ("Arial", 14, "bold italic"), bg = 'darkred', 
# 	fg = 'grey', activebackground = "grey", activeforeground = "darkred", command = b1.pack )
# b.pack()

# la = Label(f, text = "Texto", bg = "darkgreen")
# la.pack(fill = X)

# entrada = Entry(root)
# entrada.pack()

# b2 = Button(root, text = 'print', command = lambda: print(entrada.get()))
# b2.pack()

# escolha = StringVar()
# escolha.set("escolha")
# menu = OptionMenu(root, escolha, 'opção 1', 'opção 2')
# menu.pack()

# b3 = Button(root, text = 'print', command = lambda: print(escolha.get()))
# b3.pack()

class Options():
	def __init__(self):
		self.ip = "localhost"
		self.port = 8194

options = Options()
session = aula12blp.Session()

def config():
	def save():
		options.ip = ip_entry.get()
		options.port = int(port_entry.get())
		print("ip set to", options.ip)
		print("port set to", options.port)
		janela.destroy()

	janela = Toplevel()
	Label(janela, text = "IP:").pack()
	ip_entry = Entry(janela)
	ip_entry.pack()
	Label(janela, text = "Port:").pack()
	port_entry = Entry(janela)
	port_entry.pack()
	Button(janela, text = "Apply", command = save).pack()


menubar = Menu(root)

filemenu = Menu(menubar, tearoff = False)
filemenu.add_command(label = "Connect", command = lambda: session.start(options.ip, options.port))
filemenu.add_command(label = "Close", command = root.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
settingmenu = Menu(menubar, tearoff = False)
settingmenu.add_command(label = "Configure", command = config)
menubar.add_cascade(label = "Settings", menu = settingmenu)

root.config(menu = menubar)

Label(root, text = "Securities").pack()
sec_entry = Entry(root)
sec_entry.pack()

Label(root, text = "Fields").pack()
field_entry = Entry(root)
field_entry.pack()

Label(root, text = "Start Date (aaaammdd)").pack()
start_entry = Entry(root)
start_entry.pack()

Label(root, text = "End Date (aaaammdd)").pack()
end_entry = Entry(root)
end_entry.pack()

Button(root, text = "Execute", command = lambda: session.request(sec_entry.get(), field_entry.get(),
																 start_entry.get(), end_entry.get()) ).pack()

root.mainloop()