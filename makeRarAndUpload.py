import os
import shutil
import requests




folder = os.path.abspath(os.curdir)

folder_name = os.path.basename(os.path.normpath(folder))

shutil.make_archive(folder_name, "zip", folder)



# check zip file size
if os.path.getsize(f'{folder_name}.zip') <= 50 * 1024 * 1024:
    with open(f"{folder_name}.zip", "rb") as f:
        url = 'https://file.io'
        files = {'file': (f'{folder_name}.zip', f)}
        resp = requests.post(url, files=files)
        print(resp)
        link = resp.json()["link"]
        print("File uploaded successfully, download link :",link)
else:
    print("File size exceeded 50MB, cannot upload")



