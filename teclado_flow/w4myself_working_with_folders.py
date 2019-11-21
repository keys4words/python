import os

def read_folder(folder):
    for root, dirs, files in os.walk('folder'):
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level+1)
        for file in files:
            print(f'{sub_indent}{file}')


read_folder('folder')