import tkinter
import customtkinter
from pytube import YouTube


def downloadVid():
    def on_progress(stream, chunk, bytes_remaining):
        sz = stream.filesize
        downloaded = sz - bytes_remaining
        downloaded_percent = 100 * float(downloaded) / sz
        downloaded_percent = int(downloaded_percent)
        
        progress_label.configure(text=f"{downloaded_percent}%")
        progress_label.update()
        progress_bar.set(float(downloaded_percent) / 100)
        
    
    finish_label_config = {}
    try:
        entered_link = link_input.get()
        yt_vid = YouTube(entered_link, on_progress_callback=on_progress)
        
        vid_label.configure(text=yt_vid.title)
        
        vid = yt_vid.streams.get_highest_resolution()
        vid.download()
        
        finish_label_config["text"] = f"Downloaded {entered_link} successfully!"
        finish_label_config["text_color"] = "green"
    except Exception as e:
        finish_label_config["text"] = f"An error occured: {e}"
        finish_label_config["text_color"] = "red"
    
    finished_label.configure(**finish_label_config)


customtkinter.set_appearance_mode('System')  # dark mode/light mode
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")



vid_label = customtkinter.CTkLabel(app, text="YouTube Link")
vid_label.pack(padx=10, pady=10)

link_var = tkinter.StringVar()
link_input = customtkinter.CTkEntry(app, width=350, height=40, textvariable=link_var)
link_input.pack()

finished_label = customtkinter.CTkLabel(app, text="")
finished_label.pack()

progress_label = customtkinter.CTkLabel(app, text="0%")
progress_label.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

download_btn = customtkinter.CTkButton(app, text="Download", command=downloadVid)
download_btn.pack(padx=10, pady=10)


app.mainloop()