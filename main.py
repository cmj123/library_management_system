from tkinter import *
from tkinter import ttk

class Main(object):
    def __init__(self,master):
        self.master = master

        # Frames
        mainFrame=Frame(self.master)
        mainFrame.pack()

        # Top Frame
        topFrame = Frame(mainFrame, width=1350, height=70, bg='#f8f8f8', padx=20, relief=SUNKEN,
                        borderwidth=2)
        topFrame.pack(side=TOP,fill=X)

        # Centre Frame
        centerFrame = Frame(mainFrame, width=1350, relief=RIDGE, bg="#e0f0f0", height=680)
        centerFrame.pack(side=TOP)

        # Center Left Frame
        centerLeftFrame = Frame(centerFrame, width=900, height=700, bg='#e0f0f0', borderwidth=2, relief='sunken')
        centerLeftFrame.pack(side=LEFT)

        # center right frame
        centerRightFrame = Frame(centerFrame, width=450, height=700, bg='#e0f0f0', borderwidth=2, relief=SUNKEN)
        centerRightFrame.pack()

        # search bar
        search_bar = LabelFrame(centerRightFrame, width=440, height=175, text='Search Box', bg='#9bc9ff')
        search_bar.pack(fill=BOTH)

def main():
    root = Tk()
    app = Main(root)
    root.title("Library Management System")
    root.geometry("1350x750+350+200")
    root.iconbitmap('./icons/icon.ico')
    root.mainloop()

if __name__ == '__main__':
    main()
