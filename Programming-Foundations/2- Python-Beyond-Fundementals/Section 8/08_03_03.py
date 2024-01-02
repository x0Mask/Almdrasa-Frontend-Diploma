from Personal_Modules.screwdriverscript import screwDriver

slottedScrewdriver = screwDriver("Red", "Slotted", 15, True, False)
slottedScrewdriver.rotates()
slottedScrewdriver.testsElectricity()

triWingScrewdriver = screwDriver("Black", "Tri_Wing", 10, False, True)
triWingScrewdriver.rotates()
triWingScrewdriver.testsElectricity()

phillipsScrewdriver = screwDriver("Green", "Phillips", 20, True, True)
phillipsScrewdriver.rotates()
phillipsScrewdriver.testsElectricity()