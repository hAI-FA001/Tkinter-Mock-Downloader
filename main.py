import customtkinter
from pytube import YouTube


customtkinter.set_appearance_mode('System')  # dark mode/light mode
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")


vid_label = customtkinter.CTkLabel(app, text="YouTube Link")
vid_label.pack(padx=10, pady=10)

download_btn = customtkinter.CTkButton(app, text="Download")
download_btn.pack(padx=10, pady=10)


app.mainloop()