# This is just a small Product Data Storage Software where we create a interface for Barcode scanner too
class Billing:
    __Product_ID = None
    __Product_Name = None
    __Product_Company = None
    __Product_Price = 0

    "This is gonna be a Parent class for all type of Billing Info that we are gonna need here"

    def __init__(self):
        self.__Product_ID = None
        self.__Product_Name = None
        self.__Product_Company = None
        self.__Product_Price = 0.00

    # This function will take input from user:
    def get_info(self):
        try:
            self.__Product_ID = input("Enter the value of Product ID:\t")
            self.__Product_Name = input("Enter the Product Name:\t")
            self.__Product_Company = input("Enter the Company Name:\t")
            self.__Product_Price = float(input("Enter the Product Price:\t"))
            return
        except TypeError:
            print("You entered a wrong data:")
            return 0;

    # This will show Class content
    def display_info(self):
        try:
            print("The value of Product ID is:\t"+self.__Product_ID)
            print("The value of Product Name is:\t"+self.__Product_Name)
            print("The value of Product Company is:\t" + self.__Product_Company)
            print("The value of Product Price is:\t"+self.__Product_ID)
        except:
            print("Something went wrong:")
            return 0;


if __name__ == "__main__":
	print("This Main Class Module has been ran directly by user:")
