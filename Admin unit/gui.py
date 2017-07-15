import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import login

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

from PIL import ImageTk, Image, ImageDraw, ImageColor
import threading
import time
import socket
import os
import random


s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 420                      # Reserve a port for your service.
s.bind((host, port))            # Bind to the port
clientML = None
clientIP = None


loggedIn = False

LARGE_FONT = {"Verdana", 12}
style.use("ggplot")    #ggplot, dark_background, grayscale

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

f1 = Figure(figsize=(5,5), dpi=100)
a1 = f1.add_subplot(111)

f2 = Figure(figsize=(5,5), dpi=100)
a2 = f2.add_subplot(111)

f3 = Figure(figsize=(5,5), dpi=100)
a3 = f3.add_subplot(111)

entranceMap = [30, 31, 35, 32, 30, 28, 29, 27, 30, 32, 36, 40, 35]
checkMap = [32, 30, 30, 31, 35, 28, 29, 36, 40, 35, 27, 30, 32]
securityMap = [30, 28, 29, 30, 31, 35, 32, 27, 40, 35, 30, 32, 36]


def checkLogin():
    global loggedIn
    loggedIn = login.login()
    print(loggedIn)
    if loggedIn == True:
        pass
    else:
        tkinter.messagebox.showinfo("Login Failed", "Incorrect Username or Password.")
        exit(0)


def UpdateArrayData():
    f = open("sampleText.txt", "r")
    arr = []
    s = f.readline()
    while s:
        arr.append(s)
        s = f.readline()
    f.close()
    # print("ARR", arr)
    f = open("sampleText.txt", "w")
    i = 1
    for x in arr[1:]:
        f.write(str(i) + "," + x.split(",")[1])
        # print(str(i) + "," + x.split(" ")[1])
        i += 1
    f.write("\n" + str(i) + "," + str(random.randrange(15, 26)))
    # print(str(i) + " " + str(random.randrange(15, 26)) + "\n")
    f.close()


def animate(i):
    UpdateArrayData()
    pullData = open("sampleText.txt", "r").read()
    dataList = pullData.split("\n")
    X = []
    Y = []
    # print(dataList)
    for z in dataList:
        if len(dataList) > 1:
            x, y = z.split(',')
            X.append(int(x))
            Y.append(int(y))
    a.clear()
    a.plot(X, Y)


def animate1(i):
    global entranceMap
    del entranceMap[0]
    x = random.randrange(25, 45)
    while abs(x - entranceMap[-1]) > 5:
        x = random.randrange(25, 45)
    entranceMap.append(x)
    Y = [i for i in range(len(entranceMap))]
    a1.clear()
    a1.plot(Y, entranceMap)


def animate2(i):
    global checkMap
    del checkMap[0]
    x = random.randrange(25, 45)
    while abs(x - checkMap[-1]) > 5:
        x = random.randrange(25, 45)
    checkMap.append(x)
    Y = [i for i in range(len(checkMap))]
    a2.clear()
    a2.plot(Y, checkMap)


def animate3(i):
    global securityMap
    del securityMap[0]
    x = random.randrange(25, 45)
    while abs(x - securityMap[-1]) > 5:
        x = random.randrange(25, 45)
    securityMap.append(x)
    Y = [i for i in range(len(securityMap))]
    a3.clear()
    a3.plot(Y, securityMap)


def quit():
    exit(0)


def status(container):
    status = tk.Label(container, text="Initializing", bd=1, relief=tk.SUNKEN, anchor=tk.SW)
    status.grid(column=0, sticky=tk.SW)
    def update_status():
        current_status = status["text"]
        if current_status.endswith("..."):
            current_status = "Initializing"
        else:
            current_status += "."

        status["text"] = current_status
        container.after(1000, update_status)
    container.after(1, update_status)


