import pytest


def classify_triangle(a, b, c):
    try:
            
        if ((type(a)== int or type(a)== float) and (type(b)== int or type(b)== float) and (type(c)== int or type(c)== float)):
            if (a<=0) or (b<=0) or (c<=0):
                return "please enter valid triangle side lengths"
            else:
                if a == b == c:
                    return "Equilateral"
                elif (a==b) or (b==c) or (a==c):
                    
                    if (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
                        return "Right"

                    else:
                        return "Isosceles"

                else:
                    if (a*a + b*b == c*c) or (c*c + b*b == a*a) or (a*a + c*c == b*b):
                        return "Right"

                    else:
                        return "Scalene"

        else:
            return "Inputs can only be numbers"  
    except:
        return "Error occured"

print(classify_triangle(3, 4, 5))


def test_Equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_Isosceles():
    assert classify_triangle(4, 4, 6) == "Isosceles"

def test_Scalene():
    assert classify_triangle(4, 3, 7) == "Scalene"

def test_Right():
    assert classify_triangle(4, 5, 3) == "Right"

def test_NonPositive():
    assert classify_triangle(-6, 3, 3) == "please enter valid triangle side lengths"

def test_NonNumber():
    assert classify_triangle("A String", 3, 3) == "Inputs can only be numbers"



def test_Equilateral_fault():
    assert classify_triangle(2, 3, 3) == "Equilateral"

def test_Isosceles_fault():
    assert classify_triangle(4, 5, 6) == "Isosceles"

def test_Scalene_fault():
    assert classify_triangle(4, 4, 7) == "Scalene"

def test_Right_fault():
    assert classify_triangle(4, 6, 3) == "Right"

def test_NonPositive_fault():
    assert classify_triangle(6, 3, 3) == "please enter valid triangle side lengths"

def test_NonNumber_fault():
    assert classify_triangle(6, 3, 3) == "Inputs can only be numbers"
