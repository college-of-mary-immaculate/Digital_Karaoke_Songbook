from tkinter import Tk
from widgetsfactory import WidgetFactory
from PIL import Image, ImageTk

class AboutUsUI(WidgetFactory):
    def front(self):
        # window_about_us = WidgetFactory.create_new_window(
        #     self, "About Us", "1000x600")
        
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = WidgetFactory.create_canvas(self, '1000', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= 'nw' , image=img)
        label_about = WidgetFactory.create_label(
            self, "About Digital Songbook", ('Times New Roman', 16), "sunken")
        label_about.place(x=400, y=10)

        label1 = WidgetFactory.create_label(
            self, "Welcome to Digital Songbook,\nour comprehensive digital songbook designed for music enthusiasts, performers, and educators. \nOur mission is to make music accessible, organized, and enjoyable for everyone,\n whether you're a professional musician or a passionate hobbyist.", ("Arial", 12), "flat")
        label1.place(x=150, y=60)

        label2 = WidgetFactory.create_label(
            self, "Our Mission", ('Times New Roman', 16), "sunken")
        label2.place(x=450, y=165)

        label3 = WidgetFactory.create_label(
            self, "At Digital Songbook,we believe in the power of music to inspire, connect, and uplift.\n Our goal is to provide an intuitive, feature-rich platform that simplifies the way you access and manage your favorite songs,\n sheet music, and lyrics that you can use to connect in Karaoke.", ('Arial', 12), "flat")
        label3.place(x=80, y=220)

        label4 = WidgetFactory.create_label(
            self, "Contact Us", ('Times New Roman', 16), "sunken")
        label4.place(x=450, y=310)

        label5 = WidgetFactory.create_label(
            self, "Have any questions, suggestions, or need assistance? Our dedicated support team is here to help.\nContact us at support@digitalsongbook.com or follow us on social media for updates, tips, and exclusive content.", ('Arial', 12), "flat")
        label5.place(x=80, y=360)

        label6 = WidgetFactory.create_label(
            self, "Join Digital Songbook today and take your musical journey to new heights!", ('Times New Roman', 12), "sunken")
        label6.place(x=90, y=500)

        # button_mainmenu = WidgetFactory.create_button(
        #     self, "Main menu", 20, 3, '#e1dbd6')
        # button_mainmenu.place(x=820, y=500)


if __name__ == "__main__":

    about_us = AboutUsUI()
    about_us.front()
    about_us.display()
