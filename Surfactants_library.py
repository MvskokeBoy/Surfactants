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
Polysorbate_80= {"cmc":0.012,"cmcUnit":"miliMolarity","molarMass":1310,"cmcSource":"https://www.sigmaaldrich.com/US/en/product/sial/p1754"}
Tween_80= {"cmc":0.019,"cmcUnit":"miliMolarity","molarMass":428.62,"cmcSource":"https://www.sciencedirect.com/science/article/pii/S2468023019305486"}
Cocamidopropyl_Betaine= {"cmc":29,"cmcUnit":"ppm","molarMass":342.5,"cmcSource":"https://www.sciencedirect.com/science/article/pii/B9780128127056000149"}
PEG_60_Caster_Oil= {"cmc":30,"cmcUnit":"ppm","molarMass":1119.6,"cmcSource":"calculated from manufacturer"}


print(Pluronic_F_68["cmc"])

def cmcConvert(placehold):
    if placehold["cmcUnit"]=="ppm":
        placehold["cmc"]=placehold["cmc"]/placehold["molarMass"]
        #1ppm=1mg/l
    output=placehold["cmc"]*placehold["molarMass"]/1000
    output="{:.5f}".format(output)
    print("Concentration is ",output,"g/L.")
    return


print(cmcConvert(Triton_x_100))
