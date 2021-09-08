# -*- coding: utf-8 -*-
import numpy as np
import math

"""
Created on Tue Sep  7 09:24:56 2021
"""

Triton_x_100 = {"cmc": 0.2,"cmcUnit":"miliMolarity","molarMass":647,"cmcSource":"https://www.sigmaaldrich.com/US/en/product/sial/x100"}
IGEPal = {"cmc":0.08,"cmcUnit":"miliMolarity","molarMass":617,"cmcSource":"https://www.sigmaaldrich.com/US/en/product/sigma/i8896"}
Polyoxyethylene_10_Tridecyl_Ether = {"cmc":0.125,"cmcUnit":"miliMolarity","molarMass":244,"cmcSource":"https://www.researchgate.net/publication/267043941_Cellular_localization_and_detergent_dependent_oligomerization_of_rice_allene_oxide_synthase-1"}

print(Triton_x_100["cmc"])

def cmcConvert(placehold):
    output=placehold["cmc"]*placehold["molarMass"]/1000
    output="{:.5f}".format(output)
    print("Concentration is ",output,"g/L.")
    return
