import tkinter as tk
from tkinter import messagebox, OptionMenu



class Widgets_Factory:
        
    def create_new_window(self,title, size):
        self.root= tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.root.configure(bg= 'black')
        self.root.resizable(width= False, height= False)
    
    def create_label(self,text,fontsize, color):
        label= tk.Label(self.root, text= text, font= ('Arial', fontsize), bg= 'papaya whip', fg=color)
        return label
    
    def create_label2(self, text):
        bbtn=tk.Label(self.root, text=text, fg='hot pink', font=('Times', 25, 'bold'), bg='black', border= 10)
        return bbtn
    
    def create_textbox(self, h, w):
        textbox= tk.Text(self.root,height=h,width= w,font= ("Arial",15))
        return textbox
    
    def create_entry(self):
        entry= tk.Entry(self.root, width=50)
        return entry
    
    def create_listbox2(self):
        lb= tk.Listbox(self.root,width= 60)
        return lb
    def create_simple_button(self, text, func, color,w,h):
        bttn= tk.Button(self.root, text= text, width= w, height= h, bg= color, command= func)
        return bttn
    
    def create_button(self,text,bwidth,bheight,color,function, fcolor,fsize):
        bttn = tk.Button(self.root, text=text, fg=fcolor, width=bwidth, height=bheight, bg=color, font=('Arial', fsize),command=lambda: self.close_window_and_execute(function))
        
        return bttn
    def create_button2(self,text,bwidth,bheight,color,function, fcolor,fsize):
        bttn = tk.Button(self.root, text=text, fg=fcolor, width=bwidth, height=bheight, bg=color, font=('Arial', fsize),command=function)
        
        return bttn
        
    def button3(self,text,bwidth,bheight,color,function, fcolor,fsize):
        bttn = tk.Button(self.root, text=text, fg=fcolor, width=bwidth, height=bheight, bg=color, font=('Arial', fsize),command= function)
        
        return bttn
    def close_window_and_execute(self, function):
        if self.root:
           
           self.root.destroy()
        function()
    def create_main_button(self, text, function, account_type):
        button= tk.Button(self.root, text= text, width= 20, height= 3, bg= '#21aa47', borderwidth=0, command= lambda:[self.root.destroy(), function(account_type)])
        return button 
    def create_messagebox(self, message1, message2):
        messagebox.showerror(message1, message2 )    
        
    def clear_textbox(self, *textboxes):
        for textbox in  textboxes:
            textbox.delete('1.0', 'end-1c' )
    def image_button(self, img, w, h, function):
        img_button= tk.Button(self.root, image= img, width=w, height= h,command=lambda: self.close_window_and_execute(function))
        return img_button
    def image_button2(self, img, w, h, function):
        img_button= tk.Button(self.root, image= img, width=w, height= h,command=function)
        return img_button
    def create_canvas(self, w, h):
        canvas = tk.Canvas(self.root, width= w, height=h)
        return canvas
    
    def scrollbar(self):
        scrollbar = tk.Scrollbar(self.root, orient="horizontal")
        scrollbar.pack(fill="x")
        return scrollbar        
    
    def create_listbox(self, w, h, fsize, fcolor, bgcolor, items=None):
        listbox= tk.Listbox(self.root, width=w, height=h, font=('Arial', fsize), fg= fcolor, selectmode= tk.SINGLE, bg= bgcolor)
        if items:
            for item in items:
                listbox.insert(tk.END, item)
        return listbox
    def insert_lb(self, item):
        insert= insert(self.root.END, item)
        return insert
    
    def option(self, value, options):
        optionmenu= tk.OptionMenu(self.root, value, options)
        return optionmenu
    
    def create_scale(self, frm, to, ornt, command, label):
        scale = tk.Scale(self.root, from_=frm, to=to, orient=ornt, command=lambda value: command(value, label))
        return scale

    def create_scale2(self, frm, to, ornt, slength, color, w):
        scale= tk.Scale(self.root, from_= frm, to= to, orient= ornt, length= slength, bg=color, width=w)
        return scale
    
    def create_frame(self, w, h, bgc):
        frame= tk.Frame(self.root, width= w, height= h, bg= bgc, highlightbackground= 'black', highlightthickness=2)
        return frame
    def display(self):
         return self.root.mainloop() 
     
    def show_bttn(self,txt,w, h, bgc, fgc, window1, window2):
        bttn= tk.Button(self.root,text= txt, width=w, height=h, bg= bgc, fg= fgc, command= lambda: self.show_window(window1, window2) )
        return bttn
    def hide_bttn(self,txt,w, h, bgc, fgc, window1, window2):
        
        bttn= tk.Button(self.root, text= txt,width=w, height=h, bg= bgc, fg= fgc, command= lambda: self.hide_window(window1, window2) )
        return bttn

    @staticmethod
    def show_window(window, hide_window=None):
        if window is not None:
            window.deiconify()
        if hide_window is not None:
            hide_window.withdraw()

    @staticmethod
    def hide_window(window, show_window=None):
        if window is not None:
            window.withdraw()
        if show_window is not None:
            show_window.deiconify()
    
    
