print ("newton's Second law of motion")
print("____________________________________________________")
print("selecting the missing value:")
print("1.Mass(m)")
print("2.acceleration(a)")
print("3.Force(F)")
missing_value_choice=input("enter the option value :")

if missing_value_choice=="1":
    a=float(input("Enter acceleration(a):"))
    F=float(input("Enter forcr(F):"))
    m=F/a
    print(f"mass(m)={m}")


elif missing_value_choice=="2":
    m=float(input("Enter mass(m):"))
    F=float(input("Enter forcr(F):"))
    a=F/m
    print(f"acceleration(a)={a}")


elif missing_value_choice=="3":
    m=float(input("Enter mass(m):"))
    a=float(input("Enter acceleration(a):"))
    F=m*a
    print(f"Force(F)={F}")
 


else:
    print("invalid option")

