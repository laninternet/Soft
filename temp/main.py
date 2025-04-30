# © Okmeque1 Software - See https://github.com/GamerSoft24/Software/tree/Main/LICENSE for more information.
import videoplayer
from tkinter import filedialog, messagebox
filename = filedialog.askopenfilename(filetypes=[("Any File","*.*")]) 
try:
    if filename == "":
        raise FileNotFoundError
    with open(filename,"r") as valid_file:
        vid = videoplayer.VideoPlayer()
        vid.videoplayer(filename)
except FileNotFoundError:
    messagebox.showerror("Okmeque1 Video Player","The file that you selected does not exist.\nError: 6510B")
    exit()
except Exception as e:
    messagebox.showerror("Okmeque1 Video Player",f"This program has encountered an error and needs to close.\nFor more information, review the Error Chart as well as the Python Manual.\nError: {e}")