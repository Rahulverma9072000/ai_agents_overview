# Basics of List in Python 

    # Mutable 
        # List 
        # Array 
ingredients = ['water','milk','black tea']
ingredients.append('sugar')
print(ingredients)
ingredients.remove('water')
print(ingredients)

spice_options = ["ginger","cardamom"]
chai_ingredients = ["Water","Milk"]

chai_ingredients.extend(spice_options)
chai_ingredients.insert(2,"black_tea")
print(chai_ingredients)
last_added = chai_ingredients.pop()
print(chai_ingredients)
reverse_chai_ingredients = list(reversed(chai_ingredients))
print(reverse_chai_ingredients)

sugar_levels = [1,2,3,4,5]
print(f"Maximum Sugar Level : {max(sugar_levels)}")
print(f"Minimum Sugar Level : {min(sugar_levels)}")

base_liquid = ["Water","Milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix : {full_liquid_mix}")
strong_brew = ["black tea","Water"] * 3
print(f"Strong Brew : {strong_brew}")


raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes : {raw_spice_data}")