# Base class
class Device:
    def __init__(self, brand, model):
        self._brand = brand    # Protected (single underscore)
        self._model = model
    
    def device_info(self):
        return f"{self._brand} {self._model}"

# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage   # Private attribute (double underscore)
        self.__battery = battery   

    # Getter for storage
    def get_storage(self):
        return self.__storage
    
    # Setter for storage
    def set_storage(self, new_storage):
        if int(new_storage.replace("GB", "")) > 0:   # Simple validation
            self.__storage = new_storage
        else:
            print("❌ Storage must be positive.")

    # Getter for battery
    def get_battery(self):
        return self.__battery
    
    # Setter for battery
    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            print("❌ Battery must be between 0 and 100.")

    # Method to simulate charging
    def charge(self):
        print(f"⚡ {self.device_info()} charging... Battery at {self.__battery}%")

# Create and test objects
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB", 75)

print("📱 Phone info:", phone1.device_info())
print("💾 Storage:", phone1.get_storage())

phone1.set_storage("512GB")   
print("💾 Updated Storage:", phone1.get_storage())

phone1.set_battery(95)        # valid update
print("🔋 Battery:", phone1.get_battery())

phone1.set_battery(150)       # invalid update (test validation)
