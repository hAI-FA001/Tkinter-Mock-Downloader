import random
import time


class Chunk:
    def __init__(self, num_bytes):
        self.num_bytes = num_bytes

class DownloadableData:
    def __init__(self, on_progress_callback):
        self.on_progress_callback = on_progress_callback
    
    def download(self):
        k = random.randint(4, 9)
        progresses_first_digit = random.sample(list(range(0, 10)), k=k)
        progresses_second_digit = random.sample(list(range(0, 10)), k=k)
        progresses_first_digit = sorted(progresses_first_digit)
        
        for i in range(k):
            first_digit = progresses_first_digit[i]
            second_digit = progresses_second_digit[i]
            progress = first_digit * 10 + second_digit
            progress_next = progresses_first_digit[i+1]*10 + progresses_second_digit[i+1] if i != k-1 else 100
            
            self.on_progress_callback(Chunk(progress_next - progress), progress)
            time.sleep(random.randint(1, 3))
        
        self.on_progress_callback(Chunk(100 - progress), 100)

class Stream:
    def __init__(self, on_progress_callback):
        self.on_progress_callback = on_progress_callback
        self.filesize = random.randint(50, 200)
    
    def get_by_resolution(self, resolution):
        return DownloadableData(self.stream_progress_callback) if resolution in random.sample(["144p", "240p", "360p", "480p", "720p"], k=2) else None
    
    def stream_progress_callback(self, chunk, progress):
        self.on_progress_callback(self, chunk, (100 - progress) * self.filesize / 100)

class YouTube:
    def __init__(self, link, on_progress_callback):
        self.link = link
        self.streams = Stream(on_progress_callback)
        self.title = f"Yt-Vid {random.randint(1, 100)}"

