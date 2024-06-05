import tkinter as tk
from tkinter import messagebox


class WidgetFactory:
    def __init__(self):
        self.root = None

    def create_new_window(self, title, size):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)
        self.root.configure(bg='gray7')
        self.root.resizable(width=False, height=False)

    @staticmethod
    def create_label(factory, text, font, relief):
        label = tk.Label(factory.root, text=text,
                         font=font, bg='#ceb5b7', bd=2, relief=relief)
        return label

    # def create_textbox(self):
    #     textbox = tk.Text(self.root, height=0, width=15, font=("Arial", 15))
    #     return textbox

    def create_simple_button(self, text, func):
        bttn = tk.Button(self.root, text=text, width=5,
                         height=1, bg='#e1dbd6', command=func)
        return bttn
# , func, command=func

    def create_button(self, text, bwidth, bheight, color):
        bttn = tk.Button(self.root, text=text, width=bwidth, height=bheight,
                         bg=color, command=lambda: self.root.destroy())
        return bttn

        # , function(), function

    def create_playlist_button(self, text, width, height, bg, function):
        button = tk.Button(self.root, text=text, width=width, height=height, bg=bg, command=lambda: [
                           self.root.destroy(), function()])
        return button

    def create_messagebox(self, message1, message2):
        messagebox.showerror(message1, message2)

    def clear_textbox(self, *textboxes):
        for textbox in textboxes:
            textbox.delete('1.0', 'end-1c')

    def create_listbox(self, width, height):
        listbox = tk.Listbox(self.root, width=width, height=height)
        return listbox

    def create_entry(self, width, default_text=None):
        entry = tk.Entry(self.root, width=width)
        if default_text:
            entry.insert(0, default_text)
            entry.bind("<FocusIn>", lambda event,
                       entry=entry: WidgetFactory.clear_default_text(event, entry))
            entry.bind("<FocusOut>", lambda event, entry=entry,
                       default_text=default_text: WidgetFactory.restore_default_text(event, entry, default_text))
        return entry

    def on_entry_click(self, event, textbox, default_text=None):
        if textbox.get("1.0", "end-1c") == default_text:
            textbox.delete('1.0', 'end-1c')

    def on_focus_out(self, event, textbox, default_text=None):
        if textbox.get("1.0", "end-1c") == "":
            textbox.insert(tk.END, default_text)

    def clear_default_text(event, entry):
        if entry.get() == entry:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def restore_default_text(event, entry, default_text):
        if entry.get() == '':
            entry.insert(0, default_text)
            entry.config(fg='grey')

    def create_text(self, height, width):
        text = tk.Text(self.root, height=height, width=width)
        return text

    def create_textbox(self, default_text=None):
        textbox = tk.Text(self.root, height=0, width=15, font=("Arial", 10))
        if default_text:
            textbox.insert(tk.END, default_text)
            textbox.bind("<FocusIn>", lambda event, textbox=textbox,
                         default_text=default_text: self.on_entry_click(event, textbox, default_text))
            textbox.bind("<FocusOut>", lambda event, textbox=textbox,
                         default_text=default_text: self.on_focus_out(event, textbox, default_text))
        return textbox

    def create_scrollbar(self, widget):
        scrollbar = tk.Scrollbar(self.root, command=widget.yview)
        widget.config(yscrollcommand=scrollbar.set)
        return scrollbar

    def image_button(self, img, w, h, function):
        img_button = tk.Button(self.root, image=img, width=w, height=h,
                               command=lambda: self.close_window_and_execute(function))
        return img_button
    def close_window_and_execute(self, function):
        if self.root:
           
           self.root.destroy()
        function()

    def image_button2(self, img, w, h, function):
        img_button = tk.Button(self.root, image=img,
                               width=w, height=h, command=function)
        return img_button

    def create_canvas(self, w, h):
        canvas = tk.Canvas(self.root, width=w, height=h)
        return canvas

    def display(self):
        return self.root.mainloop()
