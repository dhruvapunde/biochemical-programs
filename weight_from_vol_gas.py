"""
This program uses the Ideal Gas Law to find grams of a gas from a particular volume at a given temperature and pressure
Ideal Gas Law: PV = nRT
"""

print()
volume = float(input("Enter the volume of gas in litres: "))
temperature_in_celsius = float(input("Enter the temperature in celsius: "))
pressure = float(input("Enter pressure in atm: "))

R = 0.082 # Regnault's constant

temperature_in_kelvin = temperature_in_celsius+273.15

number_of_moles = (pressure*volume)/(R*temperature_in_kelvin) # n = PV/RT

molecular_weight = float(input("Enter the molecular weight of the gas: "))

weight = number_of_moles*molecular_weight # moles times molecular weight

print(f"The weight of the gas in grams is: {weight}, at {temperature_in_celsius}C and {pressure} atm pressure")
