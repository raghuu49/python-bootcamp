print("Welcome to the tip calculator!!")
total_bill=float(input("What was your bill?$"))
tip_percentage=float(input("what is the tip percentage?"))
total_bill_including_tip=total_bill+ tip_percentage/100 * total_bill
num_people=int(input("number of total people?"))
share_per_person=round(total_bill_including_tip/num_people,2)
print(f"Each person should pay: {share_per_person}")