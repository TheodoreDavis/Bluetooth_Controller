import bluetooth

print("searching for devices...")

target_name = "My Phone"
target_address = None

while True:
    nearby_devices = bluetooth.discover_devices(duration=20, lookup_names=True)
    if nearby_devices != None:
        print("Found a device!")
        break

for addr, name in nearby_devices:
    print("{0} - {1}".format(addr, name))
    time.sleep(5)
    if name == "Xbox Wireless Controller":
        try:
            controller = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            controller.connect((addr,1))
        except bluetooth.btcommon.BlueToothError as e:
            print("Could not connect to device: " + e)
            pass
        while True:
            print(controller.recieve(256))
            time.sleep(1)
