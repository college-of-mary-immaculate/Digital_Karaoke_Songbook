from widgets_factory import Widgets_Factory
from about_us import AboutUsUI
from lyricswindows import Lyrics_section
from widgetsfactory import WidgetFactory


from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from PIL import ImageTk, Image, ImageFilter, ImageSequence

import threading
import lyricsgenius
import time
import json

class Main(Widgets_Factory):
    """root= Tk()
    root.geometry("1000x500")"""
    def front(self):
        
        front= Widgets_Factory.create_new_window(self, "KARAOKE SONG BOOK", '1000x500')
        #img= ImageTk.PhotoImage(Image.open(r"C:\Users\asus\Downloads\istockphoto-1226361494-612x612.jpg"))"C:\Users\asus\Pictures\karaoke2.jpg"
        original_image = Image.open(r"C:\Users\asus\Pictures\4.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        print(img)
        canvas = Canvas(self.root, width=1000, height=500)
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        
        enter_bttn= Widgets_Factory.create_button(self, "ENTER",'7', '1', 'black', self.home,'hot pink','15')
        enter_bttn.place(x=465, y=440)

        self.display()
    def home(self):
        home= Widgets_Factory.create_new_window(self, "HOME", "1000x500")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        photo= Image.open(r"C:\Users\asus\Pictures\songb.jpg")
        photo_rs= photo.resize((220,160))
        songbook_img= ImageTk.PhotoImage(photo_rs)
        songbook_bttn= Widgets_Factory.image_button(self, songbook_img, '220', '160', self.songbook)
        songbook_bttn.place(x= 400, y= 55)
        
         
        photo1= Image.open(r"C:\Users\asus\Pictures\lyrics.jpg")
        photo_rs1= photo1.resize((220,160)) 
        lyrics_img= ImageTk.PhotoImage(photo_rs1)
        lyrics_bttn= Widgets_Factory.image_button(self, lyrics_img, '220', '160', self.lyrics)
        lyrics_bttn.place(x= 140, y= 55)
        
        photo2= Image.open(r"C:\Users\asus\Pictures\playlist.jpg")
        photo_rs2= photo2.resize((220,160)) 
        playlist_img= ImageTk.PhotoImage(photo_rs2)
        playlist_bttn= Widgets_Factory.image_button(self, playlist_img, '220', '160', self.playlist)
        playlist_bttn.place(x= 655, y=55)
        
        photo3= Image.open(r"C:\Users\asus\Pictures\settings.jpg")
        photo_rs3= photo3.resize((220,160))
        settings_img= ImageTk.PhotoImage(photo_rs3)
        settings_bttn= Widgets_Factory.image_button(self, settings_img, '220', '160', self.settings)
        settings_bttn.place(x= 140, y= 250)
        
        photo4= Image.open(r"C:\Users\asus\Pictures\Ttimebg.jpg")
        photo_rs4= photo4.resize((220,160))
        time_img= ImageTk.PhotoImage(photo_rs4)
        time_bttn= Widgets_Factory.image_button(self, time_img, '220', '160', self.time)
        time_bttn.place(x= 400, y= 250)
        
         
        photo5= Image.open(r"C:\Users\asus\Pictures\abtusimg.jpg")
        photo_rs5= photo5.resize((220,160))
        abtus_img= ImageTk.PhotoImage(photo_rs5)
        aboutus_bttn= Widgets_Factory.image_button(self, abtus_img, '220', '160', self.about_us)
        aboutus_bttn.place(x= 655, y=250)
        
        
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.front, 'white','15')
        back.place(x=900, y=450)
        
        """song_bttn= Widgets_Factory.create_button(self, "SONG \n BOOK", 30, 10, 'DeepPink2', None, 'white')
        song_bttn.place(x= 150, y=100)
        playlist_bttn= Widgets_Factory.create_button(self, "PLAYLIST", 30, 10, 'DeepPink2', None, 'white')
        playlist_bttn.place(x= 500, y= 100)"""
        
        
        self.display()
        
        
    def lyrics(self):
        windowlyrics = Widgets_Factory.create_new_window(
            self, "Lyrics Section", "1000x600")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        lyrics= Lyrics_section()
        lyrics.front()
        
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.home, 'white','15')
        back.place(x=900, y=450)
        
        self.display()
    def songbook(self):
        
        self.sb=SongBook()
        self.sb.song_book()
        
    def playlist(self):  
        playlist=playlist_windows()
        playlist.front()
        
        self.display()
        
    def about_us(self):
        window_about_us = Widgets_Factory.create_new_window(self, "About Us", "1000x600")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        abtus=AboutUsUI()
        abtus.front()
        
        back= Widgets_Factory.create_button(self, "Back", '5', '2', 'snow4', self.home, 'black', '15')
        back.place(x= 850, y=500)
        self.display()
        
    def settings(self):
        settings= Widgets_Factory.create_new_window(self, "SETTINGS", "1000x500")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
       
        audio= Widgets_Factory.create_button(self, "Audio \n Settings", '15', '5','hot pink', self.audio_settings, 'white', '20')
        audio.place(x=200, y=50)
        
        connection= Widgets_Factory.create_button(self, "Connection", '15', '5','spring green4', self.connection, 'white', '20')
        connection.place(x=500, y=50)
        
        ownersettings= Widgets_Factory.create_button(self, "References", '15', '5','gold', self.ownersettings, 'white', '20')
        ownersettings.place(x=200, y=250)
        
        feedback= Widgets_Factory.create_button(self, "Feedback", '15', '5','dark orchid', self.feedback, 'white', '20')
        feedback.place(x=500, y=250)
        
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.home, 'white', '20')
        back.place(x=900, y=400)
        
        
        
        self.display()
        
    def time(self):
       timer=Timer()
       timer.timer()
    def audio_settings(self):
        audio_settings= Widgets_Factory.create_new_window(self, "AUDIO SETTINGS", "1000x500")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        self.volume_lbl= Widgets_Factory.create_label(self, "Music Volume: ", '15', 'black')
        self.volume_lbl.place(x=30, y=50)
        self.volume_scale= Widgets_Factory.create_scale2(self, '0', '100', "horizontal", '500', 'pink3','20' )
        self.volume_scale.place(x= 200 , y=50)
        #self.volume_val= self.volume_scale.get()
        
        self.mic_lbl= Widgets_Factory.create_label(self, "Mic Volume: ", '15', 'black')
        self.mic_lbl.place(x=30, y=150)
        self.mic= Widgets_Factory.create_scale2(self, '0', '100', "horizontal", '500', 'pink3','20' )
        self.mic.place(x= 200 , y=150)
    
        self.tempo_lbl= Widgets_Factory.create_label(self, "Tempo : ", '15', 'black')
        self.tempo_lbl.place(x=30, y=250)
        self.tempo= Widgets_Factory.create_scale2(self, '0', '100', "horizontal", '500', 'pink3','20' )
        self.tempo.place(x= 200 , y=250)
    
        self.echo_lbl=Widgets_Factory.create_label(self, "Toggle Echo", '15', 'black')
        self.echo_lbl.place(x= 30, y=350)
        self.echo_on= Widgets_Factory.create_simple_button(self, "ON", self.on, 'hot pink', '7', '3')
        self.echo_on.place(x=200, y= 350 )
        self.echo_off= Widgets_Factory.create_simple_button(self, "OFF", self.off, 'hot pink', '7', '3')
        self.echo_off.place(x=300, y= 350 )
        
        
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.settings, 'white', '15')
        back.place(x=900, y=400)
        
        self.display()
        
    def on(self):
        messagebox.showinfo("Audio Settings", "Echo: On")
    def off(self):
        messagebox.showinfo("Audio Settings", "Echo: Off")
        
    def connection(self):
        
        connection= Widgets_Factory.create_new_window(self, "CONNECTION", "1000x500")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        lbl= Widgets_Factory.create_label(self, "Connected Devices", '20', 'black')
        lbl.place(x=30, y=100)
        
        items=['KARAOKE TV 1']
        self.lb= Widgets_Factory.create_listbox(self, '20', '4', '20', 'black', 'pink3', items)
        self.lb.place(x= 300, y=100)
        
        lbl2= Widgets_Factory.create_label(self, "Paired Devices", '20', 'black')
        lbl2.place(x=30, y= 300)
        
        paired=['KARAOKE TV2', 'KARAOKE TV3', 'KARAOKE TV 4']
        self.lb2= Widgets_Factory.create_listbox(self, '20', '5', '20', 'black', 'pink3', paired)
        self.lb2.place(x= 300, y=300)
        
        self.lb2.bind("<<ListboxSelect>>", lambda event: self.on_select())
        
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.settings, 'white', '15')
        back.place(x=900, y=400)
        self.display()
        
    def on_select(self):
        if self.lb2.curselection(): 
            selected_item = self.lb2.get(self.lb2.curselection())           
            if self.lb.size() > 0:
                connected_device = self.lb.get(0)
                self.lb2.insert("end", connected_device)
                self.lb.delete(0)

           
            self.lb.insert("end", selected_item)
            self.lb2.delete(self.lb2.curselection())



    def ownersettings(self):
        settings= Widgets_Factory.create_new_window(self, "REFERENCES", "1000x500")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        r_label= Widgets_Factory.create_label(self, "References and Links", '20', 'black')
        r_label.place(x=20, y=20)
        
        button_ref= Widgets_Factory.create_label(self, "IMAGES IN BUTTONS from: \n *Menu Buttons -Edited from canva \n *Playlist buttons- from Google and Pinterest", "15", 'black')
        button_ref.place(x= 200, y=80)
        
        data_ref= Widgets_Factory.create_label(self, "Song Title and Artist from: \n -https://www.javatpoint.com/list-of-popular-english-songs \n -https://grandvideoke.com.ph/download-files/songlist/grand-videoke/GRANDVIDEOKE_Englist_Built_in_Songs.pdf \n-https://joycemusic1.com/downloads/k-pop-songs/", "10", 'black')
        data_ref.place(x= 200, y=200)
        
        lyrics_ref= Widgets_Factory.create_label(self, "LYRICS ARE SCRAPED from: \n -https://genius.com/", "15", 'black')
        lyrics_ref.place(x= 200, y=300)
 
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.settings, 'white', '15')
        back.place(x=900, y=400)

        self.display()
    
    def feedback(self):
        self.rating = None
        self.comment = ""

        settings= Widgets_Factory.create_new_window(self, "FEEDBACK", "1000x500")
        
        original_image = Image.open(r"C:\Users\asus\Pictures\feedbackbg.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        write= Widgets_Factory.create_label(self, "Share your feedback with us", '23', 'black')
        write.place(x=30, y=20)
        
        question= Widgets_Factory.create_label(self, "How would you rate your experience with us?", '16', 'black')
        question.place(x= 80 ,y= 80)
        
        bad_bttn= Widgets_Factory.create_simple_button(self, "Bad", None, 'red', 25, 2, )
        bad_bttn.place(x= 100, y= 130)
        
        neutral_bttn= Widgets_Factory.create_simple_button(self, "Neutral", None, 'gray', 25, 2, )
        neutral_bttn.place(x= 300, y= 130)
         
        good_bttn= Widgets_Factory.create_simple_button(self, "Good", None, 'green', 25, 2, )
        good_bttn.place(x= 500, y= 130)
        
        great_bttn= Widgets_Factory.create_simple_button(self, "Great", None, 'gold', 25, 2, )
        great_bttn.place(x= 700, y= 130)
        
        comment_lbl= Widgets_Factory.create_label(self, "Comment:", '16', 'black')
        comment_lbl.place(x=80, y=200)
        
        comment_tb= Widgets_Factory.create_textbox(self, '6', '50')
        comment_tb.place(x=80, y=250)
        
        def save_rating(rating):
            self.rating = rating
            print(self.rating)
   
        # def save_comment():
        #     self.comment = comment_tb.get("1.0", "end-1c")  

          
        bad_bttn.config(command=lambda: save_rating("Bad"))
        neutral_bttn.config(command=lambda: save_rating("Neutral"))
        good_bttn.config(command=lambda: save_rating("Good"))
        great_bttn.config(command=lambda: save_rating("Great"))

        def submit_feedback():
            self.comment = comment_tb.get("1.0", "end-1c")
            self.save_feedback_data()
            
        
        submit_bttn= Widgets_Factory.create_simple_button(self, "Submit", submit_feedback, 'dark orchid', '10', '2')
        submit_bttn.place(x=700, y=350)
        
        back= Widgets_Factory.create_button(self, "Back", '4', '1','gray', self.settings, 'white', '15')
        back.place(x=20, y=400)

        self.display()
    
    def save_feedback_data(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feedback_data = {
            "rating": self.rating,
            "comment": self.comment,
            "date_and_time": current_datetime
        }
        
        with open("feedback_data.json", "r") as file:
            existing_feedback = json.load(file)
       

        existing_feedback.append(feedback_data)

        with open("feedback_data.json", "w") as file:
            json.dump(existing_feedback, file, indent=4)

        print("Feedback data saved to feedback_data.json")

        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        
        
class SongBook(Widgets_Factory):
    def __init__(self):
        self.queue=[]
        self.history=[]
        self.listbox_visible=False
        self.listbox2_visible=False
        self.history_lb=None
        self.songbook_window=None
        self.songbook_windowt=True
        self.lyrics_window= None
    def song_book(self):
        self.songbook_window= Widgets_Factory.create_new_window(self, "SONGBOOK", '1200x600')  
    
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1200, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1200', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        # side_frame= Widgets_Factory.create_frame(self, '300', '600', 'pink3')
        # side_frame.place(x=900, y=0)
        
       
        
        top_frame= Widgets_Factory. create_frame(self, '1199', '150', 'LightPink4')
        top_frame.place(x=2, y=0)
        
        side_frame= Widgets_Factory.create_frame(self, '300', '600', 'LightPink3')
        side_frame.place(x=900, y=0)
        
        sb_lbl= Widgets_Factory.create_label(self, "Search:", '15', 'black' )
        sb_lbl.place(x= 100, y=30)
        self.searchbar= Widgets_Factory.create_textbox(self,'1', '50')
        self.searchbar.place(x=200, y=30)
        
        # self.searchbar= Widgets_Factory.create_entry(self)
        # self.searchbar.place(x=330, y=60)
        self.searchbar.bind("<KeyRelease>", self.update_search_results)
        
     
        
        self.sorted_song_titles= self.load_and_display_songs()
                
        self.song_list= Widgets_Factory.create_listbox(self, '70', '16', '15', 'white','black',self.sorted_song_titles )
        self.song_list.place(x=90, y=170)
       
        
        self.song_list.bind('<<ListboxSelect>>', self.onselect)
        
        self.songplaying= Widgets_Factory.create_label(self, "Current Song: ", '12', 'black')
        self.songplaying.place(x=100, y= 70)
        
        self.nextsong= Widgets_Factory.create_label(self, " Next on  Queue: ", '12', 'black' )
        self.nextsong.place(x= 100, y=120)
        # BUTTONS
        
        self.play_bttn= Widgets_Factory.create_simple_button(self, "PLAY", self.play_song, 'hot pink', '30', '2')
        self.play_bttn.place(x= 930, y=190)
        
        self.reserve= Widgets_Factory.create_simple_button(self, "RESERVE", self.reserve_songs, 'orange', '30', '2')
        self.reserve.place(x=930, y=250)
        
        self.cancel= Widgets_Factory.create_simple_button(self, "CANCEL", self.cancel_song, 'gold', '30', '2')
        self.cancel.place(x=930, y=300)
        
        self.played_songs= Widgets_Factory.create_simple_button(self, "HISTORY", self.show_history, 'light green', '30', '2')
        self.played_songs.place(x=930, y=70)
        
        self.queue_list= Widgets_Factory.create_simple_button(self, "QUEUE", self.show_queue, 'steel blue', '30', '2')
        self.queue_list.place(x=930, y=130)
        
        # self.lyrics= Widgets_Factory.create_button(self, "lyrics", '35', '2', 'purple', self.show_lyrics, 'black', '10')
        self.lyrics= Widgets_Factory.create_button(self, "LYRICS", '30', '2', 'dark orchid', self.show_lyrics, 'black', '9')
        self.lyrics.place(x=930, y=350)
     
        
        self.dropdown= Widgets_Factory.create_listbox2(self)
        self.dropdown.pack()
        self.dropdown.lift()
        self.dropdown.bind("<<ListboxSelect>>", self.dropdownselected)

        
        self.main= Main()
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.main.home, 'white', '15')
        back.place(x=1000, y=550)
        self.display()
       
        
    def play_song(self):
        
        selected__song= self.onselect(None)
        song_selected= self.dropdownselected(None)
        if song_selected:
            self.history.append(song_selected)
            self.songplaying.config(text= f"Current Song: {song_selected}")
        if selected__song:
            self.history.append(selected__song)
            self.songplaying.config(text= f"Current Song: {selected__song}")
        
    def show_history(self):
    
        if self.listbox_visible:
            self.history_lb.place_forget()
            self.listbox_visible = False

        else:
            self.history_lb= Widgets_Factory.create_listbox(self, '35', '30', '10', 'black', 'white', self.history)

            self.history_lb.place(x=930, y= 150)
            self.listbox_visible=True
         
    def reserve_songs(self):
        selected_song= self.onselect(None)
        songselected= self.dropdownselected(None)
        
        if selected_song:
            self.queue.append(selected_song)
            self.nextsong.config(text= f"Next Song om Queue: {self.queue[0]}")
        elif songselected:
            self.queue.append(songselected)
           
            self.nextsong.config(text= f"Next song on queue: {self.queue[0]}")

        
    def show_queue(self):
        if self.listbox2_visible:
            self.queue_lb.place_forget()
            self.listbox2_visible = False

        else:
            self.queue_lb= Widgets_Factory.create_listbox(self, '35', '30', '10', 'black', 'white', self.queue)

            self.queue_lb.place(x=930, y= 250)
            self.listbox2_visible=True
        
        
        
    def cancel_song(self):
        if self.queue:
            current_song = self.queue.pop(0)
            self.songplaying.config(text="No song is playing")

            if self.queue:
                self.songplaying.config(text=f"{self.queue[0]} is Playing")
                next_song = self.queue[1] if len(self.queue) > 1 else None
                if next_song:
                    self.nextsong.config(text=f"Next song on queue: {next_song}")
                else:
                    self.nextsong.config(text="No next song on queue")
        
                
    def show_lyrics(self):
        self.lyrics_window= Widgets_Factory.create_new_window(self,"LYRICS", '1000x600')
        self.original_image = Image.open(r"C:\Users\asus\Pictures\karaoke.gif")
        self. frm=[ImageTk.PhotoImage(img.resize((1200, 400))) for img in ImageSequence.Iterator(self.original_image)]
        self.frm_idx=0
        
        self.canvas = Widgets_Factory.create_canvas(self, '1200', '400')
        self.canvas.pack(fill="both", expand= True)
        # canvas.create_image(0, 0, anchor= NW , image=img)
        
        ls=Lyrics_section()
        # ls.get_lyrics("bini", "pantropiko")
        display_frame= Widgets_Factory.create_frame(self, '1200', '250', 'LightPink4')
        display_frame.place(x=0, y=400)
       
        selectedsong= self.history[-1]
        if selectedsong:
             parts = selectedsong.split(' --- ')
        if len(parts) == 2:
            song_code = parts[0]
            song_info = parts[1]
            artist_song_parts = song_info.split(': by ')
            if len(artist_song_parts) == 2:
                
                song_name = artist_song_parts[0]
                artist = artist_song_parts[1]
                lyricsshow= ls.get_lyrics(artist, song_name)
                mainlbl= Widgets_Factory.create_label2(self, song_name)
                mainlbl.place(x= 100, y=100)
                if lyricsshow:
                    self.lyrics_lines = lyricsshow.split('\n') 
                    self.index=0
                    self.displaylyrics()
                    
                    
                    
            
        self.animate()
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.song_book, 'white', '15')
        back.place(x=10, y=10)
        
        self.display()
    def displaylyrics(self):
      
            if self.index < len(self.lyrics_lines):
                    l= self.lyrics_lines[self.index]
                   
                    self.line_display= Widgets_Factory.create_label2(self, l)
                    self.line_display.place(x=50, y=450)
                    self.root.after(2000, self.clear_label)
                    self.root.after(2000, self.displaylyrics)
                    self.index+=1
                    
    def clear_label(self):
        self.line_display.destroy()
    def animate(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=NW, image=self.frm[self.frm_idx])
        self.frm_idx = (self.frm_idx + 1) % len(self.frm)
        self.root.after(100, self.animate) 
    
    

    def onselect(self, event):
        get_selected = self.song_list.curselection()
        if get_selected:
            selected_song = self.song_list.get(get_selected[0]) 
            print(selected_song)
            return selected_song
        return None 
                
    def dropdownselected(self,event):
       
        selected_get = self.dropdown.curselection()
        if selected_get:
            self.selected_song = self.dropdown.get(selected_get)
            print("Selected from dropdown:", self.selected_song)
            self.searchbar.delete(1.0, END + "-1c")
            self.searchbar.insert(1.0, self.selected_song)
            self.dropdown.place_forget()
        return self.selected_song
        
    def sort_json(self):
        filepath= r"C:\Users\asus\Documents\songs.json"
        
       
        with open(filepath, 'r') as file:
            data = json.load(file)
        
        if isinstance(data, list):
                    
            filtered_data = [item for item in data if item.get('Song') is not None]
           
            sorted_data = sorted(filtered_data, key=lambda x: x.get('Song', '').lower())
         
            with open(filepath, 'w') as file:
                json.dump(sorted_data, file, indent=4)
               

    def update_search_results(self, event=None):
        search_query = self.searchbar.get(1.0, END + "-1c").lower()
        
        if not search_query.strip():
            self.dropdown.place_forget()
            return
        
        
        self.dropdown.delete(0, 'end')
        
        result = self.search_songs(search_query, self.sorted_song_titles)
        self.searched_result= []
        self.searched_result.append(result)
        for song in result:
            self.dropdown.insert("end", song)

        if result:
            self.dropdown.place(x=250, y=110)
        else:
            self.dropdown.place_forget()

        pass
        
    # def searching(self):
    #     self.searched = self.searchbar.get("1.0", "end-1c")
    #     self.search_songs(self.searched, self.sorted_song_titles)
        
    def edit_distance(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1

        return dp[len1][len2]
    
    def search_songs(self, query, song_list):
        result = []
        
        for song in song_list:
            parts = song.split(" --- ")
            if len(parts) == 2:
                song_code = parts[0].strip()
                song_details = parts[1].split(": by ")
                if len(song_details) == 2:
                    song_title = song_details[0].strip()
                    artist = song_details[1].strip()
                else:
                    song_title = song_details[0].strip()
                    artist = ""
            else:
                continue

            if query.lower() in song_code.lower() or query.lower() in song_title.lower() or query.lower() in artist.lower():
                result.append(song)
        
        print(result)
        return result
    def load_and_display_songs(self):
        file_path = r"C:\Users\asus\Documents\songs.json"
        
        with open(file_path, 'r') as file:
            data = json.load(file)
        if isinstance(data, list):
            filtered_data = [item for item in data if item.get('Song') is not None]
            sorted_data = sorted(filtered_data, key=lambda x: x.get('Song', '').lower())
            sorted_songs = [
                f"{item.get('Song Code', 'N/A')} --- {item.get('Song', 'N/A')}: by {item.get('Artist', 'N/A')}" 
                for item in sorted_data
            ]
            self.sorted_song_titles = sorted_songs  # Assign the list to an instance variable
            return sorted_songs
        else:
            print("The data is not a list.")
            return []
    def update_labels(self):
        self.nextsong.config(text=f"Current Song:{self.dropdown_selected}")

    
class Timer(Widgets_Factory):
    
    def timer(self):
        self.timer= Widgets_Factory.create_new_window(self, "TIME", '1000x500')
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 500))
        img = ImageTk.PhotoImage(resized_image)
        canvas = Widgets_Factory.create_canvas(self, '1000', '500')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= NW , image=img)
        
        start_bttn= Widgets_Factory.create_simple_button(self, "Start Time",self.start_timer,'hot pink','15','4')
        start_bttn.place(x=200, y=160)
        
        end_bttn= Widgets_Factory.create_simple_button(self, "End Time", self.end_time, 'hot pink', '15', '4')
        end_bttn.place(x= 690, y= 160)
        
        self.timer_lbl= Widgets_Factory.create_label(self,"00:00:00", '60', 'black')
        self.timer_lbl.place(x=350, y=80)
        
        self.fifteenmins_bttn= Widgets_Factory.create_simple_button(self, "Add 15 minutes \n Php 30", self.add_15mins, 'SkyBlue4', '12', '5')
        self.fifteenmins_bttn.place(x= 360, y= 200)
         
        self.thirtymins_bttn= Widgets_Factory.create_simple_button(self, "Add 30 minutes \n Php 60", self.add_30mins, 'SkyBlue4', '12', '5')
        self.thirtymins_bttn.place(x= 465, y= 200)
        
        self.onehour_bttn= Widgets_Factory.create_simple_button(self, "Add 1 hour \n Php 110", self.add_1hour, 'SkyBlue4', '12', '5')
        self.onehour_bttn.place(x= 570, y= 200)
        
        self.total_time_lbl= Widgets_Factory.create_label(self, "Total Karaoke Time: ", '12', 'black')
        self.total_time_lbl.place(x=50,y=320)
        
        self.total_rate_lbl= Widgets_Factory.create_label(self, "Total Karaoke Rate: ", '12', 'black')
        self.total_rate_lbl.place(x=50,y=380)
        
        self.total_time= 0
        self.total_rate=0
        
        
        
        self.running_time= False
        self.main= Main()
        #back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4',self.hide, 'white', '15')
        #back= Widgets_Factory.create_simple_button(self, "Back", self.hide_time_window, 'snow4', '4','1')
         
        back= Widgets_Factory.create_button(self, "Back", '4', '1','snow4', self.main.home, 'white', '20')
        back.place(x=900, y=400)
        
        self.thread = threading.Thread(target=self.update_timer)
        self.thread.daemon = True
        self.thread.start()
        self.display()
   
        
    def start_timer(self):
        if not self.running_time:
            self.running_time = True
            threading.Thread(target=self.update_timer).start()
            
            
    def end_time(self):
        self.total_time=0
        self.timer_lbl.config(text="00:00:00")
        
        
    def update_timer(self):
      
        if self.running_time:
            self.total_time -= 1
            if self.total_time < 0:
                self.total_time = 0
                self.running_time = False
                messagebox.showinfo("Times's Up!", "Your Karaoke time is over.")
            else:
                minutes, seconds = divmod(self.total_time, 60)
                hours, minutes = divmod(minutes, 60)
                self.timer_lbl.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
                # Schedule the next update after 1000 milliseconds (1 second)
                self.root.after(1000, self.update_timer)

                
    def add_time(self, time_in_minutes):
        self.total_time += time_in_minutes
        self.update_time_display()
        if time_in_minutes== 900: 
            self.total_rate += 30
        elif time_in_minutes == 1800:  
            self.total_rate += 60
        elif time_in_minutes == 3600:  
            self.total_rate += 110

        # Update the total rate label
        self.update_time_display()

    def add_15mins(self):
        self.add_time(900)
        self.total_rate +=30
    def add_30mins(self):
        self.add_time(1800)
        self.total_rate+=60
    def add_1hour(self):
        
        self.add_time(3600)
        self.total_rate+=110
    def update_time_display(self):
       
        #self.total_time_lbl.config(text=f"Total Karaoke Time: {self.total_time} minutes")

        hours, minutes = divmod(self.total_time, 60)
       
        self.total_time_lbl.config(text=f"Total Karaoke Time: {hours} minutes")
        self.total_rate_lbl.config(text=f"Total Karaoke Rate: {self.total_rate} Pesos")



