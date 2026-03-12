import math
def calculate_summary(sale,total):
    print()
    print("DAILY SALES SUMMARY")
    for x in sale:
        print("product: ",x["product"])
        print("Total quantity sold: ",x["amount"])
        print( )
    print()
    print("Total raised: ",math.trunc(total))
    print()
    