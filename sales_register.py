def register_sale():
    name = input("Enter product name: ")
    price = float(input("enter value: "))
    amount =int(input("enter quantity: "))
    
    buys = {
           "product":name,
           "price"  :price,
           "amount":amount 
        }

    return buys
