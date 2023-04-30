import tkinter as tk
import pygame
import os


class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        master.configure(bg='lavender')

        
        label_font = ("TkDefaultFont", 13)
        
        # Create label with file name
        self.file_label = tk.Label(master, text="", font=label_font, bg='lightgray')
        self.file_label.pack(pady=5)
        
        # Create a frame to hold the buttons
        button_frame = tk.Frame(master, bg='lavender')
        button_frame.pack(pady=5)

        self.play_button = tk.Button(button_frame, text="Play", command=self.play_music, bg="skyblue", font=label_font)
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_music, bg="skyblue", font=label_font)
        self.mute_button = tk.Button(button_frame, text="Mute", command=self.mute_music, bg="skyblue", font=label_font)
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_music, bg="skyblue", font=label_font)

        self.play_button.pack(side="left", padx=10, pady=10)
        self.pause_button.pack(side="left", padx=10, pady=10)
        self.mute_button.pack(side="left", padx=10, pady=10)
        self.stop_button.pack(side="left", padx=10, pady=10)

        # Create volume control
        volume_label = tk.Label(master, text="Volume Level:", font=label_font, bg='lightgray')
        volume_label.pack(pady=5)

        self.volume_scale = tk.Scale(master, from_=0, to=100, orient='horizontal', command=self.set_volume, bg='beige')
        self.volume_scale.set(50) # Set initial volume to 50%
        self.volume_scale.pack()

        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Define the music file path
        self.music_file = "C:\\Users\\LAVANYA\\Downloads\\audio.mp3"
        
        # Update file label with name of music file
        self.update_file_label()
        
    def update_file_label(self):
        file_name = os.path.basename(self.music_file)
        self.file_label.config(text=file_name)
        
    def play_music(self):
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play()
        
    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.pause_button.config(text="Unpause")
        else:
            pygame.mixer.music.unpause()
            self.pause_button.config(text="Pause")
    
    def mute_music(self):
        if pygame.mixer.music.get_volume() == 0.0:
            pygame.mixer.music.set_volume(1.0)
            self.mute_button.config(text="Mute")
        else:
            pygame.mixer.music.set_volume(0.0)
            self.mute_button.config(text="Unmute")
            
    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(int(volume)/100)


player = tk.Tk()
player.geometry("300x200")
music_player = MusicPlayer(player)


player.mainloop()
