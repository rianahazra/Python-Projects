import os 
import shutil
source_directory="./"#current working directory
#folders=["Images", "Documents", "Videos"] .pdf, .jpeg are extensions
extensionmap={".jpg":"Images", ".pdf":"Documents",".mp4":"Videos"}
for folder in extensionmap.values():
    Folderpath=os.path.join(source_directory, folder)
    if not os.path.exists(Folderpath):
        os.makedirs(Folderpath)

for file in os.listdir(source_directory):
    #print(os.path.splitext(file))
    file_extension=os.path.splitext(file)[-1].lower()
    if file_extension in extensionmap:
        currentpath=os.path.join(source_directory,file)
        destinationpath=os.path.join(source_directory,extensionmap[file_extension],file)
        print(destinationpath)
        shutil.move(currentpath,destinationpath)
        print(f'moved {file} to {extensionmap[file_extension]} folder')
print(fileorganization complete)
