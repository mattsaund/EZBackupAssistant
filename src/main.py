import tkinter as tk
from file_browser import file_browser

def main():

    #creating window
    main_window = tk.Tk()
    main_window.title("EZBackupAssistant")
    main_window.geometry("1000x800")

    #opens the file browser for source
    def file_browser_src_exec():
        filepath_source = file_browser()

        if not filepath_source: #user cancelled, leave the box unchanged
            return

        #redraws filepath_box
        filepath_source_box.delete(0, tk.END)
        filepath_source_box.insert(0, filepath_source)

    #opens the file browser for dest
    def file_browser_dest_exec():
        filepath_dest = file_browser()

        if not filepath_dest: #user cancelled, leave the box unchanged
            return

        #redraws filepath_box
        filepath_dest_box.delete(0, tk.END)
        filepath_dest_box.insert(0, filepath_dest)

    #UI for source files
    source_button_browse = tk.Button(main_window, text = "Browse Files", command=file_browser_src_exec)
    source_button_browse.pack(pady=20) #browse button to open file_browser

    filepath_source_box = tk.Entry(main_window, width = 50)
    filepath_source_box.pack(pady=20)

    #UI for destination files
    dest_button_browse = tk.Button(main_window, text = "Browse Files", command=file_browser_dest_exec)
    dest_button_browse.pack(pady=20) #browse button to open file_browser

    filepath_dest_box = tk.Entry(main_window, width = 50)
    filepath_dest_box.pack(pady=20)

    #main window loop
    main_window.mainloop()

if __name__ == "__main__":
    main()