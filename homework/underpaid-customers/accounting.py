melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

customer1_expected = customer1_melons * melon_cost
if customer1_expected != customer1_paid:
    print(f"{customer1_name} paid ${customer1_paid:.2f},",
          f"expected ${customer1_expected:.2f}"
          )

customer2_expected = customer2_melons * melon_cost
if customer2_expected != customer2_paid:
    print(f"{customer2_name} paid ${customer2_paid:.2f},",
          f"expected ${customer2_expected:.2f}"
          )

customer3_expected = customer3_melons * melon_cost
if customer3_expected != customer3_paid:
    print(f"{customer3_name} paid ${customer3_paid:.2f},",
          f"expected ${customer3_expected:.2f}"
          )

customer4_expected = customer4_melons * melon_cost
if customer4_expected != customer4_paid:
    print(f"{customer4_name} paid ${customer4_paid:.2f},",
          f"expected ${customer4_expected:.2f}"
          )

customer5_expected = customer5_melons * melon_cost
if customer5_expected != customer5_paid:
    print(f"{customer5_name} paid ${customer5_paid:.2f},",
          f"expected ${customer5_expected:.2f}"
          )

customer6_expected = customer6_melons * melon_cost
if customer6_expected != customer6_paid:
    print(f"{customer6_name} paid ${customer6_paid:.2f},",
          f"expected ${customer6_expected:.2f}"
          )

mellon_cost = 1.00 #universal variable

def payment_status(payment_data_file):
    '''Calculate cost of melon order to determine customer payment status.'''

    payment_data = open(payment_data_file) #we are opening a data file and assigning a variable to it.

    for line in payment_data: #iterating the payment data file.
        order = line.split('')  #the line is going to split on the white space to get a list of strings.
        full_name = order[1] #assigning customers full name and assigning it the index of 1.
        first_name = full_name.split('')[0] #customers full name will get split by the white space and we are assigning first name to the index 0.
        #number of melons purchased is needed to calculate if what the customer paid was accurate.
        melons_qty = float(order[2]) #float numbers can help us keep track of the money in dollars and cents.
        customer_payed = float(order[3])
        #calculating price of the customer order.
        price = mellon_cost * melons_qty
    #printing general customer order information.
    print(f"{first_name} payed {customer1_paid}, price expected was {price}")
    #print payment status the if statement will print if they have underpaid or overpaid for the melons.
    if customer1_paid != price:

        if customer1_paid < price:
            payment_status = 'underpaid'
        elif customer1_paid > price:
            payment_status = 'overpaid'

        print(f"{first_name} has {payment_status} for their melons")

    payment_data.close() #closing the file

    print(payment_status) #calling the function


