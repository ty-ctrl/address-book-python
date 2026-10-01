class Dog: 
    def __init__(self, breed, color, age):
        self.breed = breed
        self.breed = color
        self.breed = age

        @parameter
        def year (self):
            return self.age
            
        def __eq__ (self,other):
            if not isinstance(other, Dog):
                return False

            return (self.breed == other.breed and self.color
            == other.color and self.age == other.age)