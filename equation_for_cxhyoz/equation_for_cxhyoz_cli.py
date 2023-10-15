# function to prevent a non negative number being entered
def non_negative(x):
    if(x < 0):
        print("Please enter a non negative value")

print()
# carbon in reactant
c = float(input("Enter the number of of carbon atoms in the hydrocarbon: "))
non_negative(c)
# hydrogen in reactant
h = float(input("Enter the number of of hydrogen atoms in the hydrocarbon: "))
non_negative(h)
# oxygen in reactant
o = float(input("Enter the number of of oxygen atoms in the hydrocarbon: "))
non_negative(o)

# products
carbondioxide = float(c)
water = float(h/2)

# oxyen in reactant
oxygen = float(water+2*carbondioxide-o)/2

# function to check if the number is not a decimal. If it is not a decimal then the datatype is reassigned as integer
def is_int(x):
    if(x.is_integer()):
     x = int(x)

# checks for reactants and products
is_int(c)
is_int(h)
is_int(o)
is_int(carbondioxide)
is_int(oxygen)
is_int(water)

# final reaction
print()
print(f"The reaction is C_{c} H_{h} O_{o}  +  {oxygen} O_2  -->  {carbondioxide} CO_2 + {water} H_2O")

# atomic weight of the elements
mol_c = float(12)
mol_o = float(16)
mol_h = float(1)

# molecular weight of the constituents
w_c = float(c*mol_c)
w_o = float(o*mol_o)
w_h = float (h*mol_h)
w_carbondioxide = float((mol_c+2*mol_o)*carbondioxide)
w_oxygen = float(2*mol_o*oxygen)
w_water = float((2*mol_h+mol_o)*water)
w_hydrocarbon = float(w_c+w_h+w_o)

# weight of oxygen in products
o_in_carbondioxide = float(c*2)
o_in_water = float(water)
total_o_in_products = float(o_in_carbondioxide+o_in_water)

# percentage of oxygen products
percent_o_in_carbondioxide = float(o_in_carbondioxide/total_o_in_products)
percent_o_in_water = float(o_in_water/total_o_in_products)

# percent lost
lost_c = float((w_c+w_o*percent_o_in_carbondioxide)*100/w_hydrocarbon)
lost_o = float(100-lost_c)

# final percent
print()
print("The percentage of oxygen lost as CO_2 is: %.3f" % lost_c)
print("The percentage of oxygen lost as H_2O is: %.3f" % lost_o)
print()
