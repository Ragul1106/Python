class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} turned ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} turned OFF")
    
    def operate(self):
        raise NotImplementedError("Subclasses must implement operate()")

class Light(Device):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness
    
    def operate(self):
        if self.is_on:
            print(f"Adjusting {self.name} light to {self.brightness}% brightness")
        else:
            print(f"{self.name} light is off")

class AC(Device):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self.temperature = temperature
    
    def operate(self):
        if self.is_on:
            print(f"Setting {self.name} AC to {self.temperature}°C")
        else:
            print(f"{self.name} AC is off")

class Fan(Device):
    def __init__(self, name, speed=2):
        super().__init__(name)
        self.speed = speed
    
    def operate(self):
        if self.is_on:
            print(f"Setting {self.name} fan to speed {self.speed}")
        else:
            print(f"{self.name} fan is off")

class SmartHub:
    def __init__(self):
        self.devices = []
    
    def add_device(self, device):
        self.devices.append(device)
    
    def control_all(self, command):
        for device in self.devices:
            if command == "on":
                device.turn_on()
            elif command == "off":
                device.turn_off()
            device.operate()
    
    def list_devices(self):
        return [device.name for device in self.devices]