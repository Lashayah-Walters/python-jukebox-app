import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts

# creates the window and GUI layout
class CreateTrackList:

    # sets up the window
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Create Track List")

        # list to store playlist track numbers
        self.playlist = []

        # label telling user to enter track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        # input box where user types track number
        self.input_txt = tk.Entry(window, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # button to add track to playlist
        add_btn = tk.Button(window, text="Add Track", command=self.add_track_clicked)
        add_btn.grid(row=0, column=2, padx=10, pady=10)

        # playlist text area to display the playlist
        self.playlist_txt = tkst.ScrolledText(window, width=50, height=10)
        self.playlist_txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # play playlist button
        play_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist_clicked)
        play_btn.grid(row=2, column=0, padx=10, pady=10)

        # button to reset playlist
        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist_clicked)
        reset_btn.grid(row=2, column=1, padx=10, pady=10)

        # status message label
        self.status_lbl = tk.Label(window, text="")
        self.status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    # runs when the Add Track button is clicked
    def add_track_clicked(self):
        # get the track number entered by the user
        track_number = self.input_txt.get()

        # get the track name from the library
        name = lib.get_name(track_number)

        # check if the track exists
        if name is not None:
            # store the track number in the playlist
            self.playlist.append(track_number)

            # create text to display all track names in the playlist
            playlist_names = []
            for number in self.playlist:
                playlist_names.append(lib.get_name(number))

            playlist_text = "\n".join(playlist_names)

            # clear the text area
            self.playlist_txt.delete("1.0", tk.END)

            # display the updated playlist
            self.playlist_txt.insert(1.0, playlist_text)

            # update status message
            self.status_lbl.configure(text="Track added to playlist")
        else:
            # show an error message if track is not found
            self.playlist_txt.delete("1.0", tk.END)
            self.playlist_txt.insert(1.0, "Track not found")
            self.status_lbl.configure(text="Invalid track number")

    # runs when the Play Playlist button is clicked
    def play_playlist_clicked(self):
        # check if the playlist is empty
        if len(self.playlist) == 0:
            self.status_lbl.configure(text="Playlist is empty")
        else:
            # increase play count for each track in the playlist
            for track_number in self.playlist:
                lib.increment_play_count(track_number)

            self.status_lbl.configure(text="Playlist played")

    # runs when the Reset Playlist button is clicked
    def reset_playlist_clicked(self):
        # empty the playlist
        self.playlist = []

        # clear the playlist text area
        self.playlist_txt.delete("1.0", tk.END)

        # update status message
        self.status_lbl.configure(text="Playlist reset")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTrackList(window)
    window.mainloop()