import os

# load environment variable
from dotenv import load_dotenv
import json
load_dotenv()

# cast folder to type list
folders: list = json.loads(os.environ.get("FOLDERS", "default"))
dir_name = os.environ.get("DIR_NAME", "img")

# some code to debug whether folder worked
print(folders)
print("type of folder: ", type(folders))
for i in folders:
    print(i)

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
