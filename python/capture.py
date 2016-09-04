#!/usr/bin/python2.7
from evdev import UInput, InputDevice, categorize, list_devices, ecodes as e
from select import select
#import gtk
#import wnck
#import glib
#import threading
import re
from subprocess import Popen, PIPE, STDOUT
import evdev

def get_active_window_title():
    root = Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=PIPE)

    for line in root.stdout:
        m = re.search('^_NET_ACTIVE_WINDOW.* ([\w]+)\,.*$', line)
        if m != None:
            id_ = m.group(1)
            id_w = Popen(['xprop', '-id', id_, 'WM_NAME'], stdout=PIPE)
            break

    if id_w != None:
        for line in id_w.stdout:
            match = re.match("WM_NAME\(\w+\) = (?P<name>.+)$", line)
            if match != None:
                return match.group("name")
        return "Active window not found"

#scratchboard :)
#print(categorize(event))
#print(event)
#ABS_MT_POSITION_X
#if (event.code == e.ABS_PRESSURE and event.type == 3 and event.value >= 40):

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
    #"Sends Ctrl+Minus to uinput"
    ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)
    ui.write(e.EV_KEY, e.KEY_MINUS, 1)
    ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)
    ui.write(e.EV_KEY, e.KEY_MINUS, 0)
    ui.syn()   
    return


#todo: get the device based on regex r.g. touchpad.

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)
    if "TouchPad" in device.name:
        print "----------"
        break

dev = InputDevice(device.fn)

ui = UInput()

print(dev)

while True:
    x1 = 0;
    y1 = 0;
    wndTitle = get_active_window_title();
    #print "wnd:"+wndTitle
    r,w,x = select([dev], [], [])
    for event in dev.read():
	if ( "FreeCAD" in wndTitle ):
            #print "Vleznahme"
	    if (event.code == e.ABS_X and event.type == 3):         #we are in X range/area. todo: get MAX_ABS_X and Y (about 1200 and 6000 on mine)
		if ( event.value <= 1600 or event.value >= 6000):
		    x1 = event.value
		    #print("Got X axis lockup:"+str(event.value))
		else:
		    x1 = -1;
	    if (event.code == e.ABS_Y and event.type == 3 and x1 > 0):
		if ( event.value > 500 and event.value <= 6000):     #we are in Y range/area. todo: get MAX_ABS_X and Y (about 5000 and 800 on mine)
		    #print("Got Y axis lockup:"+str(event.value))
		    if (event.value < (5000-800)/2):
			#print("Got zoomin")
			sendZoomIn(ui)
			y1 = event.value
		    else:
			#print("Got zoomout")
			y1 = event.value
			sendZoomOut(ui)
		    
		else:
		    y1 = -1

