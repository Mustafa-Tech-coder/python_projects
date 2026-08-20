print("*"*30)
def grades():
    percentage=(total/300)*100
    print("total:",total)
    print("percentage:",percentage,"%")
    if percentage >= 85:
        print("Grade:Excellent")
    elif percentage >=75:
        print("Grade:very good")
    elif percentage >=65:
        print("Grade:good")
    elif percentage >=50:
        print("Grade:pass")
    else:
        print("Grade:fail")
try:
    d1 = float(input("Enter grade 1:\n"))
    d2 = float(input("Enter grade 2:\n"))
    d3 = float(input("Enter grade 3:\n"))
    total = d1 + d2 + d3
    grades()
except ValueError:
    print("invalid number entered")
grades()
print("*"*30)