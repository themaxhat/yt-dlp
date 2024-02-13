import os
from tkinter import filedialog
import tkinter as tk
import os
from tkinter import *

'''
https://www.youtube.com/watch?v=a05zgz7uehs
'''
audioFileTypes = ["mp3", "wav", "best", "aac", "flac", "ma", "opus", "vorbis"]
unsupported_chars = [
        '#', '%', '&', '{', '}', 
        '\\', '<', '>', '*', '?', 
        '/', '$', '!', "'", 
        '"', ':', '@', '+', '`', 
        '|', '='
    ]
directory = os.path.dirname(os.path.abspath(__file__))

filesToIgnore = []
for filename in os.listdir(directory):
    filesToIgnore += [filename]

def main():

    if input("input [1] or list [2] ") == '1':
        getDetails(useInput())
    else:
        with open ('songlist.txt') as f:
        
            for line in f:
                if (line[0] == '#' or line == '\n'):
                    continue

                details = lineToArray(line)

                
                for char in unsupported_chars:
                    if char in details[1]:
                        details[1] = details[1].replace(char, '_')

                print(details)

                getDetails(details)

def renameFile (newName) :

    for filename in os.listdir(directory):
        f = os.path.join (directory, filename)

        # checking if it is a file
        if os.path.isfile(f) and filename not in filesToIgnore:

            print ('\nRenaming \"' + filename + '\" to \"' + newName + '\"')
            print ('\n' + '------------------------' + '\n')
            os.rename(filename, newName)

            print("Please select a folder to put the new file in")
            
            new_location = filedialog.askdirectory(initialdir="/mnt/c/Users/isaac/Music/")

            print(f'Moving "{newName}" from "{directory}" to "{new_location}"')
            os.system(f'cp "{newName}" "{new_location}"')
            os.system(f'mv "{newName}" "DOWNLOADS/"')
            
            break

def lineToArray (line):
    toReturn = ['','','']
    
    l = 0
    
    url = ''
    while line[l] != '|':
        url += line[l]
        l += 1
    else:
        l += 1

    name = ''
    while line[l] != '|':
        name += line[l]
        l += 1
    else:
        l += 1

    type = ''
    while line[l] != '|':
        type += line[l]
        l += 1
    else:
        l += 1

    toReturn[0] = url
    toReturn[1] = name
    toReturn[2] = type
    
    return toReturn

def numAlreadyDownloaded(fn):
    numDownloaded = 0

    if fn in os.listdir("DOWNLOADS/"):
        numDownloaded = 1
    
        while numDownloaded > -1:
            # 'mysong (numDownloaded).mp3'
            if (fn[:-4] + f' ({numDownloaded})' + fn[-4:]) in os.listdir("DOWNLOADS/"):
                numDownloaded += 1
            else:
                break

    return numDownloaded

def getDetails(details):
    if details[2] in audioFileTypes:
        new_filename = details[1] + '.' + details[2]
        os.system(f"yt-dlp -x --audio-format {details[2]} {details[0]}")

        # add a (i) to end of filename
        if numAlreadyDownloaded(details[1] + '.' + details[2]) != 0:
            replace_option = input('File already exists\n  [1] Keep Both\n  [2] Delete Original\n  [3] Cancel Download\nPlease Select an Option: ')

            while replace_option not in ['1','2','3']:
                replace_option = input("Please Select Valid Integer. ")

            if replace_option == '1':
                new_filename = f"{details[1]} ({ numAlreadyDownloaded(details[1] + '.' + details[2]) }).{details[2]}"
                renameFile(new_filename)

            elif replace_option == '2':
                renameFile(new_filename)

            else:
                os.system(f"rm '{details[1] + '.' + details[2]}'")
        else:
            renameFile(new_filename)

    else:
        print (details[1] + ' file type not supported')
        
def useInput():
    to_return = ['null', 'null', 'null']

    root = Tk()
    root.geometry("300x150")

    #------
    top = Frame(root)

    title = Label(top, text="IMax Downloader").pack()

    top.pack(side=TOP)
    #------
    link_frame = Frame(root)

    link_label = Label(link_frame, text="Song Link")
    link_label.pack(side=LEFT)

    link_input = Entry(link_frame)
    link_input.pack(side=RIGHT)

    link_frame.pack()
    #------
    name_frame = Frame(root)

    name_label = Label(name_frame, text="Song Name")
    name_label.pack(side=LEFT)

    name_input = Entry(name_frame)
    name_input.pack(side=RIGHT)

    name_frame.pack()
    #------
    type_frame = Frame(root)

    type_label = Label(type_frame, text="File Type")
    type_label.pack(side=LEFT)

    options = audioFileTypes + ['select']
    clicked = StringVar() 
    clicked.set( 'select' ) 
    type_drop = OptionMenu(type_frame, clicked, *options)
    type_drop.pack(side=RIGHT)

    type_frame.pack()

    #------
    bottom = Frame(root).pack(side=BOTTOM)

    def save():
        print(link_input.get())
        to_return[0] = link_input.get()
        to_return[1] = name_input.get()
        to_return[2] = clicked.get()

        root.quit()

    def cancel():
        root.quit()

    cancel = Button(bottom, text="cancel", command=cancel).pack(side=RIGHT)
    enter = Button(bottom, text="enter", command=save).pack(side=RIGHT)
    #------

    root.mainloop()

    return to_return

main()