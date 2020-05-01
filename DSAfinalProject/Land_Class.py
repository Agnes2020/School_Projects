# this file includes functions for the land class
from Property_class import Property


# importing the parent file.
class Land(Property):
    def __init__(self, location, rent_out_times, price, rented, size):
        super().__init__(location, rent_out_times, price, rented)
        self.LandSize = size

    def info(self):
        # this method will display information of the land to the ordinary user based on input
        return self.PropertyLocation + '\t' + str(self.price) + '\t' + str(self.LandSize)

    def land_rented(self):
        # This method is used to mark the property as rented once a user rents it
        self.rented = True

    def status(self):
        # This method Checks whether the property is rented and returns the status of the property
        if self.rented:
            return "Rented"
        else:
            return "Not Rented"

    def __str__(self):
        return self.status()
