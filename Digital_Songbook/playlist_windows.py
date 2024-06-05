import tkinter as Tk
import json
from widgetsfactory import WidgetFactory
from PIL import Image, ImageTk

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
        button_engsongs.place(x=90, y=160)

        
        photo5= Image.open(r"C:\Users\asus\Pictures\kpm.jpg")
        photo_rs5= photo5.resize((400,400))
        kpopg= ImageTk.PhotoImage(photo_rs5)
        button_ksongs = WidgetFactory.image_button(self,kpopg, '400', '400', self.kpop_songs )
        button_ksongs.place(x=510, y=160)

        # button_mainmenu = WidgetFactory.create_button(
        #     self, "Main menu", 20, 3, '#e1dbd6')
        # button_mainmenu.place(x=830, y=480)
        self.display()
    def popular_eng_songs(self):
        recent_searches = []

        windowengsongs = WidgetFactory.create_new_window(
            self, "Popular English Songs", "1000x600")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = WidgetFactory.create_canvas(self, '1000', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= 'nw' , image=img)
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
        windowengsongs = WidgetFactory.create_new_window(
            self, "Kpop Songs", "1000x600")
        original_image = Image.open(r"C:\Users\asus\Pictures\4blur.jpg")
        resized_image = original_image.resize((1000, 600))
        img = ImageTk.PhotoImage(resized_image)
        canvas = WidgetFactory.create_canvas(self, '1000', '600')
        canvas.pack(fill="both", expand= True)
        canvas.create_image(0, 0, anchor= 'nw' , image=img)
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


if __name__ == "__main__":

    playlist_ui = playlist_windows()
    playlist_ui.front()
    playlist_ui.display()
