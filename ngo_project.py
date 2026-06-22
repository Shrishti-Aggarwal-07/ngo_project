import csv
import os

file_name = "volunteers.csv"

# Generate ID
def generate_id():
    if not os.path.exists(file_name):
        return 1
    with open(file_name, "r") as file:
        reader = list(csv.reader(file))
        if len(reader) == 0:
            return 1
        return int(reader[-1][0]) + 1


# Add volunteer
def add_volunteer():
    vid = generate_id()
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([vid, name, age, city])

    print("✅ Volunteer Added Successfully!")


# View volunteers
def view_volunteers():
    if not os.path.exists(file_name):
        print("No data found.")
        return

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        print("\n--- Volunteer List ---")
        for row in reader:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, City: {row[3]}")


# Search volunteer
def search_volunteer():
    name = input("Enter name to search: ").lower()
    found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if name in row[1].lower():
                print(f"Found: {row}")
                found = True

    if not found:
        print("Volunteer not found.")


# Delete volunteer
def delete_volunteer():
    vid = input("Enter ID to delete: ")
    rows = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != vid:
                rows.append(row)

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Deleted successfully (if ID existed).")


# Count volunteers
def count_volunteers():
    with open(file_name, "r") as file:
        reader = list(csv.reader(file))
        print(f"Total Volunteers: {len(reader)}")


# Main menu
def menu():
    while True:
        print("\n--- NGO Management System ---")
        print("1. Add Volunteer")
        print("2. View Volunteers")
        print("3. Search Volunteer")
        print("4. Delete Volunteer")
        print("5. Count Volunteers")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_volunteer()
        elif choice == "2":
            view_volunteers()
        elif choice == "3":
            search_volunteer()
        elif choice == "4":
            delete_volunteer()
        elif choice == "5":
            count_volunteers()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


menu()