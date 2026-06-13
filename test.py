import os
import shutil
path=r'C:\Users\S\OneDrive\ドキュメント\24BIT089\Test'
files=os.listdir(path)
for file in files:
    source=os.path.join(path,file)
    if file.endswith(".py"):
        destination_folder=os.path.join(path,"python")
        os.makedirs(destination_folder,exist_ok=True)
        shutil.move(source,destination_folder)