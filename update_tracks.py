import tkinter as tk
import track_library as lib
import font_manager as fonts


# creates the update tracks window
class UpdateTracks:

    # sets up the window and GUI
    def __init__(self, window):
        window.geometry("400x250")
        window.title("Update Tracks")

        # label for track number
        tk.Label(window, text="Enter Track Number").grid(row=0, column=0, padx=10, pady=10)

        # input box for track number
        self.track_input = tk.Entry(window)
        self.track_input.grid(row=0, column=1, padx=10, pady=10)

        # label for new rating
        tk.Label(window, text="Enter Rating").grid(row=1, column=0, padx=10, pady=10)

        # input box for new rating
        self.rating_input = tk.Entry(window)
        self.rating_input.grid(row=1, column=1, padx=10, pady=10)

        # button to update rating
        tk.Button(window, text="Update Rating", command=self.update_rating_clicked).grid(
            row=2, column=0, columnspan=2, padx=10, pady=10
        )

        # output label to show result
        self.output_lbl = tk.Label(window, text="", justify="left")
        self.output_lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # runs when the Update Rating button is clicked
    def update_rating_clicked(self):
        # get the values entered by the user
        track_number = self.track_input.get()
        new_rating = self.rating_input.get()

        # check if inputs are numbers
        if not track_number.isdigit() or not new_rating.isdigit():
         self.output_lbl.configure(text="Invalid Input")
         return



        # check if the track exists
        name = lib.get_name(track_number)

        if name is not None:
            # update the rating in the library
            lib.set_rating(track_number, new_rating)

            # get play count for this track
            play_count = lib.get_play_count(track_number)

            # show updated track details
            message = f"{name}\nRating: {new_rating}\nPlays: {play_count}"
            self.output_lbl.configure(text=message)
        else:
            # show error if track is not found
            self.output_lbl.configure(text="Track not found")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracks(window)
    window.mainloop()