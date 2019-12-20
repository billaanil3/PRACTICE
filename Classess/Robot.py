class Robot:
    # def __init__(self, name, color, weight):
    #     self.name = name
    #     self.color = color
    #     self.weight = weight
        
    def introduceSelf(self):
        print "My Name is : " + self.name

# r1 = Robot("Anil", "White", 70)
r1 = Robot()
r1.name = "Anil"
r1.color = "White"
r1.weight = 70

r1.introduceSelf()
