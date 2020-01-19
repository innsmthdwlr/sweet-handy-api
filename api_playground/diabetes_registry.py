import json
import dropbox
import os.path

class DiabetesRegistry:
    def __init__(self, current_dir):
        self.cwd = current_dir
        self.TOKEN = None
        json_file_path = os.path.join(self.cwd, '.credentials', 'dropbox.json')
        with open(json_file_path) as f:
            data = json.load(f)
            token = data["token"]
            self.TOKEN = token
        self.dbx = dropbox.Dropbox(self.TOKEN)

    def upload(self, file_path, file_name, overwrite=True):
        mode = (dropbox.files.WriteMode.overwrite
                if overwrite
                else dropbox.files.WriteMode.add)
        with open(file_path, 'rb') as f:
            try:
                res = self.dbx.files_upload(
                    f.read(), f"/{file_name}", mode, mute=True)
            except dropbox.exceptions.ApiError as err:
                print('*** API error', err)
                return None
        return res

    def download(self, file_name):
        try:
            md, res = self.dbx.files_download(f"/{file_name}")
        except dropbox.exceptions.HttpError as err:
            print('*** HTTP error', err)
            return None
        data = res.content
        file_path = os.path.join(self.cwd, 'temp', 'registry.json')
        with open(file_path, 'wb') as f:
            f.write(data)
        return file_path
