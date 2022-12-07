"""This project is design to download any video from youtube to your device

"""

#Inporting the necessary modules for the project
from tkinter import *
from tkinter import filedialog
import shutil
#from pytube import YouTube

#Function for selecting path
def select_path():
    path = filedialog.askdirectory()
    path_label.config(Text=path)

#Function to download the video
def download():
    """Download Function"""
    global Canvas
    link = link_field.get()
    yt = YouTube(link)
    # getting the highest resolution possible
    ys = yt.stream.get_highest_resolution()

#GUI Design Starts 

#Canvas Design
screen = Tk() 
title = screen.title("YouTube Downloader")
canvas = Canvas(screen, width=500, height=1000)
canvas.pack()

#PROJECT NAME
project_name = label(screen, text="YOUTUBE DOWNLOADER", font=('arial',9))
canvas.create_window(250, 100, window=project_name)

#PROJECT IMAGE
image = PhotoImage(file='images/youtube.png')
image = image.subsample(2, 2)
canvas.create_image(250, 250, image=image)

#FIELDS
link_field = Entry(screen, width=30)
link_label = Label(screen, text="Enter the download link here.", font=('calibri', 9))
canvas.create_window(250, 400, window=link_label)
canvas.create_window(250, 450, window=link_field)

#VIDEO SAVING PATH
path_label = Label(screen, text='Select Path')
path_button = Button(screen, text="Select", command=select_path, fg = "white", font = "calibri 9", bd = 2, bg = "grey", relief = "groove")
canvas.create_window(450, 600, window=d_button)



screen.mainloop()

