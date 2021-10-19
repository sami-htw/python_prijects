from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font

from pytube import YouTube


# The Functions
folder_Name = ""


def openLocation():
    global folder_Name
    folder_Name = filedialog.askdirectory()
    if(len(folder_Name) > 1):
        download_Label.config(text=folder_Name, fg="green")
        downloadVideo()
    else:
        download_Label.config(text="Select Folder to save, please", fg="red")


def downloadVideo():
    try:
        choose = youtubeSelection.get()
        url = urlEntry.get()

        if(len(url) > 1):
            urlError.config(text="")
            yt = YouTube(url)

            if(choose == selection[0]):
                take = yt.streams.filter(
                    progressive=True, file_extension="mp4").get_highest_resolution()
            elif(choose == selection[1]):
                take = yt.streams.filter(
                    progressive=True, file_extension="mp4").get_lowest_resolution()
            elif(choose == selection[2]):
                take = yt.streams.filter(only_audio=True).first()
        else:
            urlError.config(text="Enter Valid URL!", fg="red")
        take.download(folder_Name)
        download_Label.config(text='Download Completed!', fg='green')
    except Exception as err:
        print(err)


# UI
root = Tk()
root.title('Youtube Video Downloader')
root.columnconfigure(0, weight=1)  # set all content in center

# The title
title = Label(root, text='Youtube Video Downloader',
              fg='red', font=('jost', 20))
title.grid(row=0, padx=100, pady=20)

urlLabel = Label(root, text='Enter Video URL', font=('jost', 15))
urlLabel.grid(row=1)


# URL entry
urlEntry = Entry(root, width=40, fg='blue', font=('jost', 15))
urlEntry.grid(row=2, pady=5)

# Error_Label
urlError = Label(root, text="", fg="red", font=('jost', 13))

urlError.grid(row=3)

# Choice_Label
choice_Label = Label(root, text='Select type and Quality', font=('jost', 15))
choice_Label.grid(row=4)

# comboBox
selection = ["High Quality Video", "Low Quality Video", "Audio File"]
youtubeSelection = ttk.Combobox(root, values=selection, font=('jost', 15))
youtubeSelection.grid(row=5, pady=10)

# Download_Button
download_BTN = Button(root, command=openLocation, text='Download', width=20,
                      bg='red', fg='white', font=('jost', 15))
download_BTN.grid(row=6, pady=10)


# Error_Msg
download_Label = Label(root, text="", fg="red", font=('jost', 13))
download_Label.grid(row=7, pady=10)


root.mainloop()
