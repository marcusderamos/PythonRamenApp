import total_receipt

# DISPLAY WELCOME MESSAGE WITH DELIVERY TIMES
print('''
=============================================
Welcome to Hiroshima Ramen Delivery Service!

Open 7 days a week!

Delivery 1:00pm - 9:00pm
=============================================
''')

# RAMEN MENU DICTIONARY
ramen_menu ={
    1:('Miso Ramen', 13.99),
    2:('Spicy Miso Ramen', 14.99),
    3:('Tonkatsu Ramen', 15.99),
    4:('Spicy Tonkatsu Ramen', 16.99),
    5:('Vegan Ramen', 13.99)
}

# DISPLAY MENU
print("Menu:")
for i, p in ramen_menu.items():
    print('#{}) {}: $ {}'.format(i, p[0], p[1]))

customer_list = []

add_more_items = 'Y'
while add_more_items == 'Y':
    try:
        choice = int(input('\nWhat would you like to order(1-5)? '))
        if choice in ramen_menu.keys():
            customer_list.append((ramen_menu[choice][0], ramen_menu[choice][1]))
        else:
            print('Invalid Choice')
    except ValueError:
        print("Please enter a valid number for your choice.")
    # ASK CUSTOMER TO ADD MORE ITEMS
    add_more_items = input('\nWould you like to add more to your order? (Y for yes, N for no): ').upper()

# GET CUSTOMER INFORMATION
class Customer:
    def __init__(self):
        print("=============================================")
        self.name = input('\nYour Name: ')
        self.age = int(input('Age: '))

    def address(self):
        print("\nEnter delivery address: ")
        self.street = input('Street: ')
        self.city = input('City: ')
        self.state = input('State: ')
        self.zip_code = input('Zip Code: ')
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

    def deliverydate(self):
        print("\nEnter delivery date(DD/MM/YYYY):")
        self.deliverydate = input("Date:")
        return self.deliverydate

    def deliverytime(self):
        print("\nEnter delivery time(HH:MM PM):")
        print("Delivery times: 01:00pm - 09:00pm")
        self.time = input("Time:")
        return self.time
        
# IF CUSTOMER IS SENIOR CITIZEN DISCOUNT IS APPLIED
class SeniorCitizenDiscount(Customer):
    def __init__(self):
        super().__init__()
        if self.age >= 65:
            self.discount = 0.1
        else:
            self.discount = 0

# CREATE ORDER AND CUSTOMER DETAILS
order = SeniorCitizenDiscount()
address = order.address()
delivery_date = order.deliverydate()
delivery_time = order.deliverytime()

#CALCUALTE TOTAL AND DISPLAY RECEIPT
total_receipt.total(customer_list, order.name, delivery_date, address, delivery_time, order.discount)
