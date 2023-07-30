import pytube
from tkinter import *
from tkinter import messagebox
import os


# Create a tkinter window
window = Tk()
window.title("Youtube Downloader")
window.geometry("500x450")

# Load YouTube logo image
photo = PhotoImage(file="youtube.png")
photo_label = Label(image=photo)
photo_label.pack(pady=30)

# URL entry label and entry box
enter_url_label = Label(text="Enter URL", font=('Arial', 14, 'bold'))
enter_url_label.pack()
enter_url_entry = Entry(width=45, font=('Arial', 12, 'normal'))
enter_url_entry.focus()
enter_url_entry.pack(pady=10)


# Radio buttons for selecting Mp3 or Mp4
mp_radio_checked_state = IntVar()
mp3_radiobutton = Radiobutton(text="Mp3", value=1, variable=mp_radio_checked_state, font=('Arial', 11, 'bold'))
mp3_radiobutton.pack()

mp4_radiobutton2 = Radiobutton(text="Mp4", value=2, variable=mp_radio_checked_state, font=('Arial', 11, 'bold'))
mp4_radiobutton2.pack()

# Get the current working directory
path = os.getcwd()


# Function to download the file
def download_clicked():
    url = enter_url_entry.get()
    if url == "":
        messagebox.showinfo(title="Error!", message="Please enter URL.")
    elif mp_radio_checked_state.get() == 0:
        messagebox.showinfo(title="Error!", message="You have to select mp3 or mp4.")
    try:
        if mp_radio_checked_state.get() == 1:
            mp3_file_name = "mp3 files"
            mp3_file_path = os.path.join(path, mp3_file_name)
            pytube.YouTube(url).streams.get_audio_only().download(mp3_file_path)
            messagebox.showinfo("Successfully Downloaded!", message=f"{mp3_file_path}\n{pytube.YouTube(url).title}")

        elif mp_radio_checked_state.get() == 2:
            mp4_file_name = "mp4 files"
            mp4_file_path = os.path.join(path, mp4_file_name)
            pytube.YouTube(url).streams.get_highest_resolution().download(mp4_file_path)
            messagebox.showinfo("Successfully Downloaded!", message=f"{mp4_file_path}\n{pytube.YouTube(url).title}")
    except:
        messagebox.showinfo(title="Unexpected Error!", message="Make sure you enter a valid url.")


# Download button
download_button = Button(text="Download", font=('Arial', 12, 'bold'), command=download_clicked, bg="#FF0000", fg="white")
download_button.update()
download_button.pack(pady=20)

window.mainloop()