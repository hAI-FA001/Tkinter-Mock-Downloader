import customtkinter
from pytube import YouTube


customtkinter.set_appearance_mode('System')  # dark mode/light mode
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

app.mainloop()