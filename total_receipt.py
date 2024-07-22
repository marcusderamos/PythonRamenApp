tax = 0.0775

def total(customer_list, name, deliverydate, address, time, discount):
    subtotal = sum(i[1] for i in customer_list)

    # DISPLAY RECEIPT
    print("\n=======================================")
    print("****ORDER SUMMARY****")
    print("ITEMS:")
    print(customer_list)
    print('Name:', name)
    print('Delivery date:', deliverydate)
    print('Delivering to:', address)
    print('Time of delivery:', time)
    print('\nSubtotal: $ {:.2f}'.format(subtotal))

    # DELIVERY FEE
    delivery_fee = subtotal * 0.05
    print('Delivery fee: $ {:.2f}'.format(delivery_fee))

    # TAX
    t_amount = tax * subtotal 
    print('Tax: $ {:.2f}'.format(t_amount))

    # DISCOUNT
    discount_amount = subtotal * discount
    if discount > 0:
        print(f'Senior citizen discount: $ -{discount_amount:.2f}')

    # TOTAL
    total_amount = subtotal + t_amount + delivery_fee - discount_amount
    print('Total: $ {:.2f}'.format(total_amount))

    receipt(customer_list, subtotal, total_amount, delivery_fee, name, deliverydate, address, time, discount_amount)


# CREATING A SAVED FILE FOR RECEIPT
def receipt(customer_list, subtotal, total_amount, delivery_fee, name, deliverydate, address, time, discount_amount):
    with open('receipt.txt', 'w') as fout:
        fout.write('**** RECEIPT ****\n')
        fout.write('Item        Price\n')
        fout.write('----        -----\n')

        for i in customer_list:
            fout.write('{} $ {:.2f}\n'.format(i[0], i[1]))

        fout.write('''
------------------------------
Name:    {}
Delivery Date: {}
Delivering to: {}
Time of delivery: {}
------------------------------
Subtotal:    $ {:.2f}
Delivery Fee:    $ {:.2f}
Tax:        $ {:.2f}
Discount:   $ -{:.2f}
Total:      $ {:.2f}
------------------------------
Thank you for choosing Hiroshima Ramen!
'''.format(name, deliverydate, address, time, subtotal, delivery_fee, subtotal * tax, discount_amount, total_amount))

    print('\nYour receipt has been printed in the receipt.txt file')
