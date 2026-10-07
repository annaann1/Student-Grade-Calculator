name = input("Enter student name: ")
...
... mark1 = float(input("Enter marks for Subject 1: "))
... mark2 = float(input("Enter marks for Subject 2: "))
... mark3 = float(input("Enter marks for Subject 3: "))
... mark4 = float(input("Enter marks for Subject 4: "))
... mark5 = float(input("Enter marks for Subject 5: "))
...
... total = mark1 + mark2 + mark3 + mark4 + mark5
... average = total / 5
...
... if average >= 90:
...     grade = "A+"
... elif average >= 80:
...     grade = "A"
... elif average >= 70:
...     grade = "B"
... elif average >= 60:
...     grade = "C"
... elif average >= 50:
...     grade = "D"
... else:
...     grade = "F"
...
... print("\n--- Student Result ---")
... print("Name:", name)
... print("Total Marks:", total)
... print("Average:", average)

...
Enter student name: anna
Enter marks for Subject 1: 99
Enter marks for Subject 2: 98
Enter marks for Subject 3: 95
Enter marks for Subject 4: 93
Enter marks for Subject 5: 97

--- Student Result ---
Name: anna
Total Marks: 482.0
Average: 96.4
Grade: A+
>>>