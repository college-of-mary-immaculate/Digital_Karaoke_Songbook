from tkinter import Tk
from tkinter import font, messagebox
from widgetsfactory import WidgetFactory
import lyricsgenius

genius = lyricsgenius.Genius(
    "BoJ7M5TKjUkW3qWWYDrQCzMsjH-zp2d3-1E4heKtxJtVujLqGjX1RSyytmHHlFhj")


class Lyrics_section(WidgetFactory):
    def __init__(self):
        super().__init__()
        self.recent_searches = []

    def front(self):

        # windowlyrics = WidgetFactory.create_new_window(
        #     self, "Lyrics Section", "1000x600")
        labelplaylist = WidgetFactory.create_label(
            self, "Lyrics Viewer", ('Times New Roman', 20), "sunken")
        labelplaylist.place(x=430, y=10)

        self.artist_entry = WidgetFactory.create_entry(
            self, 40, default_text="Search artist...")
        self.artist_entry.place(x=380, y=65)
        self.song_entry = WidgetFactory.create_entry(
            self, 40, default_text="Search song...")
        self.song_entry.place(x=380, y=105)

        buttonsearchplaylist = WidgetFactory.create_simple_button(
            self, "🔍", self.fetch_lyrics)
        buttonsearchplaylist.place(x=630, y=80)

        self.result_text = WidgetFactory.create_text(
            self, height=20, width=60)
        self.result_text.place(x=290, y=150)
        text_scrollbar = WidgetFactory.create_scrollbar(
            self, self.result_text)
        text_scrollbar.place(x=290 + 60 * 8 + 5, y=150, height=20 * 16)

        label_recent_research = WidgetFactory.create_label(
            self, "Recent Search", ('Times New Roman', 15), "sunken")
        label_recent_research.place(x=60, y=70)

        self.listbox_recent_search = WidgetFactory.create_listbox(
            self, 30, 20)
        self.listbox_recent_search.place(x=30, y=150)
        listbox_scrollbar = WidgetFactory.create_scrollbar(
            self, self.listbox_recent_search)
        listbox_scrollbar.place(x=5 + 26 * 8 + 2, y=150, height=20 * 16)

        # button_mainmenu = WidgetFactory.create_button(
        #     self, "Main menu", 20, 3, '#e1dbd6')
        # button_mainmenu.place(x=830, y=300)
        
        

        label_disclaimer = WidgetFactory.create_label(
            self, "Disclaimer : This uses web scrapping to fetch song lyrics. All lyrics are property and copyright of their respective owners.\n This app is for personal use and for Educational purposes only. For more information, visit Genius.com.", ('Times New Roman', 10), "sunken")
        label_disclaimer.place(x=180, y=520)

    @staticmethod
    def get_lyrics(artist, song):
        try:
            song_info = genius.search_song(song, artist)
            if song_info:
                return song_info.lyrics
            else:
                return "Lyrics not found"
        except Exception as e:
            return f"Error fetching lyrics: {e}"

    def fetch_lyrics(self):
        artist = self.artist_entry.get()
        song = self.song_entry.get()
        lyrics = self.get_lyrics(artist, song)
        self.result_text.delete(1.0, 'end')
        self.result_text.insert('end', lyrics)
        search = f"{artist} - {song}"
        self.recent_searches.append(search)
        self.update_recent_searches_listbox()

    def update_recent_searches_listbox(self):
        self.listbox_recent_search.delete(0, 'end')
        for search in self.recent_searches:
            self.listbox_recent_search.insert('end', search)


if __name__ == "__main__":

    playlist_ui = Lyrics_section()
    playlist_ui.front()
    playlist_ui.display()
