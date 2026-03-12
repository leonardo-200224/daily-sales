def calculate_summary(sale):
    print()
    print("DAILY SALES SUMMARY")
    for x in sale:
        print("product: ",x["product"])
        print("Total quantity sold: ",x["amount"])
        print( )