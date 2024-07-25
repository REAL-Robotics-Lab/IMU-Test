import smbus2
import time

def scan_i2c_addresses():
    # Manually transcribed active I2C addresses from the grid
    active_addresses = [
        0x10, 0x15, 0x1c, 0x1f, 0x2d, 0x30, 0x31, 0x33, 0x35, 0x37, 0x3a, 0x3c,
        0x41, 0x44, 0x47, 0x4e, 0x51, 0x52, 0x54, 0x59, 0x5a, 0x5f, 0x61, 0x62,
        0x67, 0x6a, 0x71, 0x74, 0x76
    ]

    path = '/dev/i2c-1'
    print(path)

    # Initialize I2C bus
    bus = smbus2.SMBus(1, force=True)  # Typically, I2C bus 1 is used on Raspberry Pi and similar devices

    for address in active_addresses:
        try:
            # Attempt to read a byte from the device to check if it responds
            response = bus.read_byte(address)
            print(f"Device at 0x{address:02x} responded with byte: {response}")
        except Exception as e:
            print(f"Device at 0x{address:02x} did not respond. Error: {e}")

        time.sleep(0.1)  # Small delay to avoid bus contention

    bus.close()

# Run the scan
scan_i2c_addresses()
