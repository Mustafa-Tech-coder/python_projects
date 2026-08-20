def analyze_grades():
      grades=[]
      while True:
            grade = input("Enter a grade (or type 'done' to finish):\n ")
            if grade.lower() == 'done':
                break
            grades.append(float(grade))
      print(f"grades: {grades}")
      if len(grades) >0:
           average = sum(grades) / len(grades)
           print(f"The average grade is: {average:.2f}")
           top_grade = max(grades)
           print(f"The highest grade is: {top_grade:.2f}")
           lowest_grade = min(grades)
           print(f"The lowest grade is: {lowest_grade:.2f}")
analyze_grades()