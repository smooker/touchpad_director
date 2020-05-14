#!/bin/bash
xinput list
xinput list-props "AlpsPS/2 ALPS DualPoint Stick"
#	libinput Scroll Method Enabled (315):	0, 0, 1
xinput set-prop "AlpsPS/2 ALPS DualPoint Stick" 315 0, 0, 0
xinput list-props "AlpsPS/2 ALPS DualPoint Stick"
