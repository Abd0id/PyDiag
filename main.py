def appreciation(moyenne):
    if moyenne <= 9.9:
        return "Insuffisant"
    elif moyenne <= 11:
        return "Passable"
    elif moyenne <= 15:
        return "Good"
    else:
        return "Very Good"


def calculate_avg(notes):

    length = 0
    sum = 0

    for note in notes:
        note = float(note)
        length += 1
        sum += note

    return sum / length

def main():

    name = input("Enter your name: ")
    lastname = input("Enter your last name: ")
    notes = input("Enter your notes: ").split()
    avg = calculate_avg(notes)


    print(f"{name} {lastname}: {avg:.2f}")
    print(f"{avg:.2f} -> {appreciation(avg)}")

if __name__ == "__main__":
    main()