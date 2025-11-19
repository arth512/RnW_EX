print("Welcome to the Bill Splitter App!")

bill=float(input("Enter total bill amount:"))
peopli=int(input("Enter number of people:"))
tip=int(input("Enter tip percentage (0/5/10/15/20):"))


tip_amount=bill*(tip/100)
total=bill+tip_amount
peopli_pay=tip_amount/peopli

print(f"\nTip Amount: ₹{tip_amount}")
print(f"Total Bill (with Tip): ₹{total}")
print(f"Each person should pay: ₹{peopli_pay}")

YN=input("Would you like to calculate another bill? (y/n): ")
    


