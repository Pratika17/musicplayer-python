import tkinter as tk
from tkinter import filedialog, messagebox
from pygame import mixer

# Initialize the mixer module in pygame
mixer.init()


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x300")

        # Add a label to show the current status
        self.status = tk.StringVar()
        self.status.set("No song loaded")

        self.status_label = tk.Label(self.root, textvariable=self.status, relief="sunken", anchor="w")
        self.status_label.pack(fill="x", pady=5)

        # Add buttons to control the music player
        self.load_button = tk.Button(self.root, text="Load Songs", command=self.load_songs)
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=5)

        # Add a listbox to display the loaded songs
        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.song_listbox.pack(fill="both", expand=True, pady=10)

        self.songs = []

    def load_songs(self):
        self.songs = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        if self.songs:
            self.song_listbox.delete(0, tk.END)
            for song in self.songs:
                self.song_listbox.insert(tk.END, song.split("/")[-1])
            self.status.set("Songs loaded")

    def play_song(self):
        selected_song_index = self.song_listbox.curselection()
        if selected_song_index:
            selected_song = self.songs[selected_song_index[0]]
            mixer.music.load(selected_song)
            mixer.music.play()
            self.status.set(f"Playing: {selected_song.split('/')[-1]}")
        else:
            messagebox.showwarning("Select Song", "Please select a song to play")

    def pause_song(self):
        mixer.music.pause()
        self.status.set("Paused")

    def stop_song(self):
        mixer.music.stop()
        self.status.set("Stopped")


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()