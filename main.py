import sys

def sort_students(results):
    results = sorted(results.items(), key=lambda item: item[1], reverse=True)
    return results

def get_failing_students(results):
    # Extraction dans une liste de tuples avec une compréhension de liste
    return [(name, avg) for name, avg in results.items() if avg < 10]

def appreciation(moyenne):
    if moyenne <= 9.9:
        return "Insufficient"
    elif moyenne <= 11:
        return "Passable"
    elif moyenne <= 15:
        return "Good"
    else:
        return "Very Good"

def check_notes(notes):
    for note in notes:
        try:
            note = float(note)
        except ValueError:
            print("INVALID VALUE!: "+note)
            return False
    return True


def calculate_avg(notes):

    if not check_notes(notes):
        sys.exit(0)

    length = 0
    sum = 0

    for note in notes:
        note = float(note)
        length += 1
        sum += note

    if length == 0:
        return 0

    return sum / length

def get_student():
    name = input("Enter your name: ")
    lastname = input("Enter your last name: ")
    notes = input("Enter your notes: ").split()



    return {"name":name+" "+lastname,"notes":notes}

def main():
    students = []
    results = {}

    while(1):
        print("0. To exit the program")
        print("1. To Enter a student")
        print("2. To see results")
        print("3. To sort students")
        print("4. To see failing students")
        choice = input("Enter your choice: ")

        match choice:
            case "0":
                sys.exit(0)
            case "1":
                students.append(get_student())
            case "2":
                for student in students:
                    results[student["name"]] = calculate_avg(student["notes"])
                    print(f"{student["name"]}: {results[student["name"]]:.2f} {appreciation(results[student["name"]])}")

                best_score = 0
                worse_score = 100
                for student in students:
                    avg = calculate_avg(student["notes"])
                    if (worse_score >= avg):
                        worse_score = avg
                        worse_student = student["name"]

                    if (best_score <= avg):
                        best_score = avg
                        best_student = student["name"]

                print("The best student: "+best_student)
                print("The worst student: " +worse_student)
            case "3":
                for name, avg in sort_students(results):
                    print(f"{name}: {avg:.2f} {appreciation(avg)}")
            case "4":
                # Ensure results is populated
                for student in students:
                    results[student["name"]] = calculate_avg(student["notes"])
                    
                failing = get_failing_students(results)
                if failing:
                    print("Failing students:")
                    for name, avg in failing:
                        print(f"{name}: {avg:.2f} {appreciation(avg)}")
                else:
                    print("No failing students.")

            case _:
                print("Unknown choice")




if __name__ == "__main__":
    main()

