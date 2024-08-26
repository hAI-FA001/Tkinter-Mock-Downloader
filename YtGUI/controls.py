import tkinter
import customtkinter

from YtGUI.features import make_download_command, make_resize_command


def make_vid_label(app):
    vid_label = customtkinter.CTkLabel(app, text="YouTube Link")
    
    # vid_label.pack(padx=10, pady=10)
    vid_label.grid(row=0, sticky="nsew", columnspan=3)
    
    return vid_label

def make_link_input(app):
    link_var = tkinter.StringVar()
    link_input = customtkinter.CTkEntry(app, width=350, height=40, textvariable=link_var)
    
    # link_input.pack()
    link_input.grid(row=1, sticky="ew", columnspan=3, padx=app.winfo_width()//4)
    
    return link_input

def make_finish_label(app):
    finish_label = customtkinter.CTkLabel(app, text="Download status will appear here")
    
    # finish_label.pack()
    finish_label.grid(row=3, columnspan=3, sticky="ew")
    
    return finish_label

def make_progress(app):
    progress_bar = customtkinter.CTkProgressBar(app, width=400)
    progress_bar.set(0)
    
    # progress_bar.pack(padx=10, pady=10)
    progress_bar.grid(row=4, column=0, sticky="ew", columnspan=2, padx=(app.winfo_width()//4, 0))

    progress_label = customtkinter.CTkLabel(app, text="0%")
    # progress_label.pack()
    progress_label.grid(row=4, column=3, padx=(0, app.winfo_width()//4))
    
    return progress_label, progress_bar

def make_download_btn(app, download_command):
    download_btn = customtkinter.CTkButton(app, text="Download", command=download_command)
    
    # download_btn.pack(padx=10, pady=10)
    download_btn.grid(row=5, sticky="nsew", columnspan=3, padx=app.winfo_width()//4)
    
    return download_btn

def make_resizer(app):
    res_width_var = tkinter.StringVar()
    res_height_var = tkinter.StringVar()
    res_input_width = customtkinter.CTkEntry(app, width=350, height=40, textvariable=res_width_var)
    res_input_height = customtkinter.CTkEntry(app, width=350, height=40, textvariable=res_height_var)
    
    # res_input_width.pack()
    res_input_width.grid(row=7, column=0, sticky="nsew", padx=app.winfo_width()//20, pady=app.winfo_height()//20)
    # res_input_height.pack()
    res_input_height.grid(row=7, column=2, sticky="nsew", padx=app.winfo_width()//20, pady=app.winfo_height()//20)
    
    return res_input_width, res_input_height

def make_resize_btn(app, resize_command):
    res_btn = customtkinter.CTkButton(app, text="Resize Window", command=resize_command)
    
    # res_btn.pack()
    res_btn.grid(row=8, columnspan=3, sticky="nsew", padx=app.winfo_width()//20)
    
    return res_btn

def make_vid_res_dropdown(app):
    vid_res_var = tkinter.StringVar(value="720p")
    vid_res_dropdown = customtkinter.CTkOptionMenu(app, variable=vid_res_var, values=["720p", "480p", "360p", "240p", "144p"])
    
    # vid_res_dropdown.pack()
    vid_res_dropdown.grid(row=2, sticky="ew", columnspan=3, padx=app.winfo_width()//2)
    
    return vid_res_dropdown

def add_controls(app: customtkinter.CTk):
    app.grid_columnconfigure(tuple(x for x in range(3)), weight=1)
    app.rowconfigure(tuple(x for x in range(10)), weight=1)
    
    controls = {}
    controls["vid_label"] = make_vid_label(app)
    controls["link_input"] = make_link_input(app)
    controls["vid_res_dropdown"] = make_vid_res_dropdown(app)
    
    controls["finish_label"] = make_finish_label(app)
    controls["progress_label"], controls["progress_bar"] = make_progress(app)
    
    controls["download_btn"] = make_download_btn(app, make_download_command(controls))
    
    controls["res_input_width"], controls["res_input_height"] = make_resizer(app)
    controls["resize_btn"] = make_resize_btn(app, make_resize_command(app, controls))
    
    # for spacing
    customtkinter.CTkLabel(app, text="").grid(row=6, columnspan=3, sticky="nsew")
    customtkinter.CTkLabel(app, text="").grid(row=9, columnspan=3, sticky="nsew")

    return controls
