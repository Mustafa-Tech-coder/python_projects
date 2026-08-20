def square_area(side):
    return side*side
def rect_area(l,w):
    return l*w
def circle_area(radius):
    return 3.14*radius*radius
def triangle_area(base,height):
    return 0.5*base*height
print("@"*40)
print("1. Square Area " \
"2. Rectangle Area  " \
"3. Circle Area" \
" 4. Triangle Area")
choice=int(input("Enter your choice:\n"))
try:
    if choice==1:
        side=float(input("Enter the side of the square:\n "))
        print("The area of the square is:", square_area(side))
    elif choice==2:
        l=float(input("Enter the length of the rectangle:\n "))
        w=float(input("Enter the width of the rectangle:\n "))
        print("The area of the rectangle is:", rect_area(l,w))
    elif choice==3:
        radius=float(input("Enter the radius of the circle:\n "))
        print("The area of the circle is:", circle_area(radius))
    elif choice==4:
        base=float(input("Enter the base of the triangle:\n "))
        height=float(input("Enter the height of the triangle: \n"))
        print("The area of the triangle is:", triangle_area(base,height))
    else:
        print("Invalid choice!")
except ValueError:
    print("Invalid input!")       
print("@"*40)
