from tkinter.filedialog import *
from tkinter.messagebox import *
import tkinter.ttk as ttk
from tkinter import colorchooser, font
import os 
# from PIL import Image, ImageTk
from tkinter import *
class TextEditor:
    def __init__(self):
        self.root =Tk()
        self.root.geometry("980x530")
        self.root.iconbitmap("hapus.ico")
        self.root.title("paulTextEditor")
        self.fm = Frame(self.root, width =580, height =580)
        self.fm.pack(fill =BOTH, expand=YES, side="top")
        self.yscrol = Scrollbar(self.fm, orient = "vertical")
        self.xscrol = Scrollbar(self.root, orient = "horizontal")
        self.comment = Text(self.fm, width =120, height =30, wrap =  NONE, xscrollcommand = self.xscrol.set, yscrollcommand = self.yscrol.set)
        self.comment.pack(side="left", fill =BOTH, expand = YES)
        self.comment.bind_all("<Control-n>", self.newPage)
        self.comment.bind_all("<Control-Key-N>", self.newPage)
        self.comment.bind_all("<KeyPress>", self.statusbar)
        self.comment.bind_all("<ButtonPress-1>", self.statusbar)
        # self.comment.insert(1.0,'this is paul')
        self.yscrol.config(command =self.comment.yview)
        self.xscrol.config(command =self.comment.xview)
        self.yscrol.pack(side="left" , anchor = E, fill =BOTH)
        self.xscrol.pack(side="top", anchor = W, fill =BOTH)
        self.statusbarfm = Frame(self.root)
        self.linecount = Label(self.statusbarfm, text="")

        self.menubar()
        self.in_path = " "

        self.root.mainloop()
    
    def menubar(self):


        self.menubar = Menu(self.root, tearoff = 0)
        self.fileMenu = Menu(self.menubar, tearoff=0)
        # self.newPlogo = Image.open('hapus_16.png')
        # self.image = ImageTk.PhotoImage(self.newPlogo, master = self.root)
        self.fileMenu.add_command(label ="New Page", command = self.newPage,  accelerator ="Ctr+N")
        self.fileMenu.add_command(label ="New Window", command = self.newindowfile,  accelerator ="Ctr+shift+N")
        self.fileMenu.add_command(label ="Open", command = self.openfile,  accelerator ="Ctr+O")
        self.fileMenu.add_command(label ="Save", command = self.savefile,  accelerator ="Ctr+S")
        self.fileMenu.add_command(label ="Save As", command = self.saveAsfile,  accelerator ="Ctr+Shift+Z")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label ='Page Setup', command=self.pagesetup, compound="left")
        self.fileMenu.add_checkbutton(label ='Print', command=self.openfile, accelerator="ctrl+P")
        self.fileMenu.add_separator()
        self.fileMenu.add_checkbutton(label ='Exit', command=self.openfile)
        
       




        # to make the filemenu show on the menubar
        self.menubar.add_cascade(label='File',menu=self.fileMenu, underline =1)
        # to make the menubar show on the root window
        # self.root.config(menu=self.menubar)

        # THIS IS THE SECTION FOR THIS EDIT PART
        self.EditMenu = Menu(self.menubar, tearoff=0)
        # self.newPlogo = Image.open('hapus_16.png')
        # self.image = ImageTk.PhotoImage(self.newPlogo, master = self.root)
        self.EditMenu.add_command(label ="Undo", command = self.undofile,  accelerator ="Ctr+Z")
        self.EditMenu.add_command(label ="Redo", command = self.redofile,  accelerator ="Ctr+Z")
        self.EditMenu.add_separator()
        self.EditMenu.add_command(label ="Cut", command = self.cutfile,  accelerator ="Ctr+X")
        self.EditMenu.add_command(label ="Copy", command = self.copyfile,  accelerator ="Ctr+C")
        self.EditMenu.add_command(label ="Paste", command = self.pastefile,  accelerator ="Ctr+V")
        self.EditMenu.add_command(label ="Delete", command = self.Deletefile,  accelerator ="Del")
        self.EditMenu.add_separator()
        self.EditMenu.add_command(label ="Searching with Bing", command = self.EditMenu,  accelerator ="Ctr+E")
        self.EditMenu.add_command(label ="Find/Replaces", command = self.findmenu,  accelerator ="Ctr+F")
        self.EditMenu.add_command(label ="Find Next", command = self.findnext,  accelerator ="Ctr+F3")
        self.EditMenu.add_command(label ="Find Previous", command = self.EditMenu,  accelerator ="Shift+F3")
        

        self.EditMenu.add_command(label ="Go To", command = self.goto,  accelerator ="Ctrl+G")
        self.EditMenu.add_separator()
        self.EditMenu.add_command(label="Selet All", command =self.seletall, accelerator="Crtl+A")
        self.EditMenu.add_command(label ="Time/Date", command = self.EditMenu,  accelerator ="F5") 
        self.menubar.add_cascade(label='Edit',menu=self.EditMenu, underline =1)


        # THIS IS THE SECTION FOR THIS FORMAT PART

        self.FormatMenu = Menu(self.menubar, tearoff=0)
        self.FormatMenu.add_command(label ="Word Wrap", command = self.FormatMenu)
        self.FormatMenu.add_command(label ="Font", command = self.font)
        self.FormatMenu.add_command(label ="Color", command = self.getcolor,  accelerator ="Ctrl+H")
        self.bold = self.FormatMenu.add_command(label ="BoldText", command = self.boldtext1,  accelerator ="Ctrt+B")
        self.italic=  self.FormatMenu.add_command(label ="ItalicText", command = self.ItalicText1,  accelerator ="Ctrl+I")
        self.under=  self.FormatMenu.add_command(label ="Underline", command = self.underline1,  accelerator ="Ctrl+U")        
        self.menubar.add_cascade(label='Format',menu=self.FormatMenu, underline =1)

        # THIS IS THE SECTION FOR THIS VIEW PART
        self.ViewMenu = Menu(self.menubar, tearoff =0)

        #add submenu item to the file menu
        self.option = Menu(self.ViewMenu, tearoff =0)
        self.option.add_command(label='Zoon In', command =self.option, accelerator="Ctrl+Plus")
        self.option.add_command(label='Zoon Out', command =self.option, accelerator="Ctrl+Minus")
        self.option.add_command(label='Restore Default Zoom', command=self.option, accelerator="Ctrl+0")
        self.ViewMenu.add_cascade(label='Zoom',menu=self.option, underline =1)
        self.menubar.add_cascade(label='View',menu=self.ViewMenu, underline =1)
        self.link =self.ViewMenu.add_checkbutton(label ='Status Bar', command=self.statusbar1)



          # THIS IS THE SECTION FOR THIS HELP PART
        self.HelpMenu =Menu(self.menubar, tearoff =0)
        self.HelpMenu.add_command(label ="View Help", command = self.HelpMenu)
        self.HelpMenu.add_command(label ="Send Feedback", command = self.HelpMenu)
        self.HelpMenu.add_command(label ="About Notepad", command = self.HelpMenu) 
        self.menubar.add_cascade(label="Help", menu=self.HelpMenu, underline =1)


        self.root.config(menu=self.menubar)
        
















        # self.EditMenu.add_separator()
        # self.EditMenu.add_command(label ='Open', command=self.openfile, compound="left")
        #add submenu item to the file menu
        # self.option = Menu(self.EditMenu, tearoff =0)
        # self.option.add_command(label='option 1')
        # self.option.add_command(label='option 2')
        # self.option.add_command(label='option 3')
        # self.EditMenu.add_cascade(label='option',menu=self.option, underline =1)




        # to make the filemenu show on the menubar
        # to make the menubar show on the root window

    


    

        


    def newPage(self, Con="none"):
        msg = askyesnocancel("warning", "Do you want to save this page")
        if msg == True:
            self.savefile()
            self.comment.delete(1.0, 'end')
        elif msg == False:
            self.comment.delete(1.0, END)

    def saveAsfile(self):
        self.in_path = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Test Documents","*.txt")])
        try:
            # Try to save the file
            with open(self.in_path,"w") as self.infile:
                self.infile.write(self.comment.get(1.0, END))
                # change the window title
                # in_path.split("/")
                self.root.title(os.path.basename(self.in_path.split("/")[1]) + " - paulTextEditor")
        except:
            pass
            
    def savefile(self):
        if self.in_path == " ":
            self.saveAsfile()
        else:
             with open(self.in_path,"w") as self.infile:
                self.infile.write(self.comment.get(1.0, END))


            

      

    def openfile(self):
        self.in_path = askopenfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Test Documents","*.txt")])
        try:
            # Try to save the file
            with open(self.in_path,"r") as self.infile:
                self.comment.delete(1.0, END)
                myfile = self.infile.read()
                self.comment.insert(1.0, myfile, END)
                self.root.title(os.path.basename(self.in_path.split("/")[1]) + " - paulTextEditor")
        except:
            pass

    def newindowfile(self):
        mynewwindow = TextEditor()

    def undofile(self):
        try:
            self.comment.event_generate("<<Undo>>")
        except:
            showinfo("Massage", "Nothing to Undo")

    def  redofile(self):
        try:
            self.comment.event_generate("<<Redo>>")
        except:
            showinfo("Massage", "You need to undo before you can redo")


    def cutfile(self):
        self.comment.event_generate("<<Cut>>")

    
    def copyfile(self):
        self.comment.event_generate("<<Copy>>")

    
    def pastefile(self):
        self.comment.event_generate("<<Paste>>")

    def  Deletefile(self):
        try:
            self.comment.delete(SEL_FIRST, SEL_LAST)
        except:
            showinfo("Massage", "Select portion of text to delete")


    def seletall(self):
        try:
            self.comment.tag_add(SEL, 1.0, END)
            self.comment.mark_set(INSERT,1.0)
            self.comment.see(INSERT)
            return 'break'
        except:
            showinfo("Selete", "Nothing to select")


    def goto(self):
        pass


    def pagesetup(self):
        self.setup = Toplevel()
        self.setup.geometry("500x400")
        self.setup.title("page setup")
        # self.page = Frame (self.setup)
        # self.page.pack(side="left")
        self.lb = LabelFrame(self.setup ,text ="Paper")
        # self.lb.grid(row=0, column =0)
        self.lb.grid(row= 0, column =0,columnspan =5, pady =5,padx=4)
        self.lb1 = Label(self.lb, text ="size: ")
        self.lb1.grid(row =0, column =0)
        self.cb = ttk.Combobox(self.lb, width=35, values =("1","2", "3", "4", "5"))
        self.cb.set("1")
        self.cb.grid(row=0, column=1)
        self.cb.bind('<<ComboboxSelected>>')
        # self.lb2.grid(anchor=NW, side = "left", padx=5)
        self.lb2 = Label(self.lb, text ="source: ")
        # self.lb1.grid(row = 0, column =1)
        self.lb2.grid(row =1, column=0)
        self.cb1 = ttk.Combobox(self.lb, width =35)
        self.cb1.set("1")
        self.cb1.grid(row=1,column =1)
        self.cb1.bind('<<ComboboxSelected>>')

        self.oren =LabelFrame(self.setup, text="orientation")
        self.oren.grid(row =1, column =0, pady=5,padx=10)
        # self.orr=Frame(self.oren)
        # self.orr.pack()
        # Radiobutton(self.orr, variable= congroup, text="A", value ='a', tristatevalue =0).grid(row=0, column=0)
        Radiobutton(self.oren,  text="Protrait", value ='a', tristatevalue =0).grid(row=0, column=0)
        Radiobutton(self.oren,  text="Landscape", value ='b', tristatevalue =0).grid(row=1, column=0)


        self.margin =LabelFrame(self.setup, text ="Margins (inchies)")
        self.margin.grid(row= 1, column=1, pady =5,padx=4)
        # self.marg =Frame(self.margin)
        # self.marg.pack()
        Label(self.margin,text="Left:").grid(row=0, column =0)
        self.ent=Entry(self.margin,width =6)
        self.ent.grid(row=0, column =1)
        Label(self.margin, text="Right:").grid(row=0, column =4, padx=5)
        self.ent2=Entry(self.margin, width =6, )
        self.ent2.grid(row=0, column =6)
        Label(self.margin, text= "Top").grid(row=1, column=0)
        self.top =Entry(self.margin, width =6)
        self.top.grid(row=1, column=1)
        Label(self.margin, text= "Bottom").grid(row=1, column=4, padx=5)
        self.bottom =Entry(self.margin, width =6)
        self.bottom.grid(row=1, column =6)






        self.preview =LabelFrame(self.setup, text="Preview")
        self.preview.grid(rowspan=2,row=0, column=12)
        Text(self.preview,height=10, width =10).grid(row=0, column=0, padx=3, pady=3)
        



        
        self.head=Label(self.setup, text ="Header:")
        self.head.grid( row =2,column=0)
        self.head1=Entry(self.setup, width = 20).grid(row=2, column=1)
        self.foot=Label(self.setup, text="Footer:")
        self.foot.grid(row=3)
        self.foot1=Entry(self.setup, width = 20).grid( row =3, column=1)


    def findmenu(self):
        self.find = Toplevel()
        self.find.geometry("300x150")
        self.find.title("Find")
        Label(self.find,text ="Find What: ").grid(row=0, column=0)
        self.finent=Entry(self.find, width=35)
        self.finent.grid(row=0, column=1, columnspan= 5)
        Label(self.find, text="Replaces: ").grid(row=1, column =0)
        self.repl = Entry(self.find, width=35)
        self.repl.grid(row=1, column=1, columnspan =5)
        Button(self.find, text="Find", command=self.findnext).grid(row=2,column=0)
        Button(self.find, text="Replaces",command=self.replaceit).grid(row=2,column=2)
        Button(self.find, text="Ok",command='').grid(row=2,column=4)


        # Button(self.find, text="Find Next").grid(row=0, column=7)
        # Button(self.find, text="Cancel").grid(row=1, column=7)
        # self.labb=LabelFrame(self.find, text="Direction")
        # self.labb.grid(row=1, column=5)
        # Radiobutton(self.labb,  text="Up", value ='a', tristatevalue =0).grid(row=0, column=0)
        # Radiobutton(self.labb,  text="Down", value ='b', tristatevalue =0).grid(row=0, column=1)
        # Checkbutton(self.find).grid(row=2, column=0)
        # Label(self.find,text="Match case").grid(row=2, column=1)
        # Checkbutton(self.find).grid(row=3, column=0)
        # Label(self.find,text="Wrap around").grid(row=3, column=1)

    def findnext(self):
        start ="1.0"
        end="end"
        start = self.comment.index(start)
        end =self.comment.index(end)
        count =IntVar()
        count = count
        self.comment.mark_set("matchStart", start)
        self.comment.mark_set("matchEnd", start)
        self.comment.mark_set("searchLimit", end)
        targetfind =self.finent.get()
        if targetfind:
            while True:
                where = self.comment.search(targetfind, "matchEnd", "searchLimit","marchStart", count = count)
                if where =="":
                    break
                elif where:
                    pastit = where + ('+%dc' % len(targetfind))
                    self.comment.mark_set("matchStart", where)
                    self.comment.mark_set("matchEnd", "%s+%sc" % (where, count.get()))
                    self.comment.tag_add(SEL , where , pastit)
                    self.comment.see(INSERT)
                    self.comment.focus()

        # self.comment.tag_remove(SEL, '1.0', END)

    def replaceit(self):
        self.bodytxt = self.comment.get(1.0, END)
        self.finded = self.finent.get()
        self.replacew = self.repl.get()
        self.bodytxt2 = self.bodytxt.replace(self.finded, self.replacew)
        self.comment.replace(1.0 ,END, self.bodytxt2)
    




                        

        # def CurSelet(evt):
        #     value =str(self.kombobox.get(self.kombobox.CurSeletion()))
        #     print(value)

        # self.mylistbox=Listbox(self.setup,width=60,height=10,font=('times',13))
        # self.mylistbox.bind('<<ListboxSelect>>',CurSelet)
        # self.mylistbox.place(x=32,y=90)

        # for items in itemsforlistbox:
        #     self.mylistbox.insert(END, items)


    def getcolor(self):
        (rgb , color) =colorchooser.askcolor()
        self.comment.tag_add("color1", SEL_FIRST , SEL_LAST)
        self.comment.tag_config("color1", foreground = color)

    def boldtext1(self):
        try:
            if self.bold == self.bold:
                self.comment.tag_add("bold1", SEL_FIRST , SEL_LAST)
                self.comment.tag_config("bold1", font=('bold'))
            else:
                self.comment.tag_remove("bold1", SEL_FIRST , SEL_LAST)

        except:
            pass

        
    def ItalicText1(self):
        try:
            if self.italic == self.italic:
                self.comment.tag_add("italic1", SEL_FIRST , SEL_LAST)
                self.comment.tag_config("italic1", font=('italic'))
            else:
                self.comment.tag_remove("italic1", SEL_FIRST , SEL_LAST)

        except:
            pass

    def underline1(self):
        # try:
        if self.under == self.under:
            self.comment.tag_add("underline1", SEL_FIRST, SEL_LAST)
            self.comment.tag_config("underline1", underline = True)
        else:
            self.comment.tag_remove("underline1", SEL_FIRST, SEL_LAST, underline = False)
        # except:
        #     pass

    

    def statusbar(self, event):
        list1=self.comment.index(INSERT).split('.')
        statusbar ="Line= "+str(self.comment.count('1.0', END, 'lines'))+", Cursor Position = row: "+list1[0]+", col: "+list1[1]+",  wordcount= "+str(len(self.comment.get('1.0', 'end-1c').split()))
        self.linecount.config(text=statusbar)
    def statusbar1(self):
        if self.link ==True:
            print("ggod")
            self.statusbar()
                
        else:
            self.statusbarfm.destroy()

    def  statusbar(self, event):
        self.statusbarfm = Frame(self.root)
        self.statusbarfm.pack(side =TOP, expand =YES, fill =BOTH, anchor =W)
        self.statusbarfm.grid_propagate(0)
        self.linecount = Label(self.statusbarfm, text=" ")
        self.linecount.pack(side =LEFT)


    def font(self):
        self.font = Toplevel()
        self.font.geometry("450x400")
        self.font.title("font")
        # self.font1 = Frame (self.font)
        # self.font1.pack()
        Label(self.font, text="Font: ").grid(row=0,column=0)
        self.fien=Entry(self.font,width =22).grid(row=1,column=0)
        # self.lis =Listbox(self.font,width=20 )
        # self.lis.grid(row=2,column=0)
        itemsforlistbox=['consolas','constantia','cooper','COPPERPLATE GOTHIC','corbel','countryBlueprint','Time New','consolas','constantia','cooper','COPPERPLATE GOTHIC','corbel','countryBlueprint','Time New']
        mylistbox=Listbox(self.font,width=15,height=10,font=('times',13))

        mylistbox.bind=('<<ListboxSelect>>')
        mylistbox.grid(row=2,column=0)
        # yscroll = Scrollbar(mylistbox, orient = "vertical")

        # yscroll.config(command =mylistbox.yview)
        # self.yscrol.pack(side="left" , anchor = E, fill =BOTH)
        
        for items in itemsforlistbox:
            mylistbox.insert(END, items)



        Label(self.font, text="Font style: ").grid(row=0,column=2,padx=10)
        self.fien=Entry(self.font,width =22).grid(row=1,column=2,padx=10)
        itemsforlistbox=['Regular','Italic','Bold','Bold Italic','kkkk','six','seven']
        mylistbox=Listbox(self.font,width=15,height=10,font=('times',13))
        mylistbox.bind('<<ListboxSelect>>')
        mylistbox.grid(row=2,column=2,padx=10)

        for items in itemsforlistbox:
            mylistbox.insert(END, items)

        # self.lis =Listbox(self.font,width=20 )
        # self.lis.grid(row=2,column=2,padx=5)
        Label(self.font, text="Size: ").grid(row=0,column=3 )
        self.fien=Entry(self.font,width =22).grid(row=1,column=3)
        itemsforlistbox=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        mylistbox=Listbox(self.font,width=15,height=10,font=('times',13))
        mylistbox.bind('<<ListboxSelect>>')
        mylistbox.grid(row=2,column=3)
        for items in itemsforlistbox:
            mylistbox.insert(END, items)
        # self.lis =Listbox(self.font,width=20 )
        # self.lis.grid(row=2,column=3, padx=5)

        self.samfont=LabelFrame(self.font, text ="Sample")
        self.samfont.grid(row=3, column=3)
        self.sam=Label(self.samfont, text ="AaBbYyZz")
        self.sam.grid(row=0,column =0)

        self.scri=Label(self.font, text="Script: ")
        self.scri.grid(row=4,column=3)
        self.scrr = ttk.Combobox(self.font, width=20, values =("Western"," "))
        self.scrr.set("1")
        self.scrr.grid(row=5, column=3)
        self.scrr.bind('<<ComboboxSelected>>')


        Button(self.font, text="Ok").grid(row =7, column=2)
        Button(self.font, text="Cancel").grid(row =7, column=3)


      
        
        




            
        
        
    
te = TextEditor()