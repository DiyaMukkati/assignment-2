try:
    m1 = int(input("Enter subject 1 marks: "))
    m2 = int(input("Enter subject 2 marks: "))
    m3 = int(input("Enter subject 3 marks: "))
    m4 = int(input("Enter subject 4 marks: "))
    m5 = int(input("Enter subject 5 marks: "))

    total = m1 + m2 + m3 + m4 + m5
    percent = total / 5

    if percent >= 90:
        grade = "A+"
    elif percent >= 80:
        grade = "A"
    elif percent >= 70:
        grade = "B"
    elif percent >= 60:
        grade = "C"
    elif percent >= 50:
        grade = "D"
    else:
        grade = "F"

    if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\nTotal:", total)
    print("Percentage:", percent)
    print("Grade:", grade)
    print("Result:", result)

except:
    print("Invalid input")