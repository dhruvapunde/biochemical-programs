import math

# the variables c, h and o are the molecules in the hydrocarbon
class Reaction:
    def __init__(self,c,h,o):
        self.c = c
        self.h = h
        self.o = o
    
    def balanced_reaction(self):
        c = self.c
        h = self.h
        o = self.o

        # products
        carbondioxide = float(c)
        water = float(h/2)

        # oxyen in reactant
        oxygen = float(water+2*carbondioxide-o)/2

        # condition to check if the number is not a decimal. If it is not a decimal then the datatype is reassigned as integer
        if(c.is_integer):
            c = int(c)
        if(h.is_integer):
            h = int(h)
        if(o.is_integer):
            o = int(o)
        if(carbondioxide.is_integer):
            carbondioxide = int(carbondioxide)
        if(oxygen.is_integer):
            oxygen = int(oxygen)
        if(water.is_integer):
            water = int(water)

        # final reaction
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
        w_hydrocarbon = float((mol_c*c)+(mol_h*h)+(mol_o*o))

        # weight of oxygen in products
        o_in_carbondioxide = float(c*2)
        o_in_water = float(water)
        total_o_in_products = float(o_in_carbondioxide+o_in_water)

        # percentage of oxygen products
        percent_o_in_carbondioxide = float(o_in_carbondioxide/total_o_in_products)
        percent_o_in_water = float(o_in_water/total_o_in_products)

        # percent lost
        lost_c = float(((c*mol_c)+(o*mol_o)*percent_o_in_carbondioxide)*100/w_hydrocarbon)
        lost_o = float(100-lost_c)

        # final percent
        print()
        print("The percentage of oxygen lost as CO_2 is: %.3f" % lost_c)
        print("The percentage of oxygen lost as H_2O is: %.3f" % lost_o)
        print()
        
        return {
            "carbondioxide": carbondioxide,
            "oxygen": oxygen,
            "water": water,
            "lost_to_water": round(lost_o,4),
            "lost_to_CO2": round(lost_c,4),
        }
