print("Movie ticket discount")
print("-----------------------------------------------------------------")

age = int(input("Enter your age: "))
student = input("are you a student (yes/no): ")

if (age <= 12 or ((age >=13 or age <= 18) and student == "yes")):
    print("you are elegible for this discount")

else:
    print("you are not elegible for this discount")