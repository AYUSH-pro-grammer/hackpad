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

## Other notes
This is my first PCB project ever, so it might not be the best design, but it was fun to make one!