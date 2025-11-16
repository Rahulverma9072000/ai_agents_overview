# Tuples 
# Fiexed Ingredents : cannot be changes 
masala_spices  = ("cardmom","cloves","cinnamon")

#Extract Values from tuples 
(spice1 , spice2 , spice3) = masala_spices

print(f"Main Masala Spices : {spice1} , {spice2} , {spice3}")

ginger_ratio , cadramom_ratio = 2,1
print(f"Ratio is G : {ginger_ratio} and C : {cadramom_ratio}")
# Swap the Variable like this without 3rd variable 
ginger_ratio , cadramom_ratio = cadramom_ratio , ginger_ratio
print(f"Ratio is G : {ginger_ratio} and C : {cadramom_ratio}")

#Membership 
print(f"Is Ginger in Masala Spices ? {'ginger' in masala_spices}")
print(f"Is cinnamon in Masala Spices ? {'cinnamon' in masala_spices}")
