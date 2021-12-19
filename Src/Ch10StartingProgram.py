### Programming Assignment #10:
### Program name: ShippingCalc (Stability Enhanced edition!)
### This program will calculate the shipping cost based on the total purchase price.

def main():
    print("This program will calculate the shipping cost based on "
          "the total purchase price,\n")

    # get the company name and make sure the string is not empty
    company = input('Please enter the company name: ')
    while company == "":
        print("You must enter a company name!")
        company = input('Please enter the company name: ') 

    # Get the total purchase price and check for invalid input
    while True:
        try:
            cost = float(input("Please enter in the purchase price: "))
            break
        except ValueError:
            print('Invalid input. Please enter a number.')

    if cost <= 100.00:
        shipping = 10.0
    elif cost <= 300.00:
        shipping = 8.0
    elif cost <= 500.00:
        shipping = 5.0
    else:
        shipping = 0.0

    total = cost + shipping

    print("At a purchase price of ${:.2f}, the shipping cost will be ${:.2f},"
          " with a final total of ${:.2f}.".format(cost, shipping, total))
    print('{}, thank you for shopping with us!'.format(company))

main()