import math
def calculate_summary(sale,total):
    print()
    print("DAILY SALES SUMMARY\n")
    for x in sale:
        print("product: ",x["product"])
        print("Total quantity sold: ",x["quantity"])
        print( )
    print()
    print("Total raised: ",math.trunc(total))
    print()
    