import os

# load environment variable
from dotenv import load_dotenv
load_dotenv()

folders = os.environ.get("FOLDERS", "default")
dir_name = os.environ.get("DIR_NAME", "img")
print(folders)

# check if dir already exist at root level
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

# check under local /img folder if any has been created already
dir_path = os.path.join(dir_name)
print(dir_path)

for f in folders:
    full_path = os.path.join(dir_path, f)
    if os.path.exists(full_path):
        print(f"{full_path} already exists")
    else:
        os.makedirs(full_path)
        print(f"{full_path} has been created")