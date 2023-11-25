import os


directory = './folder'
for root, dirs, files in os.walk(directory):
    for file in files:
        # Печать пути к файлу
        print(os.path.join(root, file))