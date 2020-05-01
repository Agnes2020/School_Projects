
# This class will be the Parent file for the Lands and House class and contains all the Parents arguments to be passed.
class Property:
    # It has a constructor and methods that will be used in the House class and Lands class
    def __init__(self, location, rent_out_times, price, rented):
        self.PropertyLocation = location
        self.RentOutTimes = rent_out_times
        self.price = price
        self.rented = rented
        self.TotalRevenue = rent_out_times * price

    def property_info(self):
        # this method will display property information
        return "Property Location:" + self.PropertyLocation + "\n" + "Number of times rented out: " + str(
            self.RentOutTimes) + "\n" + " Price of property:" + str(self.price)

    def Total_revenue(self):
        # this method will show the total revenue from all properties
        return self.TotalRevenue

    def update_rent_time(self):
        # This method will update the rent time by user input
        number_time = int(input("Insert number of times it has been rented: "))
        self.RentOutTimes = number_time + self.RentOutTimes
        return self.RentOutTimes

    def Update_price(self):
        # this method will update the price of a property based on user input.
        new_price = int(input("What is the new price of the property?"))
        self.price = new_price
        return self.price
