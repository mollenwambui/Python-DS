class Vehicle:
    color="White"
    def __init__(self,name,max_speed,mileage) :
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def car(self)  :
        return f"Wow congratulations on buying a {self.color} {self.name} with a speed of {self.max_speed} and {self.mileage} mileage"  

    def sitting_capacity(self,capacity)  :
        return f"your {self.name} can carry {capacity} passengers"  