class playlist_windows(WidgetFactory):
    def front(self):
        windowplaylist = WidgetFactory.create_new_window(
            self, "Tracklist", "1000x600")
        
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = WidgetFactory.create_canvas(self, '1000', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= 'nw' , image=img)
        labelplaylist = WidgetFactory.create_label(
            self, "Songbook Playlist", ('Times New Roman', 20), "sunken")
        labelplaylist.place(x=390, y=50)

        # button_engsongs = WidgetFactory.create_playlist_button(
        #     self, "Popular English Songs", 50, 10, '#EED6D3', self.popular_eng_songs)
        photo4= Image.open(r"C:\Users\asus\Pictures\pem.jpg")
        photo_rs4= photo4.resize((400,400))
        time_img= ImageTk.PhotoImage(photo_rs4)
        button_engsongs= WidgetFactory.image_button(self, time_img, '400', '400', self.popular_eng_songs )
        button_engsongs.place(x=90, y=120)

        
        photo5= Image.open(r"C:\Users\asus\Pictures\kpm.jpg")
        photo_rs5= photo5.resize((400,400))
        kpopg= ImageTk.PhotoImage(photo_rs5)
        button_ksongs = WidgetFactory.image_button(self,kpopg, '400', '400', self.kpop_songs )
        button_ksongs.place(x=510, y=120)

        self.main= Main()
        back= Widgets_Factory.create_button(self, "Back", '5', '2', 'snow4', self.main.home, 'black', '10')
        back.place(x= 900, y=550)
        # button_mainmenu = WidgetFactory.create_button(
        #     self, "Main menu", 20, 3, '#e1dbd6')
        # button_mainmenu.place(x=830, y=480)
        self.display()
    def popular_eng_songs(self):
        recent_searches = []

        windowengsongs = WidgetFactory.create_new_window(
            self, "Popular English Songs", "1000x600")
        
        labelplaylist = WidgetFactory.create_label(
            self, "Popular English Songs", ('Times New Roman', 20), "sunken")
        labelplaylist.place(x=480, y=50)
        
        def load_json(filename):
            with open(filename, 'r') as file:
                return json.load(file)

        titles = load_json(
            r"C:\Users\asus\Documents\New folder\popularenglishsongs.json")
        sorted_songs = sorted(titles.items(), key=lambda x: x[1]['title'])

        def edit_distance(str1, str2):
            len1 = len(str1)
            len2 = len(str2)
            dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

            for i in range(len1 + 1):
                dp[i][0] = i
            for j in range(len2 + 1):
                dp[0][j] = j

            for i in range(1, len1 + 1):
                for j in range(1, len2 + 1):
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1]) + 1
            return dp[len1][len2]

        def search_song(search, song_list):
            result = []
            for code, song_data in song_list.items():
                title = song_data['title']
                artist = song_data['artist']
                title_match = edit_distance(search, title)
                artist_match = edit_distance(search, artist)
                code_match = edit_distance(search, code)
                if search.lower() in title.lower() or search.lower() in artist.lower() or search == code:
                    result.append((title, artist, code))
                elif title_match <= len(search.lower()) // 2 or artist_match <= len(search.lower()) // 2 or code_match <= len(search.lower()) // 2:
                    result.append((title, artist, code))
            return result

        def search():
            query = self.search_entry.get()
            results = search_song(query, song_list)
            self.listbox_result.delete(0, "end")
            if results:
                for title, artist, code in results:
                    self.listbox_result.insert('end',
                                               f"{code}--{title} by {artist}")
            else:
                self.listbox_result.insert("end", "No results found.")

            if query not in recent_searches:
                recent_searches.append(query)
                self.listbox_recent_search.insert("end", query)

        song_list = load_json(
           r"C:\Users\asus\Documents\New folder\popularenglishsongs.json")

        self.search_entry = WidgetFactory.create_entry(
            self, 40, default_text="Search...")
        self.search_entry.place(x=460, y=115)

        self.listbox_result = WidgetFactory.create_listbox(
            self, 35, 5)
        self.listbox_result.place(x=770, y=10)

        buttonsearchplaylist = WidgetFactory.create_simple_button(
            self, "🔍", search)
        buttonsearchplaylist.place(x=720, y=110)

        self.listbox_search = WidgetFactory.create_listbox(
            self, 100, 20)
        self.listbox_search.place(x=300, y=150)
        listbox_scrollbar = WidgetFactory.create_scrollbar(
            self, self.listbox_search)
        listbox_scrollbar.place(x=43 + 43 * 20 + 2, y=150, height=20 * 16)

        for code, details in sorted_songs:
            entry = f"{code} |  {details['title']} | By: {details['artist']}"
            self.listbox_search.insert("end", entry)

        label_recent_research = WidgetFactory.create_label(
            self, "Recent Search", ('Times New Roman', 15), "sunken")
        label_recent_research.place(x=60, y=70)
        self.listbox_recent_search = WidgetFactory.create_listbox(
            self, 30, 20)
        self.listbox_recent_search.place(x=30, y=150)
        listbox_scrollbar = WidgetFactory.create_scrollbar(
            self, self.listbox_recent_search)
        listbox_scrollbar.place(x=5 + 26 * 8 + 2, y=150, height=20 * 16)

        button_back = WidgetFactory.create_playlist_button(
            self, "Back", 10, 3, '#EED6D3', self.front)
        button_back.place(x=850, y=480)

    def kpop_songs(self):
        recent_searches = []
        kpopsongs = WidgetFactory.create_new_window(
            self, "Kpop Songs", "1000x600")
        
        
        labelplaylist = WidgetFactory.create_label(
            self, "Kpop Songs", ('Times New Roman', 20), "sunken")
        labelplaylist.place(x=500, y=50)
        
        def load_json(filename):
            with open(filename, 'r') as file:
                return json.load(file)

        songs = load_json(r"C:\Users\asus\Documents\New folder\songdict.json")
        sorted_songs = sorted(songs.items(), key=lambda x: x[1]['Song'])
        
        

        def edit_distance(str1, str2):
            len1 = len(str1)
            len2 = len(str2)
            dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

            for i in range(len1 + 1):
                dp[i][0] = i
            for j in range(len2 + 1):
                dp[0][j] = j

            for i in range(1, len1 + 1):
                for j in range(1, len2 + 1):
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1]) + 1
            return dp[len1][len2]

        def search_song(search, song_list):
            result = []
            for code, song_data in song_list.items():
                title = song_data['Song']
                artist = song_data['Artist']
                title_match = edit_distance(search, title)
                artist_match = edit_distance(search, artist)
                code_match = edit_distance(search, code)
                if search.lower() in title.lower() or search.lower() in artist.lower() or search == code:
                    result.append((title, artist, code))
                elif title_match <= len(search.lower()) // 2 or artist_match <= len(search.lower()) // 2 or code_match <= len(search.lower()) // 2:
                    result.append((title, artist, code))
            return result

        def search():
            query = self.search_entry.get()
            results = search_song(query, song_list)
            self.listbox_result.delete(0, "end")
            if results:
                for title, artist, code in results:
                    self.listbox_result.insert('end',
                                               f"{code}--{title} by {artist}")
            else:
                self.listbox_result.insert("end", "No results found.")
            if query not in recent_searches:
                recent_searches.append(query)
                self.listbox_recent_search.insert("end", query)

        song_list = load_json(
           r"C:\Users\asus\Documents\New folder\songdict.json")

        self.search_entry = WidgetFactory.create_entry(
            self, 40, default_text="Search...")
        self.search_entry.place(x=380, y=115)

        self.listbox_result = WidgetFactory.create_listbox(
            self, 35, 5)
        self.listbox_result.place(x=770, y=10)

        buttonsearchplaylist = WidgetFactory.create_simple_button(
            self, "🔍", search)
        buttonsearchplaylist.place(x=720, y=110)

        self.listbox_search = WidgetFactory.create_listbox(
            self, 100, 20)
        self.listbox_search.place(x=300, y=150)
        listbox_scrollbar = WidgetFactory.create_scrollbar(
            self, self.listbox_search)
        listbox_scrollbar.place(x=43 + 43 * 20 + 2, y=150, height=20 * 16)

        for code, details in sorted_songs:
            entry = f"{code} |  {details['Song']} | By: {details['Artist']}"
            self.listbox_search.insert("end", entry)

        label_recent_research = WidgetFactory.create_label(
            self, "Recent Search", ('Times New Roman', 15), "sunken")
        label_recent_research.place(x=60, y=70)
        self.listbox_recent_search = WidgetFactory.create_listbox(
            self, 30, 20)
        self.listbox_recent_search.place(x=30, y=150)
        listbox_scrollbar = WidgetFactory.create_scrollbar(
            self, self.listbox_recent_search)
        listbox_scrollbar.place(x=5 + 26 * 8 + 2, y=150, height=20 * 16)

        button_back = WidgetFactory.create_playlist_button(
            self, "Back", 10, 3, '#EED6D3', self.front)
        button_back.place(x=850, y=480)




if __name__ =='__main__':    
    m=Main()
    m.front()
    
  