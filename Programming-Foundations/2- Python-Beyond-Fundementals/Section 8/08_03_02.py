from Personal_Modules.screwdriver import Screwdriver

# Create a slotted screwdriver object
slotted_screwdriver = Screwdriver("Black", 10, "Slotted", False, True)
# Rotate the slotted screwdriver
slotted_screwdriver.rotates()
# Test electricity with the slotted screwdriver
slotted_screwdriver.testsElectricity()

# Create a tri-wing screwdriver object
tri_wing_screwdriver = Screwdriver("Yellow", 15, "Tri-wing", True, False)
# Rotate the tri-wing screwdriver
tri_wing_screwdriver.rotates()
# Test electricity with the tri-wing screwdriver
tri_wing_screwdriver.testsElectricity()

# Create a Philips screwdriver object
philips_screwdriver = Screwdriver("Red", 36, "Philips", True, False)
# Rotate the Philips screwdriver
philips_screwdriver.rotates()
# Test electricity with the Philips screwdriver
philips_screwdriver.testsElectricity()