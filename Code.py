#Importing 
import sqlite3 
# Variables
database = 'Medals.db'
connecting = "SELECT * FROM Country JOIN Medals ON Country.country_code = Medals.country_code ORDER BY (Medals.gold + Medals.silver + Medals.bronze) DESC;"
adding_country = "INSERT INTO Country (country_code, country_name) VALUES (?, ?);"
adding_medals = "INSERT INTO Medals (country_code, gold, silver, bronze) VALUES (?, ?, ?, ?);"
deleting_country = "DELETE FROM Country WHERE country_code = ?;"
deleting_medals = "DELETE FROM Medals WHERE country_code = ?;"
finding = "SELECT * FROM Country, Medals WHERE Country.country_code = ?;"
duplicate = "SELECT * FROM Country WHERE country_code = ? OR country_name = ?;"
# -----------------------------------------------------
db = sqlite3.connect(database)
cursor = db.cursor()
cursor.execute(connecting) # Joined the two tables together and ordered them
result = cursor.fetchall()
print("Welcome to the Olympic Medal Table! What would you like to do?")
# FUNCTIONS
def adding_country(): #Used to add a country to the medal table
    country_code = input("Country code: ").upper()
    country_name = input("Country name: ")
    cursor.execute(duplicate, (country_code, country_name))
    found = cursor.fetchone()
    if found is not None:
        print("Name or code already existed. Try again")
        return
    if not country_code.isalpha() or len(country_code) != 3 or not country_name.isalpha() :
        print("Invalid name or code. Country code must be 3 letters and country name must contain only letters")
        return
    try:
        gold = int(input("Number of gold medals: "))
        silver = int(input("Number of silver medals: "))
        bronze = int(input("Number of bronze medals: "))
    except ValueError:
        print("Invalid input. Please enter a number")
        return
    #Inserting country and medals inside the tables
    cursor.execute(adding_country, (country_code, country_name))
    cursor.execute(adding_medals, (country_code, gold, silver, bronze))
    db.commit()
    print(f"{country_name} has been added to the table")
def removing_country(): #Removing a country
    country_code = input("Enter the country code to remove: ").upper()
    cursor.execute(deleting_medals, (country_code,))
    cursor.execute(deleting_country, (country_code,))
    db.commit()
    print(f"{country_code} has been removed from the table")
def finding_country():#Finding a country
    country_code = input("Enter the country code to find: ").upper()
    cursor.execute(finding, (country_code,))
    country = cursor.fetchone()
    if country is not None:
        print(f"{'Code':<5}{'Country':<23}{'Gold':<6}{'Silver':<7}{'Bronze':<6}")
        print(f"{country[0]:<5}{country[1]:<23}{country[3]:<6}{country[4]:<7}{country[5]:<6}")
    else:
        print(f"No country found")
# MAIN CODE
while True:
    print("-------------------------------\n1. View Medal Table\n2. Add a Country\n3. Remove a Country\n4. Find a Country\n5. Exit\n-------------------------------")
    #Main layout of the program
    try:
        Choose = int(input("What do you wanna do? "))
    except ValueError:
        print("Invalid. Enter a number")
        #If invalid then asked again
    if Choose == 1:
        print(f"{'Code':<5}{'Country':<23}{'Gold':<6}{'Silver':<7}{'Bronze':<6}")
        for row in result:
            print(f"{row[0]:<5}{row[1]:<23}{row[3]:<6}{row[4]:<7}{row[5]:<6}")
    elif Choose == 2: #If the user wants to add a country  
        adding_country()
    elif Choose == 3: #If the user wants to remove a country
        removing_country()
    elif Choose == 4: #If the user wants to find a country
        finding_country()
    elif Choose == 5: #If the user wants to exit the program
        print("Thank you for using the Olympic Medal Table. Goodbye!")
        break
    else:
        print("Invalid. Please try again")
        #If it's invalid