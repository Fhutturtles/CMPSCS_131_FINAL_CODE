import math
def circle_area(r):
    return(math.pi*(r**2))
radius = float(input("Enter the radius of teh circle: "))
area = circle_area(radius)
print(f"The area of the circle is {area:.2f}square units.")
