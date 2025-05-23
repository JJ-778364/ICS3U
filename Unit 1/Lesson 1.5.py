import math
print("Area of a Norman Window Calculator")
radius = input("Please input a radius: ")
radius = float(radius)
radiuss = math.pow(radius, 2)
areaa = 0.5*math.pi*radiuss
areab = 4*radiuss
totalarea = areab + areaa
print("The area of the window is:", totalarea)
