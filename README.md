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

## Bill of Materials (BOM)


| Name                                                                                                 | Purpose                                | Quantity | Reference Link                                                                                                                                         | Distributor               |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| PCB                                                                                                  | Main board for soldering all the parts | 1        | Custom-designed PCB                                                                                                                                    | Custom Fabrication        |
| [Seeed XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?utm_source=chatgpt.com) | Main controller                        | 1        | Seeed Studio                                                                                                                                           | Seeed Studio              |
| MX Switches                                                                                          | Mechanical switches for the 3×3 keypad | 9        | [Cherry MX Switch Set](https://keychron.in/product/cherry-mx-switch-set/?utm_source=chatgpt.com)                                                       | Keychron                  |
| Keycaps                                                                                              | Keycaps mounted on the switches        | 9        | [Cherry Colour PBT Keycap Set](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/cherry-colour-pbt-keycap-set/?utm_source=chatgpt.com) | Meckeys                   |
| 1N4148 Diodes                                                                                        | Prevent ghosting in the key matrix     | 9        | [1N4148 Diodes](https://quartzcomponents.com/products/1n4148-zener-diode?utm_source=chatgpt.com)                                                       | Quartz Components         |
| 0.91" OLED Display (128×32 I2C SSD1306)                                                              | Displays status and information        | 1        | [OLED Display Module](https://www.buydisplay.com/i2c-blue-0-91-inch-oled-display-module-128x32-arduino-raspberry-pi?utm_source=chatgpt.com)            | BuyDisplay                |
| 5 mm LED                                                                                             | Indicates device status / key presses  | 1        | Standard 5 mm LED                                                                                                                                      | Local Supplier            |
| 220 Ω Resistor                                                                                       | Limits current through the LED         | 1        | [220 Ω Resistor Pack](https://robocraze.com/products/220-ohm-resistor-pack-of-10?utm_source=chatgpt.com)                                               | RoboCraze                 |
| 3D Printed Case                                                                                      | Encloses and protects the device       | 1        | Custom-designed and 3D printed                                                                                                                         | Local 3D Printing Service |



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
