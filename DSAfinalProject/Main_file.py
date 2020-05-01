# Author: Agnes Fusese
from Land_Class import Land
from House_class import House
from Property_class import Property
from AdminUser_class import MainUser
import datetime
import sys

# This is an array to hold all admin users
users = []

# Static house property instances
house1 = House('Kigali', 67, 200, False, 54)
house2 = House('Awoshie', 6, 100, True, 4)
house3 = House('Haatso', 5, 700, True, 5)
house4 = House('East_Legon', 4, 900, False, 4)
house5 = House('Kwabenya', 3, 1200, False, 6)

houses = [house1, house2, house3, house4, house5]

# Static land property instances
land1 = Land('Kigali', 67, 200, False, 540)
land2 = Land('Awoshie', 6, 100, True, 400)
land3 = Land('Haatso', 5, 700, True, 500)
land4 = Land('East_Legon', 4, 900, False, 400)
land5 = Land('Kwabenya', 3, 1200, False, 600)

lands = [land1, land2, land3, land4, land5]

properties = []
# land and houses properties combined

for i in houses:
    properties.append(i)
for j in lands:
    properties.append(j)


def add_house():
    # Method to add house by admin user
    log = False
    if len(users) == 0:
        print("Please create users first")
        create_admins()
    else:
        while 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user in users:
                if user.username == username and user.password == password:
                    log = True
            if log:
                repeat1 = True
                repeat2 = True
                repeat3 = True
                print("Successfully Logged In\n")
                location = input("Add the location of the House: ")
                while repeat1:
                    try:
                        rented_times = int(input("How many times has the house been rented out: "))
                        repeat1 = False
                    except:
                        print("\nN0. of times input should be an integer")
                        repeat1 = True

                while repeat2:
                    try:
                        price = int(input("What is the price of the House: "))
                        repeat2 = False
                    except:
                        print("\nPrice input should be an integer")
                        repeat2 = True

                while repeat3:
                    try:
                        no_of_rooms = int(input("How many rooms does this house have?: "))
                        repeat3 = False
                    except:
                        print("\nNo. ot rooms input should be an integer")
                        repeat3 = True

                while 1:
                    f = open("saveData.txt", "a")
                    num_user = len(users) - 1
                    try:
                        rented = int(input("Is the house rented?: \n\n1 for yes and 2 for no: "))
                    except:
                        print('\nThis input accept only Integers')
                    else:
                        if rented == 1:
                            rented_final = True
                            f.write(str(users[
                                            num_user].info()) + ' has added a house successfully at: ' + datetime.datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S") + "\n")
                            f.close()
                            print("House Added successfully. Thank you!!")
                            break
                        elif rented == 2:
                            rented_final = False
                            f.write(str(users[num_user].info()) + ' has added a house successfully at: ' +
                                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                            f.close()
                            print("House Added successfully. Thank you!!")
                            break
                        else:
                            print("Please enter 1 to confirm the house is rented  or 2 otherwise")

                house = House(location, rented_times, price, rented_final, no_of_rooms)
                houses.append(house)
                properties.append(house)
                break

            else:
                print('Username or Password wrong. Please try again')


def add_land():
    # Method to add land by admin user
    log = False
    if len(users) == 0:
        print("Please create users first")
        create_admins()
    else:
        while 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user in users:
                if user.username == username and user.password == password:
                    log = True
            if log:
                repeat1 = True
                repeat2 = True
                repeat3 = True
                print("Successfully Logged In")
                location = input("Add the location of the Land: ")
                while repeat1:
                    try:
                        rented_times = int(input("How many times has the Land been rented out: "))
                        repeat1 = False
                    except:
                        print("\nN0. of times input should be an integer")
                        repeat1 = True

                while repeat2:
                    try:
                        price = int(input("What is the price of the Land: "))
                        repeat2 = False
                    except:
                        print("\nPrice input should be an integer")
                        repeat2 = True

                while repeat3:
                    try:
                        size = int(input("What is the size of the Land?: "))
                        repeat3 = False
                    except:
                        print("\nsize input should be an integer")
                        repeat3 = True

                while 1:
                    f = open("saveData.txt", "a")
                    num_user = len(users) - 1
                    try:
                        rented = int(input("Is the Land rented?: \n\n1 for yes and 2 for no: "))
                    except:
                        print("\nThis input accept only Integers")
                    else:
                        if rented == 1:
                            rented_final = True
                            f.write(str(users[num_user].info()) + ' has added a piece of land successfully at: ' +
                                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                            f.close()
                            print('Land Added successfully. Thank you!!')
                            break
                        elif rented == 2:
                            rented_final = False
                            f.write(str(users[num_user].info()) + ' has added a piece of land successfully at: ' +
                                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                            f.close()
                            print('Land Added successfully. Thank you!!')
                            break
                        else:
                            print("Please enter 1 or 2")

                land = Land(location, rented_times, price, rented_final, size)
                lands.append(land)
                properties.append(land)
                break

            else:
                print('Username or Password wrong. Please try again')


def rent(_property):
    check = True
    # Method to update the status and the number of times a property has been rented.
    _property.RentOutTimes += 1
    _property.rented = True
    print("Location\tPrice\tRooms/Size")
    print(_property.info())
    print("Property Rented by you\n")
    print('You are required to pay ' + str(_property.price) + ' per month')
    while check:
        try:
            time = int(input('\nHow many months do you wish to rent the property: '))
            check = False
        except:
            print("\nNo. of months requires an integer input")
            check = True
    print('The total amount you should pay is: ' + str(_property.price * time))
    f = open("saveData.txt", "a")
    num_users = len(users) - 1
    if num_users < 1:
        f.write(
            'A house has been rented by an anonymous User. Details are as follows: \n' + "Location\tPrice\trooms/Size\n" + str(_property.info()) + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
        f.close()
    else:
        f.write(str(users[num_users].info()) + ' Has rented a property with the following details: \n')

        f.write(str(_property.info()) + 'at: ' +
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
        f.close()


def view_property():
    # This function will display the property collection to normal user
    index = 0
    print("\nHOUSES")
    print("ID\tLocation\tPrice\tRooms/Size\tStatus")
    for house in houses:
        print(str(index) + ". " + house.info() + '\t' + house.status())
        # print("Status: " + house.status())
        index += 1
    print('\n')

    print('LANDS')
    print("ID\tLocation\tPrice\tRooms/Size\tStatus")
    for land in lands:
        print(str(index) + ". " + land.info() + '\t' + land.status())
        # print("Status: " + land.status())
        index += 1

    f = open("saveData.txt", "a")
    num_user = len(users) - 1

    if num_user < 1:
        f.write('An anonymous user viewed the property at:' +
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.close()
    else:
        f.write(str(users[num_user].info()) + ' viewed the property at:' +
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.close()


def create_admins():
    username = input("Create username: ")
    password = input("Create password: ")

    user = MainUser(password, username)
    users.append(user)

    f = open("saveData.txt", "a")
    f.write('A new user was created at:' +
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.close()


def view_property_details():
    # this method displays a more detailed information about properties to the AdminUser
    log = False
    if len(users) == 0:
        print("Please create users first")
        create_admins()

    else:
        while 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user in users:
                if user.username == username and user.password == password:
                    log = True

            if log:
                print("Successfully Logged In")
                index = 0
                for _property in properties:
                    print(str(index) + ". " + _property.property_info())
                    index += 1

                num_user = len(users) - 1
                f = open("saveData.txt", "a")
                f.write(str(users[num_user].info()) + ' viewed the property details at:' +
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                f.close()
                break
            else:
                print("Username or password wrong. Try Again!!")


def get_total_revenue():
    # this
    logged = False
    if len(users) == 0:
        print("Please create users first")
        create_admins()
    else:
        while 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user in users:
                if user.username == username and user.password == password:
                    logged = True
            if logged:
                print("Successfully Logged In")
                total = 0
                for prop in properties:
                    total += prop.Total_revenue()
                print('The total Revenue is: ' + str(total))
                num_user = len(users) - 1
                f = open("saveData.txt", "a")
                f.write(str(users[num_user].info()) + ' viewed the total revenue at' +
                        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                f.close()
                break
            else:
                print("Username or password wrong. Try Again!!")


def main():
    print("\n\n\t\t\t----- Property Rental App -----")
    now = datetime.datetime.now()  # Display time and Date
    print("Current date and time : " + now.strftime("%Y-%m-%d %H:%M:%S"))

    def menu():
        print("\nChoose what you wanna do buddy")
        print("1. Create an Account\n2. Add Houses\n3. Add Land\n4. View Total Revenue\n"
              "5. View Properties\n6. View Property Details\n7. Rent Property\n8. Exit Application")
        runApp()

    def choose_again():
        print("\nWanna perform another operation?")
        while 1:
            try:
                sel = int(input("1. Yes\n2. Exit Application\n: "))
            except:
                print("\nSelection must be an Integer")
            else:
                if sel == 1:
                    menu()
                    break
                elif sel == 2:
                    f = open("saveData.txt", "a")
                    f.write("\nThe user has successfully logged out of the application at: " +
                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                    f.close()
                    print("Thanks for using the app")
                    sys.exit()
                else:
                    print("Select 1 or 2")

    def runApp():
        while True:
            try:
                selection = int(input("Please select one: "))
            except:
                print("\nSelection must be an integer")
            else:
                if selection == 1:
                    create_admins()
                    choose_again()

                elif selection == 2:
                    add_house()
                    choose_again()

                elif selection == 3:
                    add_land()
                    choose_again()

                elif selection == 4:
                    get_total_revenue()
                    choose_again()

                elif selection == 5:
                    view_property()
                    choose_again()

                elif selection == 6:
                    view_property_details()
                    choose_again()

                elif selection == 7:
                    view_property()
                    while True:
                        try:
                            id_prop = int(input("Enter the id of the property to rented: "))
                        except:
                            print("\nProperty ID should be an integer")
                        else:
                            if id_prop < (len(properties)):
                                if properties[id_prop].rented:
                                    print("Property has already been rented")
                                    f = open("saveData.txt", "a")
                                    num_users = len(users) - 1
                                    if len(users) == 0:
                                        f.write(
                                            'An anonymous user tried to rent the property listed below but it is '
                                            'already rented out\n' + str(
                                                properties[id_prop].info()) + "at: " +
                                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
                                        f.close()
                                        choose_again()
                                    else:
                                        f.write(str(users[
                                                        num_users].info())  + 'tried to rent the property listed below but it '
                                                                      'is rented out\n' + str(
                                            properties[id_prop].info()) + "at: " +
                                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n\n')
                                        f.close()
                                    choose_again()
                                else:
                                    rent(properties[id_prop])
                                    choose_again()

                            else:
                                print('Enter a property that exists please')

                elif selection == 8:
                    print("Thank you for using our awesome app!")
                    f = open("saveData.txt", "a")
                    f.write("\nThe user has successfully logged out of the application at: " +
                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                    f.close()
                    sys.exit()

                else:
                    print("Please enter the choices given")
                    menu()

    menu()


main()
