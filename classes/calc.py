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

    def compare_memory(self, other):
        if self.ram > other.ram:
            print(f"{self.brand} {self.model} has more RAM than {other.brand} {other.model}")
        elif self.ram < other.ram:
            print(f"{self.brand} {self.model} has less RAM than {other.brand} {other.model}")
        else:
            print(f"{self.brand} {self.model} has the same amount of RAM as {other.brand} {other.model}")

com1 = Computer("Dell", "XPS 13", "i5", "16GB RAM")
com1.display_info()
com1.config()
print(id(com1))

com2 = Computer("Apple", "MacBook Pro", "M1", "8GB RAM")
com2.display_info()
com2.config()
print(id(com2))

com1.compare_memory(com2)
