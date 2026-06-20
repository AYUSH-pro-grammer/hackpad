# Hackpad

Hi there! Here is my personal Hack Club macropad.

It is a compact 3x3 keyboard meant for shortcuts, programming and gaming.  
The keyboard consists of a Seeed XIAO RP2040 microcontroller, OLED screen, and mechanical switches.

## What it includes
- 3x3 mechanical switches
- 0.91" OLED screen
- Seeed XIAO RP2040
- 3D-printed housing
- Custom PCB designed in KiCad

## Images

### Schematic
![Schematic](image/schematic.png)

### PCB Layout
![PCB Layout](image/pcb.png)

### 3D Front View
![PCB 3D Front](image/pcb-3d-front.png)

### 3D Back View
![PCB 3D Back](image/pcb-3d-back.png)

### Render 1
![Render 1](image/3d1.png)

### Render 2
![Render 2](image/3d2.png)


## Bill of Materials

These are the parts I used for my hackpad:

| Part                      | Purpose                                | Qty | Reference / Purchase Link                                                                                                  |
| ------------------------- | -------------------------------------- | --- | -------------------------------------------------------------------------------------------------------------------------- |
| PCB                       | Main board for soldering all the parts | 1   | Custom designed PCB                                                                                                        |
| Seeed XIAO RP2040         | Main controller                        | 1   | [Seeed XIAO RP2040 Official Product Page](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?utm_source=chatgpt.com) |
| MX Switches               | The 3×3 keys                           | 9   | [Cherry MX Switches](https://www.cherry.de/en-gb/product/mx2a-switches?utm_source=chatgpt.com)                             |
| Keycaps                   | For the switches                       | 9   | [Keycap Set Example](https://www.keychron.com/collections/keycaps?utm_source=chatgpt.com)                                  |
| 1N4148 Diodes             | Prevent ghosting in the key matrix     | 9   | [1N4148 Diode Datasheet (Vishay)](https://www.vishay.com/docs/81857/1n4148.pdf?utm_source=chatgpt.com)                     |
| 0.91" OLED Display        | Shows info on the screen               | 1   | [0.91 inch OLED Display Example](https://www.waveshare.com/0.91inch-oled-module.htm?utm_source=chatgpt.com)                |
| LED                       | Blinks when a key is pressed           | 1   | Standard 5 mm LED                                                                                                          |
| Current-limiting resistor | Protects the LED                       | 1   | 220 Ω resistor                                                                                                             |
| 3D Printed Case           | Holds everything together              | 1   | Custom designed and printed case                                                                                           |


## Project files structure
- `kicad/` - PCB files
- `cad/` - 3D models
- `grb/` - gerber files for manufacturing
- `image/` - screenshots and renders

## Parts list
- 9x MX-style switches
- 9x keycaps
- 1x Seeed XIAO RP2040
- 1x 0.91" OLED screen
- 9x diodes
- 1x custom PCB
- 1x 3D-printed housing

## Firmware
For firmware I used CircuitPython.

### Brief steps
1. Load CircuitPython on the XIAO RP2040
2. Move necessary libraries onto the board
3. Upload `code.py` file 
4. Connect and test the switches

## Images
The images with PCB and 3D render can be found in the `image/` folder.
