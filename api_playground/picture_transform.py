from PIL import Image
import math

class PictureTransformator:
    def __init__(self, new_width=540, new_height=295):
        self.new_width = new_width
        self.new_height = new_height

    def resize(self, file_path):
        im = Image.open(file_path)
        old_width, old_height = im.size[0], im.size[1]
        ratio = self.new_width / old_width
        im.thumbnail((math.floor(old_width * ratio), math.floor(old_height * ratio)))
        im.save(file_path, optimize=True, quality=50)
        return self.get_datetime(file_path)

    def get_datetime(self, file_path):
        file_name = file_path.split('/')[-1]
        _, date, time = file_name.rstrip('.jpg').split('_')
        date = '-'.join(a+b for a, b in zip(date[::2], date[1::2])).replace('-', '', 1)
        time = ':'.join(a+b for a, b in zip(time[::2], time[1::2]))
        return (file_name, date, time)
