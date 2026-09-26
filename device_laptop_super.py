# Create a parent class Device with a method start() that prints "Device Started".
# Create a child class Laptop. Inside the child class, create a method boot() and call the parent class method using super().start().

class Device:
    def start(self):
        return 'Device Started'

class Laptop(Device):
    def boot(self):
        return super().start()

print(Laptop().boot())
