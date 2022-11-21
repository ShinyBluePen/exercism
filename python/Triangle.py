"""Triangle

https://exercism.org/tracks/python/exercises/triangle
""" 

def equilateral(sides: list[int]) -> bool:
    """Determine if a given 'triangle' is equliateral.
    
    :param sides: - A list of 3 int's representing the faces of a triangle.
    :return: bool - True if all ints in `sides` are equal.
    """
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides: list[int]) -> bool:
    """Determine if a given 'triangle' is isosceles.
    
    :param sides: - A list of 3 int's representing the faces of a triangle.
    :return: bool - True if 2 ints in `sides` are equal.
    """
    return is_triangle(sides) and len(set(sides)) < 3

def scalene(sides: list[int]) -> bool:
    """Determine if a given 'triangle' is scalene.
    
    :param sides: - A list of 3 int's representing the faces of a triangle.
    :return: bool - True if all ints in `sides` are different values.
    """
    return is_triangle(sides) and len(set(sides)) == 3

def is_triangle(triangle: list[int]) -> bool:
    """Determine if the given dimensions are valid for a triangle.
    
    :param sides: - A list of 3 int's representing the faces of a triangle.
    :return: bool - True if the ints in `sides` compose a valid triangle.
    """
    if 0 in triangle: return False
        
    if len(triangle) == 3:
        a, b, c = triangle
        if a+b>c and b+c>a and a+c>b:
            return True
        if a+b==c or b+c==a or a+c==b:
            print("degenerate triangle!")
            return True
            
    return False
