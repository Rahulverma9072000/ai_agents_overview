# Delivery Fees Waiver System 
order_amount  = int(input("Enter the Order Amount : "))
print(f"Order Amount : {type(order_amount)}")

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery Fees is : {delivery_fees}")