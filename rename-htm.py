import os

for filename in os.listdir('.'):
    if filename.endswith('.htm'):
        new_name = filename[:-4] + '.html'
        os.rename(filename, new_name)
        print(f'Renamed: {filename} → {new_name}')