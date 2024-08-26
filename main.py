import customtkinter
from YtGUI.controls import add_controls


if __name__ == "__main__":
    customtkinter.set_appearance_mode('System')  # dark mode/light mode
    customtkinter.set_default_color_theme('blue')

    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("YouTube Video Downloader")
    
    controls = add_controls(app)
    
    app.mainloop()
