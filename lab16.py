class Cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

myCar = Cars("Volvo", "XC40")
print(myCar.brand)
print(myCar.model)