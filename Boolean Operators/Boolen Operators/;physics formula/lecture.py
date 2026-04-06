class Car:
    def __init__(self, brand, model, price, color, tax):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.tax = tax

    def showCarInfo(self):
        print("Brand", self.brand)
        print("Model", self.model)
        print("Price", self.price)
        print("Color", self.color)

    def showTax(self):
        t = self.price * self.tax
        print("The tax is", t)

c = Car() #empty object
c.brand = "Toyota"
c.model = "Vios"
c.price = 1000000
c.color = "blue"
c.tax = 0.10
c.showCarInfo()
c.showTax()

c2 = Car("Honda", "SUV", 200000, "white", 0.1)