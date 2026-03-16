from sales_register import register_sale
from sales_summary import calculate_summary
from sales_totals import calculate_total
total =[]
counter=1
while counter==1:
    print("\nSales menu\n")
    buys = register_sale()
    total.append(buys)
    
    try:
        end= int(input("1- finish\n"
                      "2- enter new sale"))
        if end == 1:
            counter =2
            x= calculate_total(total)
            calculate_summary(total,x)
        elif end >2 or end <1:
            print("\nEnter valid value 1 or 2.")
            
    except ValueError:
        print("\nEnter valid value 1 or 2.")
    