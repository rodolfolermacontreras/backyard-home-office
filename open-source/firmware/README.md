# Firmware

Code for optional smart controls in the WorkPod Pro.

## Features

- Lighting control (on/off, dimming)
- Ventilator scheduling
- Temperature/humidity monitoring
- Door sensor

## Boards Supported

- ESP32 (recommended)
- Raspberry Pi Pico W

## Getting Started

```bash
# Install dependencies
pip install esptool

# Flash to ESP32
esptool.py --port /dev/ttyUSB0 write_flash 0x0 firmware.bin
```

## Build from Source

```bash
cd src/
# Install PlatformIO
pio run --target upload
```
