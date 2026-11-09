# tkinter is used to create the GUI (window, buttons, etc.)
import tkinter as tk
# this allows a text box with a scroll bar
import tkinter.scrolledtext as tkst #creats a text box with a scroll bar to display text

# stores all track data and allows getting name, artist, rating etc.
import track_library as lib
# controls how text looks (font, style and size)
import font_manager as fonts

# function that changes what is shown inside a text box
def set_text(text_area, content):
    # removes all text from the box
    text_area.delete("1.0", tk.END)

    # inserts new text into the box
    text_area.insert(1.0, content)

# creates the main program window and builds the GUI
class TrackViewer():

    # sets up the window and GUI layout when the program starts
    def __init__(self, window):
        # sets the size of the window
        window.geometry("750x350")

        # sets the title of the window
        window.title("View Tracks")

        # creates a button that shows all tracks when clicked
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)

        # places the button in the window
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # creates a label telling the user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        # places the label in the window
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # input box where the user types a track number
        self.input_txt = tk.Entry(window, width=3)
        # places the input box in the window
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # button that shows the details of a specific track when clicked
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        # places the button in the window
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # places the text area in the window
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # text area to display details of one track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        # places the text area in the window
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)
        # label used to show messages (e.g. button clicked)
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # automatically shows all tracks when the window opens
        self.list_tracks_clicked()
        # runs when "View track" button is clicked
    def view_tracks_clicked(self):
        # get the track number entered by the user
        key = self.input_txt.get()
        # check if the track exists in the library
        name = lib.get_name(key)
        if name is not None:
            # if track exists, get its details
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            # create a message showing track details
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            # display the track details in the text area
            set_text(self.track_txt, track_details)
        else:
            # show error message if track is not found
            set_text(self.track_txt, f"Track {key} not found")
            # update status message
        self.status_lbl.configure(text="View Track button was clicked!")

        # runs when "List All Tracks" button is clicked
    def list_tracks_clicked(self):
        # get all tracks from the library
        track_list = lib.list_all()
        # display all tracks in the text area
        set_text(self.list_txt, track_list)
        # update status message
        self.status_lbl.configure(text="List Tracks button was clicked!")

        # this part runs the program
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create the main window
    fonts.configure()       # apply font settings
    TrackViewer(window)     # open the TrackViewer window
    window.mainloop()       # keep the window running
