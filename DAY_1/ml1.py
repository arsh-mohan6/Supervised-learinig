import csv

FILE_NAME = "students.csv"


def write_students():
    header = ["Roll No", "Name", "Age", "Grade"]

    students = [
        [1, "Arsh Mohan", 18, "9"],
        [2, "Aditya Das", 18, "10"],
        [3, "Agniv", 19, "8"]
    ]

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)       # write header
        writer.writerows(students)    # write data

    print("Student data written to CSV successfully!")


# Function to read student data from CSV
def read_students():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# Main execution
if __name__ == "__main__":
    write_students()
    print("\nReading student data from CSV:\n")
    read_students()
