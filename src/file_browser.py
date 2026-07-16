import tkinter as tk
from tkinter import filedialog

def file_browser():

    #opens a file dialog pop up window
    filepath = filedialog.askdirectory(
        initialdir = "/", #initial directory the file browser window opens to
        title = "Select a Folder", #title of popup window
    )

    return filepath #returns selected folder
