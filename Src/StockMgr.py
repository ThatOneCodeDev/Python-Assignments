### Programming Assignment #7: 
### Written by: Jerhyn Huey - Date: 10/12/21
### Program name: StockMgr

def main():
    print("="*15 + " Welocme to StockMgr " + "="*15)
    # Alternative would be to use "with open('inventory.csv','r') as stockPayload"
    stockPayload = input("Please input your current item stock (Comma Deliminated): ")
    print("\n") # Pad the output area
    # Split the user submitted payload at each comma, storing the result in a list.
    stockLst = stockPayload.split(",")
    
    # Stock formatted and for loop appending to it was inspired from the class examples
    stockFormatted = []
    for item in stockLst: # Parse each item into a separate list of cleanly formatted values.
        stockFormatted.append(item.strip().title())

    stockTotal = float()# Init a new float to hold the total price all items in stock.
    indice = int() # Init a new integer as our indice that is used to determine which index we are referring to in our stock list.

    for item in stockLst[::3]:
        # Update the indice to reflect the 3 CSV items for the current loop context.
        indice = stockLst.index(item, indice)
        
        # Calculate the stock total by multiplying the amount of items by sell price.
        itemStockValue = float(stockFormatted[indice + 1]) * float(stockFormatted[indice + 2])

        # Add the total value of the stock of the item at the current indice to the complete stock total.
        stockTotal += itemStockValue

        # Print current row of the table and evenly space interpolated values.
        print(f'{stockFormatted[indice]: <18s} {stockFormatted[indice + 1]: ^12s} {stockFormatted[indice + 2]: ^8s} ${itemStockValue:.2f}')
    # On completion of the loop, we display the total of all stock to the end-user.
    print(f"\nThe total value of all items in stock is: ${stockTotal:.2f}")

if __name__ == "__main__":
    main()