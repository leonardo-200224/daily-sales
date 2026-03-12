def calculate_total(sale):
    total =0
    for x in sale:
        total += x["price"] 
    return total