from YtGUI.mock.youtube import YouTube


def make_download_command(controls):
    def downloadVid():
        def on_progress(stream, chunk, bytes_remaining):
            sz = stream.filesize
            downloaded = sz - bytes_remaining
            downloaded_percent = 100 * float(downloaded) / sz
            downloaded_percent = int(downloaded_percent)
            
            controls["progress_label"].configure(text=f"{downloaded_percent}%")
            controls["progress_label"].update()
            controls["progress_bar"].set(float(downloaded_percent) / 100)
            
        
        finish_label_config = {}
        try:
            entered_link = controls["link_input"].get()
            yt_vid = YouTube(entered_link, on_progress_callback=on_progress)
            
            controls["vid_label"].configure(text=yt_vid.title)
            
            user_res = controls["vid_res_dropdown"].get()
            res = user_res
            vid = yt_vid.streams.get_by_resolution(res)
            
            resolutions = ["144p", "240p", "360p", "480p", "720p"]
            i = -1
            while vid is None and i < len(resolutions):
                i += 1
                res = resolutions[i]
                vid = yt_vid.streams.get_by_resolution(res)
            
            controls['finish_label'].configure(text=f"Could not find {user_res}, using {res} instead...", text_color="orange")
            vid.download()
            
            finish_label_config["text"] = f"Downloaded {entered_link} successfully!"
            finish_label_config["text_color"] = "green"
        except Exception as e:
            finish_label_config["text"] = f"An error occured: {e}"
            finish_label_config["text_color"] = "red"
        
        controls["finish_label"].configure(**finish_label_config)

    return downloadVid

def make_resize_command(app, controls):
    return lambda: app.geometry(f"{controls["res_input_width"].get()}x{controls["res_input_height"].get()}")
