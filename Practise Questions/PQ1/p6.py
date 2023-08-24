def area_Triange(x1, y1, x2, y2, x3, y3):
    # Check for collinearity
    if (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) == 0:
        return None  # Points are collinear, cannot form a triangle
    
    # Check for degenerate triangle
    if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
        return None  # Two points are the same, cannot form a triangle
    
    area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return abs(area)  # Make sure the area is positive

x1, y1 = map(int, input("Enter coordinates of point 1 (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of point 2 (x2 y2): ").split())
x3, y3 = map(int, input("Enter coordinates of point 3 (x3 y3): ").split())

triangle_area = area_Triange(x1, y1, x2, y2, x3, y3)

if triangle_area is None:
    print("The points cannot form a triangle.")
else:
    print("Area of the triangle:", triangle_area)
