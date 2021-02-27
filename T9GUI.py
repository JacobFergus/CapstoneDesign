from guizero import App, Text, PushButton, ButtonGroup
import math, random
from gpiozero import DigitalOutputDevice

one20Pin0 = DigitalOutputDevice(23)
one20Pin1 = DigitalOutputDevice(24)

two40Pin0 = DigitalOutputDevice(17)
two40Pin1 = DigitalOutputDevice(27)

four80Pin0 = DigitalOutputDevice(2)
four80Pin1 = DigitalOutputDevice(3)
four80Pin2 = DigitalOutputDevice(4)

def confirm_select():
    voltage = buttonSelect.value
    if voltage == "Off":
        relay_120_Off()
        relay_240_Off()
        relay_480_Off()
    elif voltage == "120":
        relay_240_Off()
        relay_480_Off()
        relay_120_On()
    elif voltage == "240":
        relay_120_Off()
        relay_480_Off()
        relay_240_On()
    elif voltage == "480":
        relay_120_Off()
        relay_240_Off()
        relay_480_On()

def relay_120_On():
    one20Pin0.on()
    one20Pin1.on()
def relay_240_On():
    two40Pin0.on()
    two40Pin1.on()
def relay_480_On():
    four80Pin0.on()
    four80Pin1.on()
    four80Pin2.on()
def relay_120_Off():
    one20Pin0.off()
    one20Pin1.off()
def relay_240_Off():
    two40Pin0.off()
    two40Pin1.off()
def relay_480_Off():
    four80Pin0.off()
    four80Pin1.off()
    four80Pin2.off()
    
def update_values():
    one20_0.value = "120V 0: " + str(random.randrange(20))
    one20_1.value = "120V 1: " + str(random.randrange(20))
    two40_0.value = "240V 0: " + str(random.randrange(20))
    four80_0.value = "480V 0: " + str(random.randrange(20))

buttonOptions = [["120V", "120"],["240V", "240"], ["480V", "480"], ["Off", "Off"]]
app = App("Team 9 Display")

one20_0 = Text(app, text="Current Measurements",color="green", grid=[0,0], width = "fill")
one20_1 = Text(app, text="Current Measurements", color="green",   width = "fill")
two40_0 = Text(app, text="Current Measurements", color="green",   width = "fill")
four80_0 = Text(app, text="Current Measurements", color="green",   width = "fill")
buttonSelect = ButtonGroup(app, options = buttonOptions, selected = "Off", horizontal = True)
PushButton(app, command=confirm_select, text="confirm select")

one20_0.repeat(1000, update_values)


app.display()
