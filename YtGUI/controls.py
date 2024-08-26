import tkinter
import customtkinter

from YtGUI.features import make_download_command


def make_vid_label(app):
    vid_label = customtkinter.CTkLabel(app, text="YouTube Link")
    vid_label.pack(padx=10, pady=10)
    return vid_label

def make_link_input(app):
    link_var = tkinter.StringVar()
    link_input = customtkinter.CTkEntry(app, width=350, height=40, textvariable=link_var)
    link_input.pack()
    return link_input

def make_finish_label(app):
    finish_label = customtkinter.CTkLabel(app, text="")
    finish_label.pack()
    return finish_label

def make_progress(app):
    progress_label = customtkinter.CTkLabel(app, text="0%")
    progress_label.pack()

    progress_bar = customtkinter.CTkProgressBar(app, width=400)
    progress_bar.set(0)
    progress_bar.pack(padx=10, pady=10)
    
    return progress_label, progress_bar

def make_download_btn(app, download_command):
    download_btn = customtkinter.CTkButton(app, text="Download", command=download_command)
    download_btn.pack(padx=10, pady=10)
    return download_btn

def add_controls(app):
    controls = {}
    controls["vid_label"] = make_vid_label(app)
    controls["link_input"] = make_link_input(app)
    controls["finish_label"] = make_finish_label(app)
    controls["progress_label"], controls["progress_bar"] = make_progress(app)
    
    controls["download_btn"] = make_download_btn(app, make_download_command(controls))

    return controls
