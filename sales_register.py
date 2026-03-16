#validations
def register_sale():
    # name validation
    counter_name=1
    while counter_name ==1:
            # Request user data
            name = input("enter product name: ")
            if not name.isalpha():
                print("Symbols and Numbers are not allowed")
                continue
            
            counter_name +=2
    
    # price validation
    counter_price=1
    while counter_price ==1:        
        try:
            # Request user data
            price = float(input("enter product price: "))
            if price <=0:
                print("ERRO: Enter a valid value")
                continue
        
            break
        except ValueError:
            print("Enter a valid value")
            continue
        

    # quantity validation
    counter_quantity=1
    while counter_quantity ==1:  
        try:
            # Request user data
            quantity = int(input("enter product quantity: "))
            if quantity <=0:
                print("ERRO: Enter a valid value")
                continue
            break
        except ValueError:
            print("Enter a valid value")
            continue

    #data storage library
    buys = {
           "product" :name,
           "price"   :price,
           "quantity":quantity 
        }

    return buys