class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"\nCountry: {self.country}\nCode: {self.code}\n"
                f"Product: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}")

# List to store Shoe objects
shoe_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                shoe_data = line.strip().split(",")
                if len(shoe_data) == 5:
                    shoe_list.append(Shoe(*shoe_data))
    except FileNotFoundError:
        print("This file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def capture_shoes():
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
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    try:
        min_quantity = float('inf')
        shoe_to_restock = None

        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                shoe_data = line.strip().split(",")
                if len(shoe_data) == 5:
                    quantity = int(shoe_data[4])
                    if quantity < min_quantity:
                        min_quantity = quantity
                        shoe_to_restock = Shoe(*shoe_data)

        if shoe_to_restock:
            print(f"The shoe with the lowest quantity is '{shoe_to_restock.product}' and it has {min_quantity} pairs.")
            restock_quantity = int(input("How many pairs do you want to add? "))
            new_quantity = min_quantity + restock_quantity

            for shoe in shoe_list:
                if shoe.code == shoe_to_restock.code:
                    shoe.quantity = new_quantity

            with open("inventory.txt", "w") as file:
                for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        else:
            print("No shoes available for restocking.")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_shoe():
    try:
        bar_code = input("Please enter the shoe's code: ")
        found = False
        with open("inventory.txt", "r") as file:
            for line in file:
                shoe_code = line.strip().split(",")
                if bar_code == shoe_code[1]:
                    print(line.strip())
                    found = True
                    break
        if not found:
            print("Shoe code not found.")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def value_per_item():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                shoe_data = line.strip().split(",")
                if len(shoe_data) == 5:
                    cost = float(shoe_data[3])
                    quantity = int(shoe_data[4])
                    value_cost = cost * quantity
                    print(f"The total value for {shoe_data[2]} is {value_cost}.")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def highest_qty():
    try:
        shoe_for_sale = None
        max_quantity = 0
        with open("inventory.txt", "r") as file:
            for line in file:
                shoe_data = line.strip().split(",")
                if len(shoe_data) == 5:
                    quantity = int(shoe_data[4])
                    if quantity > max_quantity:
                        max_quantity = quantity
                        shoe_for_sale = shoe_data

        if shoe_for_sale:
            print("The shoe with the highest quantity is:")
            print(f"Country: {shoe_for_sale[0]}")
            print(f"Code: {shoe_for_sale[1]}")
            print(f"Product: {shoe_for_sale[2]}")
            print(f"Cost: {shoe_for_sale[3]}")
            print(f"Quantity: {shoe_for_sale[4]}")
        else:
            print("No shoes available for sale.")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
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
