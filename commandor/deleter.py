import os
def delete_file():
    print()
    print('Write file name')
    file_name = str(input())
    print('Write file extension (for example .txt or .docx)')
    extension_file = str(input())
    print('write path of file \n if you print nothing you will delete file in the commandor folder')
    path_file = str(input())
    if (path_file == False):
        path_file = './'

    os.remove(path_file + file_name + extension_file)

def delete_folder():
    print()
    print('Write folder name')
    folder_name = str(input())
    print('\n')
    print('Write folder path \n if you print nothing you will delete folder in commandor')
    folder_path = str(input())
    if folder_path == False:
        folder_path = './'

    os.rmdir(folder_path + folder_name)