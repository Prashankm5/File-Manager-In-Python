import os ,shutil


# NOTE: you cane write every single extention in tuple
dict_extention = {
'audio_extention' : ('.mp3','.m4a','.wav','.flac'),
'videos_extention' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
'Document_extention' : ('.doc','.pdf','.txt'),
'python' : ('.py')
}
    

# hint = ('audio_extention','videos_extention','Document_extention','python')

# file_extention = input(f'enter your extention form {hint} \n NOTE :  you can enter your own extention in tuple : ')
folderPath = input('enter the path of folder : ')

def file_finder (folder_path,file_extention):

    return (file for file in os.listdir(folderPath) for extention in file_extention if file.endswith(extention))

for extention_type,extention_tuple in dict_extention.items():
    folder_name = extention_type.split('_')[0] + 'File'
    folder_Path = os.path.join(folderPath,folder_name)
    os.mkdir(folderPath)
    for item in file_finder(folderPath,extention_tuple):
        item_path = os.path.join(folderPath,item)
        new_item_path = os.path.join(folder_Path,item)
        shutil.move(item_path,new_item_path)