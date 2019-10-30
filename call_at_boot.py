import os
import pyttsx3

def call_here(inp_string):
    eng = pyttsx3.init()
    eng.setProperty('rate', 125)
    eng.setProperty('voice', 'english+f5')
    eng.say(inp_string)
    eng.runAndWait()

os.chdir("/sys/class/power_supply/BAT0")
f = open("capacity", 'r')

k = f.read().strip("\n")
to_int = int(k)

status_in = open("status", 'r')
curr_status=(status_in.read()).strip("\n")

call_here("battery at ")
call_here(str(to_int))
call_here("percent")
call_here(curr_status)
