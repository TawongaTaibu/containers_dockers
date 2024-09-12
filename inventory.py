class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize a Shoe object with the given attributes.
        
        Args:
            country (str): The country where the shoe is manufactured.
            code (str): The unique code for the shoe.
            product (str): The name of the product.
            cost (float): The cost of the shoe.
            quantity (int): The quantity of shoes available.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """
        Get the cost of the shoe.
        
        Returns:
            float: The cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Get the quantity of the shoes.
        
        Returns:
            int: The quantity of the shoes.
        """
        return self.quantity

    def __str__(self):
        """
        Return a string representation of the Shoe object.
        
        Returns:
            str: The string representation of the Shoe object.
        """
        return (f"\nCountry: {self.country}\nCode: {self.code}\n"
                f"Product: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}")


# List to store Shoe objects
shoe_list = []


def read_shoes_data():
    """
    Read shoe data from 'inventory.txt', create Shoe objects, and append them to the shoe_list.
    Skips the first line and handles file not found errors.
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                if line.strip():  # Skip empty lines
                    shoe_data = line.strip().split(",")
                    if len(shoe_data) == 5:
                        shoe_list.append(Shoe(*shoe_data))
    except FileNotFoundError:
        print("This file does not exist.")
    except Exception as e:
        print("An error occurred:", e)


def capture_shoes():
    """
    Capture data about a shoe from user input, create a Shoe object, and append it to the shoe_list.
    Validates the code length and handles value errors.
    """
    try:
        country = input("Please enter the country: ")
        code = input("Please enter the 8 digit code: ")
        if len(code) != 8:
            raise ValueError("Please make sure that your code is 8 digits.")
        product = input("Please enter the product name: ")
        cost = float(input("Please enter the cost of the shoe: "))
        quantity = int(input(f"Please enter the pairs of {product} available: "))
        shoe_list.append(Shoe(country, code, product, cost, quantity))
    except ValueError as ve:
        print(ve)


def view_all():
    """
    Print the details of all shoes in the shoe_list using the __str__ method of the Shoe class.
    """
    for shoe in shoe_list:
        print(shoe)
def re_stock():
    """
    Find the shoe with the lowest quantity, ask the user if they want to add more pairs,
    and update the quantity in the shoe_list and 'inventory.txt'.
    """
    try:
        # Load all shoes from the file
        temp_shoe_list = []
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                if line.strip():  # Skip empty lines
                    shoe_data = line.strip().split(",")
                    if len(shoe_data) == 5:
                        temp_shoe_list.append(Shoe(*shoe_data))

        # If the list is empty, there is nothing to restock
        if not temp_shoe_list:
            print("No data available for restocking.")
            return

        # Find the shoe with the lowest quantity
        lowest_quantity = min(shoe.get_quantity() for shoe in temp_shoe_list)
        shoe_to_restock = next((shoe for shoe in temp_shoe_list if shoe.get_quantity() == lowest_quantity), None)

        if shoe_to_restock:
            print(f"The shoe with the lowest quantity is '{shoe_to_restock.product}' and it has {lowest_quantity} pairs.")
            restock_quantity = int(input("How many pairs do you want to add? "))
            new_quantity = lowest_quantity + restock_quantity

            # Update quantity in the list
            for shoe in temp_shoe_list:
                if shoe.code == shoe_to_restock.code:
                    shoe.quantity = new_quantity
                    break

            # Write updated list back to the file
            with open("inventory.txt", "w") as file:
                file.write("Country,Code,Product,Cost,Quantity\n")  # Write header
                for shoe in temp_shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        else:
            print("No shoes available for restocking.")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_shoe():
    """
    Search for a shoe in 'inventory.txt' by code and print its details in a user-friendly format if found.
    """
    try:
        bar_code = input("Please enter the shoe's code: ")
        found = False
        
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                if line.strip():  # Skip empty lines
                    shoe_code = line.strip().split(",")
                    if len(shoe_code) == 5 and bar_code == shoe_code[1]:
                        shoe = Shoe(*shoe_code)
                        print("\nShoe Details:")
                        print(f"Country: {shoe.country}")
                        print(f"Code: {shoe.code}")
                        print(f"Product: {shoe.product}")
                        print(f"Cost: ${shoe.cost:.2f}")
                        print(f"Quantity: {shoe.quantity}")
                        found = True
                        break
        
        if not found:
            print("Shoe code not found.")
    
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def value_per_item():
    """
    Calculate and print the total value for each shoe item based on its cost and quantity.
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)  #Skip header
            print("\nTotal Value for Each Shoe Item:\n")
            found_data = False
            for line in file:
                if line.strip():  #Skip empty lines
                    shoe_value = line.strip().split(",")
                    if len(shoe_value) == 5:
                        try:
                            cost = float(shoe_value[3].strip())
                            quantity = int(shoe_value[4].strip())
                            value_cost = cost * quantity
                            print(f"Product: {shoe_value[2]}")
                            print(f"Cost per item: R{cost:.2f}")
                            print(f"Quantity available: {quantity}")
                            print(f"Total value: R{value_cost:.2f}\n")
                            found_data = True
                        except ValueError as ve:
                            print(f"Error processing data for shoe with code {shoe_value[1]}: {ve}")
            
            if not found_data:
                print("No valid shoe data found to calculate the total value.")
                
    except FileNotFoundError:
        print("Error: The inventory file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def highest_qty():
    """
    Determine and print the shoe with the highest quantity from 'inventory.txt'.
    """
    try:
        shoe_for_sale = None
        max_quantity = 0

        with open("inventory.txt", "r") as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    highest_shoe_quantity = line.strip().split(",")
                    if len(highest_shoe_quantity) == 5:
                        quantity = int(highest_shoe_quantity[4])
                        if quantity > max_quantity:
                            max_quantity = quantity
                            shoe_for_sale = highest_shoe_quantity

        if shoe_for_sale:
            print("The shoe with the highest quantity is:")
            print(f"Country: {shoe_for_sale[0]}")
            print(f"Code: {shoe_for_sale[1]}")
            print(f"Product: {shoe_for_sale[2]}")
            print(f"Cost: {shoe_for_sale[3]}")
            print(f"Quantity: {shoe_for_sale[4]}")
        else:
            print("There are no shoes available for sale.")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to display the menu and handle user choices.
    """
    while True:
        print("\nMenu:")
        print("1. Read shoes data from file")
        print("2. Capture new shoes")
        print("3. View all shoes")
        print("4. Shoes that need re-stocking")
        print("5. Search for shoe")
        print("6. Value per item")
        print("7. Product with highest quantity")
        print("q. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice.lower() == "q":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
