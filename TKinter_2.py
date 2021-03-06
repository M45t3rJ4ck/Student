from tkinter import *
from tkinter import ttk, messagebox


# ---------- VARIABLES & UNBIND ----------
def get_data(event):

    # Output the values for the Widgets with get()
    print("String :", strVar.get())
    print("Integer :", intVar.get())
    print("Double :", dblVar.get())
    print("Boolean :", boolVar.get())


# You can unbind and rebind an event to a function
def bind_button(event):
    if boolVar.get():
        getDataButton.unbind("<Button-1>")
    else:
        getDataButton.bind("<Button-1>", get_data)


root = Tk()

# As I showed previously there are TkInter variables you can use with Widgets to set and get values
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

# Set the default values with set()
strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

# Assign the variable to either textvariable or variable
strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)
intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)
dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

# Depending on if this check button is selected or not will determine if we can get data on our Widgets
theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)

# Call the function get_data on click
getDataButton = Button(root, text="Get Data")
getDataButton.bind("<Button-1>", get_data)
getDataButton.pack(side=LEFT)

root.mainloop()


# ---------- STYLING WIDGETS ----------
# There are many ways to custom style your widgets
# You can open message boxes
def open_msg_box():
    messagebox.showwarning("Event Triggered", "Button Clicked")


root = Tk()

# You can define the size of the window and the position on the screen with widthxheight+xoffset+yoffset
root.geometry("400x400+300+300")

# You can make it so the window isn't resizable
root.resizable(width=False, height=False)

frame = Frame(root)

# Your can change a styling option like this
# Color option names are here http://wiki.tcl.tk/37701
# For the font list the font family, px and font style
style = ttk.Style()
style.configure("TButton", foreground="midnight blue", font="Times 20 bold italic", padding=20)

# Ttk widget names : TButton, TCheckbutton, TCombobox,
# TEntry, TFrame, TLabel, TLabelframe, TMenubutton,
# TNotebook, TProgressbar, TRadiobutton, TScale,
# TScrollbar, TSpinbox, Treeview
# You can change the theme style for your applications
# This shows you all the themes for your OS
print(ttk.Style().theme_names())

# You can see current style settings like this
print(style.lookup('TButton', 'font'))
print(style.lookup('TButton', 'foreground'))
print(style.lookup('TButton', 'padding'))

# Change the theme for every widget
ttk.Style().theme_use('clam')

# Have the button open a message box on click
theButton = ttk.Button(frame, text="Important Button", command=open_msg_box)

# You can also disable and enable buttons
theButton['state'] = 'disabled'
theButton['state'] = 'normal'
theButton.pack()
frame.pack()

root.mainloop()


# ---------- MENU BARS ----------
# Quits the TkInter app when called
def quit_app():
    root.quit()


# Opens a message box when called
def show_about(event=None):
    messagebox.showwarning("About", "This Awesome Program was Made in 2016")


root = Tk()

# Create the menu object
the_menu = Menu(root)

# ----- FILE MENU -----
# Create a pull down menu that can't be removed
file_menu = Menu(the_menu, tearoff=0)

# Add items to the menu that show when clicked compound allows you to add an image
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

# Add a horizontal bar to group similar commands
file_menu.add_separator()

# Call for the function to execute when clicked
file_menu.add_command(label="Quit", command=quit_app)

# Add the pull down menu to the menu bar
the_menu.add_cascade(label="File", menu=file_menu)

# ----- FONT MENU FOR VIEW MENU -----
# Stores font chosen and will update based on menu selection
text_font = StringVar()
text_font.set("Times")


# Outputs font changes
def change_font(event=None):
    print("Font Picked :", text_font.get())


# Define font drop down that will be attached to view
font_menu = Menu(the_menu, tearoff=0)

# Define radio button options for fonts
font_menu.add_radiobutton(label="Times", variable=text_font, command=change_font)
font_menu.add_radiobutton(label="Courier", variable=text_font, command=change_font)
font_menu.add_radiobutton(label="Ariel", variable=text_font, command=change_font)

# ----- VIEW MENU -----
view_menu = Menu(the_menu, tearoff=0)

# Variable changes when line numbers is checked or unchecked
line_numbers = IntVar()
line_numbers.set(1)

# Bind the checking of the line number option to variable line_numbers
view_menu.add_checkbutton(label="Line Numbers", variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

# Add the pull down menu to the menu bar
the_menu.add_cascade(label="View", menu=view_menu)

# ----- HELP MENU -----
help_menu = Menu(the_menu, tearoff=0)

# accelerator is used to show a shortcut
# OSX, Windows and Linux use the following options:
# Command-O, Shift+Ctrl+S, Command-Option-Q with the modifiers Control, Ctrl, Option, Opt, Alt, Shift, Command
help_menu.add_command(label="About", accelerator="command-H", command=show_about)

the_menu.add_cascade(label="Help", menu=help_menu)

# Bind the shortcut to the function
root.bind('<Command-A>', show_about)
root.bind('<Command-a>', show_about)

# Display the menu bar
root.config(menu=the_menu)

root.mainloop()
