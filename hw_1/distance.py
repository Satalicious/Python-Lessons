"""
.. moduleauthor:: Mathias Schuh <mathias.schuh@hotmail.com>
"""



x1 = float(input("First point's x-coordinate: ")) 
y1 = float(input("First point's y-coordinate: "))

x2 = float(input("Second point's x-coordinate: "))
y2 = float(input("Second point's y-coordinate: "))


result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

result = round(result,4)
print(f"The euclidean distance between the two points is {result:.4f}.")
