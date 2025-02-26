#Write a Python program that calculates the area of a rectangle given its length and width.

length = 12
width = 12
area = length * width
print(area)

def area(l,w):
    return l*w
print(area(11,11))

class area():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def get_area(self):
        area = length*width
        return area
    
myArea = area(12,10)
myArea.get_area()
print(myArea)
