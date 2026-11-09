# Python Jukebox GUI App

A desktop Jukebox application developed in Python using Tkinter for the COMP1752 Object-Oriented Programming module at the University of Greenwich.

---

### Features & Functionality
- **View Tracks (`view_tracks.py`):** Display the track library, view artist names, track ratings (star ratings), and play counts.
- **Create Playlist (`create_track_list.py`):** Add tracks by ID to a custom user playlist, simulate playing the list (which increments play counts), or reset the selection.
- **Update Ratings (`update_tracks.py`):** Modify song ratings dynamically with built-in input validation.
- **Robust Error Handling:** Checks for non-existent track IDs and invalid string inputs to prevent GUI crashes.

---

### Tech Stack & Architecture
- **Language:** Python 3
- **GUI Framework:** Tkinter (`tkst`, `tkfont`)
- **Design Pattern:** Object-Oriented Programming (OOP)
- **IDE:** PyCharm

---

### Code Files Included
- `track_player.py` - Main launch menu / entry point
- `view_tracks.py` - Track list viewer interface
- `create_track_list.py` - Custom playlist creation manager
- `update_tracks.py` - Rating modification interface
- `track_library.py` & `library_item.py` - Data structures & backend logic
- `font_manager.py` - Global UI font styling
- `COMP1752 - REPORT.pdf` - Project design specification & test plan report
