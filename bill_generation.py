from datetime import datetime
import random

print("\n    \t\t   Indraprastha   ")
print("")
GSTIN = "29AAEF12030E12"
print("     \n  Menu  \n")
print("1. Chicken Biryani", "\t\t 2. Dosa ", "\n\n3. Veg Biryani ", "\t\t4. Idli")
bill_no = random.randrange(1, 500)
I_price = 0
itm = []
amount = 0

s = True
while s:
    itm_choice = int(input("\nEnter Your Choice :  "))
    if itm_choice == 1:
        num_plate = int(input("Enter the quantity for Chicken Biryani: "))
        C_b_price=250
        itm.append(["Chicken Biryani", C_b_price,num_plate])
    elif itm_choice == 2:
        num_plate = int(input("Enter the quantity for Dosa: "))
        D_price = 30
        itm.append(["Dosa           ", D_price,num_plate])
    elif itm_choice == 3:
        num_plate = int(input("Enter the quantity for Veg Biryani: "))
        V_B_price = 100
        itm.append(["Veg Biryani    ", V_B_price,num_plate])
    elif itm_choice == 4:
        num_plate = int(input("Enter the quantity for Idli: "))
        I_price = 30
        itm.append(["Idli           ", I_price,num_plate])
    else:
        print('Sorry Input  ')
        break
    esl = input('Do you want something else (y/n): ')
    if esl != "y":
        s=False


if len(itm):
    print("")
    print("\t\tCASH BILL")
    print("")
    print("GST No : ", GSTIN)
    print("\nBill No:", bill_no, "\t\t\t Bill Date :", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("")
    print("Item Name ", "\t\t Qty ", "\t\tRate", "\t\t  Amount")
    print("")

    total_amount = 0
    for item, price,qty1 in itm:
        item_amount = qty1 * price
        total_amount += item_amount
        print(item ,"   ",qty1,"\t\t ",price,"\t\t " ,item_amount)

    print("--------------------------------------------------------------------")
    CGST = (6 / 100) * total_amount
    SGST = (6 / 100) * total_amount
    print("CGST 6% \t\t\t\t\t\t:        ",format(CGST,'.2f'))
    print("SGST 6% \t\t\t\t\t\t:        ",format( SGST,'.2f'))
    print("")
    print("Total Amount \t\t\t\t\t:\t     ", (total_amount + CGST + SGST)//2)
    print("")