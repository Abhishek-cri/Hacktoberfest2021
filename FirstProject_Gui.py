import os,shutil

# NOTE : YOU CAN WRITE EVERY SINGLE EXTENSION INSIDE TUPLES
dict_extensions={
'audio_extensions':('.mp3','.mp4','.wav','.flac','.vlc'),
'videos_extension':('.mp4','.mkv','.MKV','.flv','.mpeg'),
'documents_extension':('.doc','.pdf','.txt')
}
#audio_extensions=('.mp3','.mp4','.wav','.flac','.vlc')
folderpath=input("Enter folder path :")

def file_finder(folder_path,file_extensions):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    
    return files

#print(file_finder(folder_path, audio_extensions))  this will print audio files

for extension_type,extension_tuple in dict_extensions.items():  # finding all files from dictionary by accessing 
    #print("calling file finder")
    #file_finder(folder_path, extension_tuple)
    folder_name=extension_type.split('_')[0]+'Files'  # creating folder name
    folder_path=os.path.join(folderpath,folder_name)  # creating folder path and joining with folder name
    try:
       os.mkdir(folder_path)  # making new folder
    except FileExistsError():
        print('file already exists') 
    for item in (file_finder(folderpath,extension_tuple)): # to move items in separate files
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)



