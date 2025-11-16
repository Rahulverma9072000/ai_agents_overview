# Everything is object in python 
# Evety object have unique identity , type 

# Mutable : that is changeable 
# Immutable : that is not changeable 

sugar_amount  = 2
print("Current Id ",id(sugar_amount))
print(f"Initial Sugar : {sugar_amount}")
sugar_amount = 12
print(f"Second Sugar : {sugar_amount}")
print("Second Id ",id(sugar_amount))
# What happend behind the scene , we point to new memory location that have 12 , so we are changing the reference 
# To Proove it track on the basis of identity not the value 

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}");