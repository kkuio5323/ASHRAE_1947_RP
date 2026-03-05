import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import copy
from matplotlib import dates
from matplotlib.dates import DayLocator, HourLocator,DateFormatter
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
from eppy import modeleditor
from eppy.modeleditor import IDF
import sys



#%% data path

pathnameto_eppy = '../'
sys.path.append(pathnameto_eppy)

##### Windows OS
iddfile = "C:/EnergyPlusV25-1-0/Energy+.idd"
office1 = "../Building_models/Model_test/mid_office/ASHRAE901_OfficeMedium_STD2022/"
filename = "ASHRAE901_OfficeMedium_STD2022_NewYork.idf"

##### mac OS
# iddfile = "/Applications/EnergyPlus-25-1-0/Energy+.idd"
# office1 = "../Building_models/Model_test/mid_office/ASHRAE901_OfficeMedium_STD2022/"
# filename = "ASHRAE901_OfficeMedium_STD2022_NewYork.idf"
IDF.setiddname(iddfile)
idf1 = IDF(office1 + filename)

newpath = "../Building_models/New_model1/"

#%%

#put this measure in the loop

def measure1(idf1, newpath):
    floors = 3
    location = idf1.idfobjects['Site:Location'][0].Name[:20]
    
    coil_elc = "Coil:Heating:Electric"
    coil_gas = 'Coil:Heating:Fuel'
    gas = idf1.idfobjects[coil_gas]
    elec = idf1.idfobjects[coil_elc]

    heating_gas = gas[0]
    heating_elec = elec[0]

    # check field names
    gasfields=heating_gas.fieldnames[1:]
    elecfields=heating_elec.fieldnames[1:]
    
    l = 1   
    for i in range(floors):
        globals()['new_e' + 
                  str(l)] = pd.DataFrame(index=elecfields, columns=['value'])
        globals()['new_e' + 
                  str(l)].loc[elecfields[0], 'value'] = gas[i].Name
        globals()['new_e' + 
                  str(l)].loc[elecfields[1], 'value'] = gas[i].Availability_Schedule_Name
        globals()['new_e' + 
                  str(l)].loc[elecfields[2], 'value'] = elec[i].Efficiency
        globals()['new_e' + 
                  str(l)].loc[elecfields[3], 'value'] = gas[i].Nominal_Capacity
        globals()['new_e' + 
                  str(l)].loc[elecfields[4], 'value'] = gas[i].Air_Inlet_Node_Name
        globals()['new_e' + 
                  str(l)].loc[elecfields[5], 'value'] = gas[i].Air_Outlet_Node_Name   
        globals()['new_e' + 
                  str(l)].loc[elecfields[6], 'value'] = gas[i].Temperature_Setpoint_Node_Name   
        l = l+1
        
    
    idf1.newidfobject(coil_elc)    
    elec[-1].Name = new_e3.loc['Name', 'value']
    elec[-1].Availability_Schedule_Name = new_e3.loc['Availability_Schedule_Name', 'value']
    elec[-1].Efficiency = new_e3.loc['Efficiency', 'value']
    elec[-1].Nominal_Capacity = new_e3.loc['Nominal_Capacity', 'value']
    elec[-1].Air_Inlet_Node_Name = new_e3.loc['Air_Inlet_Node_Name', 'value']
    elec[-1].Air_Outlet_Node_Name = new_e3.loc['Air_Outlet_Node_Name', 'value']
    elec[-1].Temperature_Setpoint_Node_Name = new_e3.loc['Temperature_Setpoint_Node_Name', 'value']


    idf1.newidfobject(coil_elc)    
    elec[-1].Name = new_e2.loc['Name', 'value']
    elec[-1].Availability_Schedule_Name = new_e2.loc['Availability_Schedule_Name', 'value']
    elec[-1].Efficiency = new_e2.loc['Efficiency', 'value']
    elec[-1].Nominal_Capacity = new_e2.loc['Nominal_Capacity', 'value']
    elec[-1].Air_Inlet_Node_Name = new_e2.loc['Air_Inlet_Node_Name', 'value']
    elec[-1].Air_Outlet_Node_Name = new_e2.loc['Air_Outlet_Node_Name', 'value']
    elec[-1].Temperature_Setpoint_Node_Name = new_e2.loc['Temperature_Setpoint_Node_Name', 'value']


    idf1.newidfobject(coil_elc)    
    elec[-1].Name = new_e1.loc['Name', 'value']
    elec[-1].Availability_Schedule_Name = new_e1.loc['Availability_Schedule_Name', 'value']
    elec[-1].Efficiency = new_e1.loc['Efficiency', 'value']
    elec[-1].Nominal_Capacity = new_e1.loc['Nominal_Capacity', 'value']
    elec[-1].Air_Inlet_Node_Name = new_e1.loc['Air_Inlet_Node_Name', 'value']
    elec[-1].Air_Outlet_Node_Name = new_e1.loc['Air_Outlet_Node_Name', 'value']
    elec[-1].Temperature_Setpoint_Node_Name = new_e2.loc['Temperature_Setpoint_Node_Name', 'value']

    gas.clear()
    
    b = 'Branch'
    branch = idf1.idfobjects[b]
    for a in range(floors):
        branch[a].Component_3_Object_Type = coil_elc
    
    
    idf1.saveas(newpath + "m1_" + location + '.idf')
    return print("check the new file")
    
#%% test
 
# measure1(idf1, newpath)
    
