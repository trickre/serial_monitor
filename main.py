import serial
import threading
import time

#Serial Port
COMPORT_NAME = "COM4"
ser = serial.Serial(COMPORT_NAME,9600,timeout=0.1)

def main():
    print("<<<<< Serial Console >>>>>")
    print("input exit() or 'Ctrl + C' then exit")

    #Send Serial message
    while(True):
        txt_input = input()
        if(txt_input == "exit()"):
            exit()
        else:
            ser.write(txt_input.encode("utf-8"))

def receive():
    time.sleep(1)
    while(True):
        rcv = ser.readline()
        if(rcv != b""):
            print(rcv)
            time.sleep(0.1)

if __name__ == "__main__":
    thread = threading.Thread(target=receive)
    thread.setDaemon(True)
    thread.start()
    main()