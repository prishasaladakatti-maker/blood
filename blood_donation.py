import sys

def check_eligibility(age, weight):
    if age >= 18 and age <= 65 and weight >= 50:
        return "Eligible for blood donation"
    else:
        return "Not eligible for blood donation"


if __name__ == "__main__":
    if len(sys.argv) == 3:
        age = int(sys.argv[1])
        weight = float(sys.argv[2])
    else:
        age = int(input("Enter age: "))
        weight = float(input("Enter weight in kg: "))

    result = check_eligibility(age, weight)
    print(result)