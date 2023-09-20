import os
import shutil

from_dir = "C:/Users/Fabiana/Downloads"
to_dir = "C:/Users/Fabiana/Downloads/Imagens"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extention = os.path.splitext(file_name)
    #print(name)
    #print(extention)

    if extention == '':
        continue
    if extention in ['.gif', '.png', '.jpg', '.jpeg', '.JPG', '.jfif']:
        path1 = from_dir + '/' +  file_name
        path2 = to_dir + '/' + "Fotos do Mets"
        path3 = to_dir +'/' + "Fotos do Mets" '/' + file_name
        #print(path1)
        #print(path3)

        if os.path.exists(path2):
            print("Movendo " + file_name + ". . . . .")

            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Movendo " + file_name + ". . . . .")
            shutil.move(path1, path3)