# Dictionary in Python 
chai_order = dict(type = "Masala Chai" , size = "large" , sugar = 2)
print(chai_order)
chai_recipe = {}
chai_recipe["base"] = "black Tea"
chai_recipe["liquid"] = "milk"
print(f"Reciepes Base : {chai_recipe["base"]}")
print(f"Reciepes : {chai_recipe}")
del chai_recipe["liquid"]
print(f"Reciepes : {chai_recipe}")

print(f"Is Sugar in the Order ? {'sugar' in chai_order}")

chai_order = {"type" : "Ginger Chai", "size" : "Medium" , "sugar" : 1 }
print(f"Order Details (keys) : {chai_order.keys()}")
print(f"Order Details (values) : {chai_order.values()}")
print(f"Order Details (Items) : {chai_order.items()}")


last_item = chai_order.popitem()
print(f"Removed Last item : {last_item}")

extra_spices = {"cardamom" : "crushed" , "ginger" : "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated Chai Recipe : {chai_recipe}")

# If note is not present in dictionary than No Note will appear 
customer_note = chai_order.get("note","No Note")
print(f"Customer_note is : {customer_note}")
