# Importing the libraries   76.55718711  37.64053081
import numpy as np
from matplotlib.pyplot import *
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import threading
import socket
import time
import ast


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 420                # Reserve a port for your service.

dictionaryOfEvaluationFunctions = {}
dictionaryOfLengthOfQueue = {}                  # stores the length of the queue whos time has to be calculated
dictionaryOfTimeCurrent = {}
dictionaryOfServiceTime = {'cam1':40, 'cam2':40, 'cam3':40, 'cam4':40}              # TODO : get this real time

def dataToDict(dict):
    global dictionaryOfLengthOfQueue
    for key, value in dict.items():
        # print(key)
        dictionaryOfLengthOfQueue[key] = arrayConverter(value)
        calculateTime(key)


def arrayConverter(value):
    # format [[x, y, w, h], [x, y, w, h], [x, y, w, h]]
    value1 = []
    for x in value:
        value1.append(int(x[0]))
    # print(value)
    value1.sort()
    # print(value1)
    return value1


def calculateTime(key):
    # print(dictionaryOfLengthOfQueue)
    s = dictionaryOfLengthOfQueue[key]
    s.sort()
    s1 = []
    for i in range(len(s)-1):
        if abs(s[i] - s[i+1]) > 25:
            s1.append(s[i])
    x = len(dictionaryOfLengthOfQueue[key])
    print("No. of People in ", key, "are ", x)
    c1 = 76.55718711
    st = dictionaryOfServiceTime[key]
    c2 = 37.64053081
    c3 = 0
    # print("no of people : ", key, x)
    time = (x*st)/60
    # s.send(dictionaryOfTimeCurrent)
    # time = (c1*st + c2*x + c3)/60
    print("time is : ", key, time)
    dictionaryOfLengthOfQueue.pop(key)
    dictionaryOfTimeCurrent[key] = str(time)
    print("dictionaryOfTimeCurrent : ", dictionaryOfTimeCurrent)
    # print("dictionaryOfLengthOfQueue : " ,dictionaryOfLengthOfQueue)


class recieveFromAdmin(threading.Thread):
    client = None
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        s.connect(("192.168.43.238", port))        # Bind to the port
        s.send("ML".encode())
        # while s.recv(1024) != "go!":
        #     pass
        while True:
            # data = b"{'cam1': [['176', '69', '60', '119'], ['337', '101', '43', '85'], ['2', '101', '42', '84'], ['630', '100', '56', '112'], ['470', '64', '64', '127'], ['346', '78', '43', '87'], ['36', '143', '46', '93'], ['582', '125', '43', '87'], ['608', '115', '44', '89'], ['339', '72', '67', '134'], ['467', '158', '43', '86'], ['558', '159', '44', '88'], ['148', '164', '43', '85'], ['347', '21', '51', '103'], ['537', '12', '42', '83'], ['214', '75', '41', '83'], ['4', '57', '51', '102']]}".decode()
            data = s.recv(4096).decode()
            dict = ast.literal_eval(data)
            for key, value in dict.items():
                # print("recieveFromAdmin, before check value : ", value)
                if len(value) < 10:
                    # this is service time
                    dictionaryOfServiceTime[key] = int(value[0][0])
                    # print("recieveFromAdmin after updation : ", dictionaryOfServiceTime)
                    pass
                else:
                    # this is for time calculation
                    dataToDict(dict)
            # time.sleep(10)

    def _delete(self):
        self.client.close()

class sendToCommunicator(threading.Thread):
    client = None
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("yo")
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        self.client = c
        print('Got connection from', addr)
        while True:
            c.send("this is the shit")

    def _delete(self):
        self.client.close()


class sendToAdministrator(threading.Thread):
    client = None
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("yo")
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()     # Establish connection with client.
        self.client = c
        print('Got connection from', addr)
        while True:
           c.send("Wasup nigga")
           time.sleep(10)

    def _delete(self):
        self.client.close()


def compute():
    # Importing the dataset
    dataset = pd.read_csv('50_Startups.csv')
    # print(dataset)
    X = dataset.iloc[:, :-2].values
    y = dataset.iloc[:, 4].values
    # for x in X:
    #     print(x)
    # print("done")
    # x = [[] for x in range(3)]
    # for x1 in X:
    #     x[0].append(x1[0])
    #     x[1].append(x1[1])
    #     x[2].append(x1[2])
    # plot(x[0], y, "bo")
    # plot(x[1], y, "ro")
    # plot(x[2], y, "yo")
    # plot(y, y, "go")
    # show()

    # Encoding categorical data
    # Encoding the Independent Variable
    labelencoder_X = LabelEncoder()
    # X[:, 2] = labelencoder_X.fit_transform(X[:, 2])
    # for x in X:
    #     print(x)
    # exit(0)
    # onehotencoder = OneHotEncoder(categorical_features = [3])
    # X = onehotencoder.fit_transform(X).toarray()
    # for x in X:
    #     print(x)
    #Avoidiung the Dummy Variable Trap
    # X = X[:, 1:]
    # for x in X:
    #     print(x)
    # exit(0)
    # Splitting the dataset into the Training set and Test set
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    X_train = X
    X_test = X
    y_train = y
    y_test = y
    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    print("Xtrain")
    for x in X_train:
        print(x)
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    #Fitting Multiple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    print(regressor.coef_)
    # print("over")

    #Predicting the Test and set results
    y_pred = regressor.predict(X_test)
    i = 0
    for x in range(50):
        print(int(y_pred[x]), "\t\t", int(y_test[x]), "\t\t", int(abs(100*(y_pred[x] - y_test[x])/y_test[x])))
        i += int(abs(100*(y_pred[x] - y_test[x])/y_test[x]))
    print(i)
    a = [i for i in range(50, 0, -1)]
    plot(a, y_test, 'r-')
    plot(a, y_pred, 'b-')
    show()



# ........... MAIN ...........

t1 = recieveFromAdmin()
t1.start()

# t2 = sendToCommunicator()
# t2.start()
#
# t3 = sendToAdministrator()
# t3.start()