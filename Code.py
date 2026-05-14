
import sqlite3
db = sqlite3.connect('Medals.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM Country INNER JOIN Medals ON Country.country_code = Medals.country_code;")
result = cursor.fetchall()
print("Good evening, welcome to the Olympic Medal Table! What would you like to do?")
def add_country():
    country_code = input("Enter the country code: ").upper()
    country_name = input("Enter the country name: ")
    if not country_code.isalpha() or len(country_code) != 3 or not country_name.isalpha():
        print("Invalid name or code. Country code must be 3 letters and country name must contain only letters.")
        return
    try:
        gold = int(input("Enter the number of gold medals: "))
        silver = int(input("Enter the number of silver medals: "))
        bronze = int(input("Enter the number of bronze medals: "))
    except ValueError:
        print("Invalid input. Please enter a number for medals.")
    cursor.execute("INSERT INTO Country (country_code, country_name) VALUES (?, ?);",(country_code, country_name))
    cursor.execute("INSERT INTO Medals (country_code, gold, silver, bronze) VALUES (?, ?, ?, ?);",(country_code, gold, silver, bronze))
    db.commit()
    print(f"{country_name} has been added to the medal table.")

while True:
    print("-------------------------------\n1. View Medal Table\n2. Add a Country\n3. Remove a Country\n4. Exit\n-------------------------------")
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input. Enter a number.")
    if choice == 1:
        print(f"{'Code':<5}{'Country':<23}{'Gold':<6}{'Silver':<7}{'Bronze':<6}")
        for row in result:
            print(f"{row[0]:<5}{row[1]:<23}{row[3]:<6}{row[4]:<7}{row[5]:<6}")
    elif choice == 2:
        add_country()
    elif choice == 3:
        country_code = input("Enter the country code to remove: ").upper()
        cursor.execute("DELETE FROM Medals WHERE country_code = ?;", (country_code,))
        cursor.execute("DELETE FROM Country WHERE country_code = ?;", (country_code,))
        db.commit()
        print(f"Country with code {country_code} has been removed from the medal table.")
    elif choice == 4:   
        print("Thank you for using the Olympic Medal Table. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")