class Computer:
    def __init__(self, brand, model, cpu, ram):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram = ram
        print(f"Computer initialized: {self.brand} {self.model} {self.cpu} {self.ram}")
        print("In init")

    def display_info(self):
        print(f"Computer Brand: {self.brand}")
        print(f"Computer Model: {self.model}")
        print(f"Computer CPU: {self.cpu}")
        print(f"Computer RAM: {self.ram}")

    def config(self):
        print("Configuring computer...")
        # Add configuration logic here
        print(f"Configuration: {self.cpu}, {self.ram}")


com1 = Computer("Dell", "XPS 13", "i5", "16GB RAM")
com1.display_info()
com1.config()   

com2 = Computer("Apple", "MacBook Pro", "M1", "8GB RAM")
com2.display_info()
com2.config()


