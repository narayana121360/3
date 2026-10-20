#!/usr/bin/env python
# coding: utf-8

# In[1]:


import CoolProp.CoolProp as CP


# To to find compostion of flue gas when 1 kg of fuel is utilized

class composition:
    def __init__(self, fuel, power, t, p, u_ratio, stream_carbon_ratio, excess_air):
        self.fuel = fuel
        self.u_ratio = u_ratio
        self.stream_carbon_ratio = stream_carbon_ratio
        self.excess_air = excess_air
        self.power = power
        self.t = t
        self.p = p
        self.mass_flow = None
        self.mf_nitrogen = None
        self.mf_oxygen = None
        self.water = None
        self.co2 = None


    def calc(self):
        if self.fuel == "methane" or "Methane" or "METHANE":
            if __name__ == "__main__":
                print("Methane is selcted as Fuel Cell Fuel")
                print("Excess Air: ", self.excess_air)
                print("The H2O/C Ratio is", self.stream_carbon_ratio)
                print("The Fuel Cell Utilization Ratio is", self.u_ratio)
            O2, H2O, CO2, s_c_ratio_conversion = [3.989178946318598, 2.245902211584013, 2.743274241404244, 1.122951105792006]
            s_c_mass_ratio = self.stream_carbon_ratio * s_c_ratio_conversion
            stoich_air_requirement = O2 * (self.u_ratio/100)/0.23057397
            air_requirement = stoich_air_requirement * (1+(self.excess_air/100))
            nitrogen_in_flue = air_requirement * 0.76165843
            co2_in_flue = CO2
            oxygen_in_flue = (air_requirement * 0.23057397) - O2
            water_in_flue = (air_requirement * 0.0077676014) + H2O + s_c_mass_ratio
            if __name__ == "__main__":
                print("The Total Air Requirement is", air_requirement)
                print(nitrogen_in_flue)
                print(co2_in_flue)
                print(oxygen_in_flue)
                print(water_in_flue)
                print(s_c_mass_ratio)
            total = nitrogen_in_flue + co2_in_flue + oxygen_in_flue + water_in_flue
            moles_nitrogen = 1000 * nitrogen_in_flue / 28.0134
            moles_co2 = 1000 * co2_in_flue / 44.0098
            moles_oxygen = 1000 * oxygen_in_flue / 31.99886
            moles_water = 1000 * water_in_flue / 18.01528
            total_moles = moles_nitrogen + moles_co2 + moles_oxygen + moles_water
            if __name__ == "__main__":
                print('Total flue mass =', total)
                print('Total flue moles =', total_moles)
            mf_nitrogen = moles_nitrogen/total_moles
            mf_co2 = moles_co2/total_moles
            mf_oxygen = moles_oxygen/total_moles
            mf_water = moles_water/total_moles
            flue = ['Nitrogen', 'Oxygen', 'Water', 'CO2']
            flue_mole_fractions = [mf_nitrogen, mf_oxygen, mf_water, mf_co2]
            test2 = CP.PropsSI('H', 'P', self.p, 'T', self.t, 'HEOS::Methane-PengRobinson[1]')
            if __name__ == "__main__":
                print(flue)
                print(flue_mole_fractions)
                print(mf_water)
                print(mf_oxygen)
                print(mf_co2)
                print(mf_co2)
                print(mf_co2)
                print(mf_nitrogen)
                print(test2)
            flue_string = f'HEOS::Nitrogen[{mf_nitrogen}]&Oxygen[{mf_oxygen}]&Water[{mf_water}]&CO2[{mf_co2}]'

            total_moles_noh2o = moles_nitrogen + moles_co2 + moles_oxygen
            mf_nitrogen_noh2o = moles_nitrogen/total_moles_noh2o
            mf_co2_noh2o = moles_co2/total_moles_noh2o
            mf_oxygen_noh2o = moles_oxygen/total_moles_noh2o
            flue_noh2o = ['Nitrogen', 'Oxygen', 'CO2']
            flue_mole_fractions_noh2o = [mf_nitrogen, mf_oxygen, mf_co2]
            flue_string_noh2o = f'Nitrogen[{mf_nitrogen_noh2o}]&Oxygen[{mf_oxygen_noh2o}]&CO2[{mf_co2_noh2o}]'


            h_noh2o = CP.PropsSI('H','T',25+273.15,'P',101325, flue_string_noh2o)
            h_h2o = CP.PropsSI('H','T',25+273.15,'P',101325, "Water")
            mass_fraction_h2o = water_in_flue/total
            mass_fraction_noh2o = 1- mass_fraction_h2o
            h = (h_noh2o*mass_fraction_noh2o)+(h_h2o*mass_fraction_h2o)

    










            
            test1 = CP.PropsSI('H','T|gas',self.t,'P', self.p, flue_string)
            test3 = CP.PropsSI('H','T|supercritical_gas',650+273.15,'P',200000, flue_string)
            test2 = CP.PropsSI('H','T',25+273.15,'P',101325, flue_string)
            heat = (test1 -h)/1000
            heat2 = (test3 -test2)/1000
            self.mass_flow = self.power/heat

            self.mf_nitrogen = mf_nitrogen
            self.mf_oxygen = mf_oxygen
            self.mf_water = mf_water
            self.mf_co2 = mf_co2
            
            
            return(flue_mole_fractions, self.mass_flow)







