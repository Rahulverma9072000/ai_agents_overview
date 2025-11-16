# Strings 
    # Immutable can not be changed 

chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} Please !")

chai_description = "Aromatic and Bold"
# last number is not inclusive 
print(f"First Word : {chai_description[0:8:1]}")
print(f"Last Word : {chai_description[12::1]}") #Skip the last index 
print(f"Reverse Word : {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"Encoded Label : {encoded_label}")
print(f"Non Encoded Label : {label_text}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")
