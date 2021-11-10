import tkinter as tk
import webbrowser
import os


def quit():
    root.destroy()


def openendel():
    os.system("open /Applications/Endel.app")
    quit()


def openfocusatwill(chrome_path="open -a /Applications/Google\ Chrome.app %s"):
    webbrowser.get(chrome_path).open("https://www.focusatwill.com/")
    quit()


def openbrainfm(chrome_path="open -a /Applications/Google\ Chrome.app %s"):
    webbrowser.get(chrome_path).open("https://www.brain.fm/")
    quit()


# Create Object
root = tk.Tk()

# Set geometry
root.geometry("200x200")

# Add Label
tk.Label(root, text="Focus app picker", font="italic 15 bold").pack(pady=10)

chrome_path = "open -a /Applications/Google\ Chrome.app %s"

# Add Buttons
endel = tk.Button(root, text="Endel", command=openendel)
endel.pack(pady=10)
focusatwill = tk.Button(root, text="focus@will", command=openfocusatwill)
focusatwill.pack(pady=10)
brainfm = tk.Button(root, text="BrainFM", command=openbrainfm)
brainfm.pack(pady=10)

# Execute Tkinter
root.mainloop()
