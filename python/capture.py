from evdev import InputDevice, categorize, ecodes
from select import select
dev = InputDevice('/dev/input/event6')

print(dev)
#device /dev/input/event1, name "Dell Dell USB Keyboard", phys "usb-0000:00:12.1-2/input0"

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
#        if event.type == ecodes.EV_KEY:
#            print(categorize(event))
#        if event.type == ecodes.EV_REL:
        print(categorize(event))
        print(event)
