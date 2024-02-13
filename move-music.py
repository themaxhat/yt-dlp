import os

for filename in os.listdir("../yt-dlp"):
    filename_len = len(str(filename))
    file_ext = filename[filename_len-3] + filename[filename_len-2] + filename[filename_len-1]

    # if a file is an mp3, copy it to 'Music' folder and 'DOWNLOADS' directory 
    if (file_ext == "mp3"):
        # print(filename)
        os.system('cp \"' + filename + '\" /mnt/c/Users/isaac/Music/')
        os.system('mv \"' + filename + '\" DOWNLOADS/')