def refreshImage(container):

    # load = Image.open("airport.png")
    load = Image.open("ppp.jpg")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(container, image=render)
    img.pack(fill=tk.X)
    img.image = render
    img.place(x=0, y=45)

    # status = tk.Label(container, text="Initializing", bd=1, relief=tk.SUNKEN, anchor=tk.SW)
    # status.grid(column=0, sticky=tk.SW)
    def update_img1():
        # img.destroy()
        # load = Image.open("airport1.png")
        load = Image.open("ppp1.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(container, image=render)
        img.pack(fill=tk.X)
        img.image = render
        img.place(x=0, y=45)
        # current_status = status["text"]
        # if current_status.endswith("..."):
        #     current_status = "Initializing"
        # else:
        #     current_status += "."

        # status["text"] = current_status
        container.after(5000, update_img2)

    def update_img2():
        # img.destroy()
        # load = Image.open("airport1.png")
        load = Image.open("ppp2.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(container, image=render)
        img.pack(fill=tk.X)
        img.image = render
        img.place(x=0, y=45)
        # current_status = status["text"]
        # if current_status.endswith("..."):
        #     current_status = "Initializing"
        # else:
        #     current_status += "."

        # status["text"] = current_status
        container.after(5000, update_img3)

    def update_img3():
        # img.destroy()
        # load = Image.open("airport1.png")
        load = Image.open("ppp3.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(container, image=render)
        img.pack(fill=tk.X)
        img.image = render
        img.place(x=0, y=45)
        # current_status = status["text"]
        # if current_status.endswith("..."):
        #     current_status = "Initializing"
        # else:
        #     current_status += "."

        # status["text"] = current_status
        container.after(5000, update_img4)

    def update_img4():
        # img.destroy()
        # load = Image.open("airport1.png")
        load = Image.open("ppp4.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(container, image=render)
        img.pack(fill=tk.X)
        img.image = render
        img.place(x=0, y=45)
        # current_status = status["text"]
        # if current_status.endswith("..."):
        #     current_status = "Initializing"
        # else:
        #     current_status += "."

        # status["text"] = current_status
        container.after(5000, update_img1)
    container.after(5000, update_img1)


def refreshImageThree(container):
    # load = Image.open("airport.png")
    load = Image.open("airportchange.jpg")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(container, image=render)
    img.pack(fill=tk.X)
    img.image = render
    img.place(x=0, y=45)

    # status = tk.Label(container, text="Initializing", bd=1, relief=tk.SUNKEN, anchor=tk.SW)
    # status.grid(column=0, sticky=tk.SW)
    def update_img():
        # img.destroy()
        # load = Image.open("airport1.png")
        load = Image.open("airportchange.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(container, image=render)
        img.pack(fill=tk.X)
        img.image = render
        img.place(x=0, y=45)
        # current_status = status["text"]
        # if current_status.endswith("..."):
        #     current_status = "Initializing"
        # else:
        #     current_status += "."

        # status["text"] = current_status
        container.after(5000, update_img)

    container.after(5000, update_img)


def intializeSocketClients():
    print("Entered intializeSocketClients()")
    global clientIP
    global clientML
    while clientIP == None or clientML == None:
        s.listen(5)
        c, addr = s.accept()     # Establish connection with client.
        temp = c.recv(4096)
        print(temp.decode())
        if "IP" in temp.decode():
            clientIP = c
            print("IP connected with address : ", addr)
        elif "ML" in temp.decode():
            clientML = c
            print("ML connected with address : ", addr)
    print("All clients connected")


dictOfAllPoints = {'cam1':[[], []], 'cam2':[[], []], 'cam3':[[], []], 'cam4':[[], []]}
dictOfCoOrdinates = {"cam1":[704.0,576.0,352.0,288.0,107.0,160.0,166.0,80.0,338.0,336.0,471.0,459.0],
                     "cam2":[704.0,576.0,409.0,288.0,164.0,217.0,223.0,137.0,338.0,336.0,471.0,459.0],
                     "cam3":[704.0,576.0,466.0,288.0,221.0,274.0,260.0,164.0,338.0,336.0,471.0,459.0],
                     "cam4":[704.0,576.0,523.0,288.0,278.0,331.0,317.0,211.0,338.0,336.0,471.0,459.0]}
# order X, Y, x, y, a1, a2, a3, a4, b1, b2, b3, b4


class UpdateImage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            print(clientML.recv(4096))
            # im = Image.open("Airportincomp.jpg")
            # draw = ImageDraw.Draw(im)
            # # getPoints
            # # plot all using loop
            # x = ['110', '340', '683', '192', '304', '555', '165', '225', '310', '366', '422', '553', '618', '672',
            #      '124', '205', '354', '418', '564', '628', '180', '437']
            # y = ['352', '250', '51', '565', '565', '565', '353', '351', '353', '353', '353', '353', '353', '353', '242',
            #      '242', '242', '248', '246', '246', '54', '54']
            #
            #
            # for i in range(0, 21):
            #     RandomTime = str(int(100 * random.random()))
            #     draw.text((int(x[i]), int(y[i])), RandomTime + " min", (255, 255, 255))
            #
            # del draw
            # im.save("airportchange.jpg")
            # time.sleep(10)


def forResourceAllocation(dict):
    X = []
    Y = []
    for key,value in dict.items():
        for x in range(len(value[0])):
            X.append(int(value[0][x]))
            Y.append(int(value[1][x]))
            dictOfAllPoints.pop(key)
            dictOfAllPoints[key] = [X, Y]


def convCoord(array):
    [X,Y,x,y,a1,a2,a3,a4,b1,b2,b3,b4] = array
    n = x/X
    m = (X-x)/X                 #obtained values of m and n

    Ax = ((a1 * m + a2 * n) / (m + n))
    Ay = ((b1 * m + b2 * n) / (m + n))     #co-ordinates of A found

    i = y / Y
    j = (Y - y) / Y             #values of i and j

    Bx = ((a4 * i + a1 * j) / (i + j))
    By = ((b4 * i + b1 * j) / (i + j))  # co-ordinates of B found

    mA = ((a1 - a2) / (b2 - b1))
    mB = ((a1 - a4) / (b4 - b1))

    a = ((Ay - By) - ((mA*Ax)-(mB*Bx))) / (mB-mA)
    b = Ay + mA*(a-Ax)

    return int(a),int(b)


class CommunicationStarter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        intializeSocketClients()
        t1 = ReceiveFromIP()
        t1.start()
        # t3 = UpdateImage()
        # t3.start()


class ReceiveFromIP(threading.Thread):
    global clientIP
    global clientML
    def __init__(self):
        threading.Thread.__init__(self)

    def stripData(self, s):
        temp = []
        s1 = str(s).replace("b'", "")
        s1.replace("'", "")
        # s1 = s1[1:]
        s1 = s1[:-1]
        s2 = s1.split(":")
        # print(s2[0])
        # print(s2[1])
        # print("s2:", s2)
        s2[1] = s2[1].replace("[", "")
        s2[1] = s2[1].replace("]", "")
        for x in s2[1].split("\\n"):
            y = x.split(" ")
            while "" in y:
                y.remove("")
            temp.append(y)
            # print(y)
        return {s2[0]:temp}

    def run(self):
        while True:
            dict = self.stripData(clientIP.recv(4096))
            # print(dict)
            for key,value in dict.items():
                # print("determination : ", key)
                # differentiating data into service time, coordinates, alerts
                if key[1:-1].islower():
                # if key[:-1].islower():
                    # send dict to Ml
                    print("check : ", dict)
                    clientML.send(str(dict).encode())
                    # use this dict for resource
                    forResourceAllocation(dict)
                else:
                    pass


class Alerts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(20)
        str = "Bag Found \n Cam1 \n Unattended 10min"
        tk.messagebox.showwarning("Unattended Baggage", str)


class UpdateImage2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            im = Image.open("airport1.png")
            draw = ImageDraw.Draw(im)
            # data = {'cam1':12, 'cam2':13}
            # getPoints
            # plot all using loop
            # draw.point((100, 100), ImageColor.getrgb("white"))
            del draw
            im.save("airport1.png")
            time.sleep(10)

class status_bar(threading.Thread):
    def __init__(self, container):
        threading.Thread.__init__(self)
        self.container = container

    def run(self):
        status(self.container)


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="clientIcon.ico")
        tk.Tk.title(self, "Monitoring Station")

        #menu bar
        self.menu()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # status bar
        status_thread = status_bar(container)
        status_thread.start()

        self.frames = {}
        for F in (StartPage, GraphPage, PageThree, ThroughPutCheckIn, ThroughPutEntrance, ThroughPutSecurity):                #, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def menu(self):
        menu = tk.Menu(self)
        tk.Tk.config(self, menu=menu)
        subMenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subSubMenu = tk.Menu(subMenu)
        subMenu.add_cascade(label="Throughput", menu=subSubMenu)
        subSubMenu.add_command(label="Check In", command=lambda : self.show_frame(ThroughPutCheckIn))
        subSubMenu.add_command(label="Entrance", command=lambda : self.show_frame(ThroughPutEntrance))
        subSubMenu.add_command(label="Security", command=lambda : self.show_frame(ThroughPutSecurity))
        subMenu.add_command(label="Distribution Page", command=lambda : self.show_frame(StartPage))
        subMenu.add_command(label="Graph Page", command=lambda : self.show_frame(GraphPage))
        subMenu.add_command(label="Page 3", command=lambda : self.show_frame(PageThree))
        subMenu.add_command(label="Throughput", command=lambda : self.show_frame(ThroughPutPage))
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=quit)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Airport Layout", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        refreshImage(self)
        # b1 = ttk.Button(self, text="Visit Graph Page", command=lambda : controller.show_frame(GraphPage))
        # b1.pack()


class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        b1 = ttk.Button(self, text="back to home", command=lambda :controller.show_frame(StartPage))
        b1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class ThroughPutCheckIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CheckIn Throughput", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        b1 = ttk.Button(self, text="back to home", command=lambda :controller.show_frame(StartPage))
        b1.pack()

        canvas1 = FigureCanvasTkAgg(f1, self)
        canvas1.show()
        canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        canvas1._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class ThroughPutEntrance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Entrance Throughput", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        b1 = ttk.Button(self, text="back to home", command=lambda :controller.show_frame(StartPage))
        b1.pack()

        canvas2 = FigureCanvasTkAgg(f2, self)
        canvas2.show()
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        canvas2._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class ThroughPutSecurity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Security Throughput", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        b1 = ttk.Button(self, text="back to home", command=lambda :controller.show_frame(StartPage))
        b1.pack()

        canvas3 = FigureCanvasTkAgg(f3, self)
        canvas3.show()
        canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        canvas3._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Airport Layout and current Queue Time", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        refreshImageThree(self)
        # b1 = ttk.Button(self, text="Visit Graph Page", command=lambda : controller.show_frame(GraphPage))
        # b1.pack()



#.........MAIN..............
# threadCommunication = CommunicationStarter()
# threadCommunication.start()
t2 = UpdateImage2()
t2.start()
# checkLogin()
app = Main()
t1 = Alerts()
t1.start()
ani = animation.FuncAnimation(f, animate, interval=5000)
ani1 = animation.FuncAnimation(f1, animate1, interval=5000)
ani2 = animation.FuncAnimation(f2, animate2, interval=5000)
ani3 = animation.FuncAnimation(f3, animate3, interval=5000)
app.mainloop()