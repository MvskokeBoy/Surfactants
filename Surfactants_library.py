# -*- coding: utf-8 -*-
import numpy as np
import math

"""
Created on Tue Sep  7 09:24:56 2021
"""

Triton_x_100 = {"cmc": 0.2,"cmcUnit":"miliMolarity","molarMass":647,"cmcSource":"https://www.sigmaaldrich.com/US/en/product/sial/x100"}
IGEPal = {"cmc":0.08,"cmcUnit":"miliMolarity","molarMass":617,"cmcSource":"https://www.sigmaaldrich.com/US/en/product/sigma/i8896"}
Polyoxyethylene_10_Tridecyl_Ether = {"cmc":0.125,"cmcUnit":"miliMolarity","molarMass":244,"cmcSource":"https://www.researchgate.net/publication/267043941_Cellular_localization_and_detergent_dependent_oligomerization_of_rice_allene_oxide_synthase-1"}
Pluronic_F_68={"cmc":.04,"cmcUnit":"miliMolarity","molarMass":8350,"cmcSource":"https://www.sigmaaldrich.com/US/en/product/sigma/p1300" }
Turgiton_NP_10={"cmc":55, "cmcUnit":"ppm","molarMass":682,"cmsSource":"https://www.sigmaaldrich.com/US/en/product/sigma/np10?context=product"}


print(Pluronic_F_68["cmc"])

def cmcConvert(placehold):
    if placehold["cmcUnit"]=="ppm":
        placehold["cmc"]=placehold["cmc"]/placehold["molarMass"]
    output=placehold["cmc"]*placehold["molarMass"]/1000
    output="{:.5f}".format(output)
    print("Concentration is ",output,"g/L.")
    return


print(cmcConvert(Triton_x_100))
