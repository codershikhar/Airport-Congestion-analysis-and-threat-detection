import os
import multiprocessing
import Tkinter
import threading
import cv2,os



#check for required folders
if not os.path.isdir("cascades"):
    print("cascades folder not found")
if not os.path.isdir("red_corner"):
    print("red corner folder not found")
#TODO make a checksum of all codes and check them from secured place

print("system init done...\nstarting system")

def startMainGUI():
    mainGUI = Tkinter.Tk()
    txt = Tkinter.Text(mainGUI)
    txt.pack()
    mainGUI.mainloop()

p = multiprocessing.Process(target=startMainGUI)
p.start()

os.system("python2 main.py 2>/dev/null")

