import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
media_control = ConsumerControl(usb_hid.devices)


pin_map = {
    "1": board.A2,
    "2": board.A3,
    "3": board.SCK,
    "4": board.A0,
    "5": board.TX,
    "6": board.MISO,
    "7": board.A1,
    "8": board.RX,
    "9": board.MOSI,
}

# Macro assignments
macros = {
    "1": ("keys", (Keycode.CONTROL, Keycode.T)),
    "2": ("media", ConsumerControlCode.PLAY_PAUSE),
    "3": ("keys", (Keycode.WINDOWS, Keycode.L)),

    "4": ("keys", (Keycode.CONTROL, Keycode.C)),
    "5": ("keys", (Keycode.CONTROL, Keycode.V)),
    "6": ("keys", (Keycode.CONTROL, Keycode.X)),

    "7": ("keys", (Keycode.DOWN_ARROW,)),
    "8": ("keys", (Keycode.UP_ARROW,)),
    "9": ("keys", (Keycode.ENTER,))
}


switches = {}

for label, gpio in pin_map.items():
    switch = digitalio.DigitalInOut(gpio)
    switch.direction = digitalio.Direction.INPUT
    switch.pull = digitalio.Pull.UP
    switches[label] = switch


previous_state = set()

while True:
    current_state = {
        label for label, switch in switches.items()
        if not switch.value
    }

    newly_pressed = current_state.difference(previous_state)

    for label in newly_pressed:
        action, command = macros[label]

        if action == "keys":
            keyboard.send(*command)

        elif action == "media":
            media_control.send(command)

    previous_state = current_state
    time.sleep(0.05)
