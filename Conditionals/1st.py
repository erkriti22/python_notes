#  Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

n = int(input("Enter your age"))

if n<13:
    print("You are a Child")
elif 20 <=n<=59:
    print("you are adult")
elif n> 60:
    print("you are senior")