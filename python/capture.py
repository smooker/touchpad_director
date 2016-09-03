#!/usr/bin/python2.7
from evdev import UInput, InputDevice, categorize, ecodes as e
from select import select


def sendZoomIn( ui ):
    #"Send Ctrl+Shift+Plus to uinput"
    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
    ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)
    ui.write(e.EV_KEY, e.KEY_EQUAL, 1)
    ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)
    ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)
    ui.write(e.EV_KEY, e.KEY_EQUAL, 0)
    ui.syn()   
    return

def sendZoomOut( ui ):
    #"Send Ctrl+Minus to uinput"
    ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)
    ui.write(e.EV_KEY, e.KEY_MINUS, 1)
    ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)
    ui.write(e.EV_KEY, e.KEY_MINUS, 0)
    ui.syn()   
    return

#triabva da go namiram, zashtoto se smenia
dev = InputDevice('/dev/input/event7')

ui = UInput()

print(dev)
#device /dev/input/event1, name "Dell Dell USB Keyboard", phys "usb-0000:00:12.1-2/input0"

while True:
    x1 = 0;
    y1 = 0;
    r,w,x = select([dev], [], [])
    for event in dev.read():
        #print(categorize(event))
        #print(event)
        #print("code:"+str(event.code))
        #print("type:"+str(event.type))
        #print("asdf:"+str(e.ABS_PRESSURE))
        #ABS_MT_POSITION_X
        #if (event.code == e.ABS_PRESSURE and event.type == 3 and event.value >= 40):
        if (event.code == e.ABS_X and event.type == 3):
            if ( event.value <= 1200 or event.value >= 6000):
                x1 = event.value;
                print("Got X axis lockup:"+str(event.value))
            else:
                x1 = -1;
                
        if (event.code == e.ABS_Y and event.type == 3 and x1 > 0):
            if ( event.value > 800 and event.value <= 5000):     #v obhvat na Y sme
                print("Got Y axis lockup:"+str(event.value))
                if (event.value < (5000-800)/2):
                    print("Got zoomin")
                    sendZoomIn(ui)
                    y1 = event.value;
                else:
                    print("Got zoomout")
                    y1 = event.value;
                    sendZoomOut(ui)
                
            else:
                y1 = -1;
                