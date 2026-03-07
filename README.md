# ASHRAE_1947_RP
## Problems
1. **Problem 1**: Stochastic future weather, considering extremely hot (e.g., heat waves) and cold (e.g., cold snaps) weather events, and energy analysis of heat pump technologies have yet to be systematically analyzed across the U.S.
2. **Problem 2**: An easy-to-understand tool to store and visualize building resilience across the U.S. is lacking, which is useful for making understanding issues pertinent to the HVAC&R sector accessible.
3. **Problem 3**: Building standards need to be updated to enhance future building resilience to climate change with extremely hot and cold weather events.
## Objectives
1. Systematize the process of running building energy models with a wide range of future weather files.
2. Create an easy-to-understand way to store and visualize the simulation results for building resilience.
3. Support the improvement of ASHRAE Standards to guide the enhancement of future building resilience against climate change with extreme weather events.
## Task 1. Reconfigure Building Energy Models
### Task Description
This task will reconfigure building energy models based on DOE Prototype Building Models. Two building types with the newest building energy code versions will be selected as the starting point: (1) ***2021 IECC single-family detached houses*** and (2) ***ASHRAE 90.1-2022 medium offices***.
### Measures
Five measures will be created to automatically change the HVAC and hot water systems in the DOE Prototype Building Models to new models with the required systems for the six scenarios. All the measures will be written using Python, and Python packages, such as eppy, will be used in these measures5. The descriptions of these measures and how to use my previous research experience to support this work are summarized as follows:
- **Measure 1**: This measure aims to replace the heating system in a building model (IDF) with electric element heating. The method for automatically creating HVAC systems in OpenStudio Standards/UrbanBEM will be leveraged to develop this measure.
- **Measure 2**: This measure aims to study the impact of power outages on building resilience. All electric equipment, including HVAC systems, will periodically turn on and off to mimic the reactions of buildings during rolling blackouts during extreme weather events. The power outage periods will be an input, which means the power off and on periods are adjustable. New Energy Management System (EMS) objects will be added to modify/rewrite schedules in a building model (IDF). The method for automatically creating HVAC systems in Tri-Lab Resilience will be leveraged to develop this measure.
- **Measure 3**: This measure aims to replace the HVAC and hot water systems in a building model (IDF) with unintegrated air-source heat pumps (ASHP). The method for automatically creating HVAC systems in OpenStudio Standards/UrbanBEM will be leveraged to develop this measure.
- **Measure 4**: This measure aims to replace the HVAC and hot water systems in a building model with high-efficiency ground-source heat pumps (GSHP). The team proposes writing a Python measure using the eppy package to implement EnergyPlus objects (e.g., HeatPump:WaterToWater:EquationFit and HeatPump:WaterToWater:ParameterEstimation) into a building model (IDF). EnergyPlus example files will be referred to create this measure.
- **Measure 5**: This measure aims to replace the HVAC and hot water systems in a building model with high-efficiency integrated ASHP. The team proposes writing a Python measure using the eppy package to implement EnergyPlus objects (e.g., CoilSystem:IntegratedHeatPump:AirSource) into a building model (IDF). EnergyPlus example files will be referred to create this measure.
### New Models
Using the DOE Prototype Building Models and the five measures, the UA team will create six categories of new models:
- **New Model 1**: The DOE Prototype Building Models of single-family detached houses with electric resistance will be used as the single residential dwelling baseline with electric element heating. Measure 1 will change the heating systems in the DOE Prototype Building Models of medium offices to electric element heating. The new model will be used as the commercial medium office baseline with electric element heating.
- **New Model 2**: The DOE Prototype Building Models of single-family detached houses with gas furnaces and medium offices will be used as the baselines with natural gas heating.
- **New Model 3**: Measure 2 will add system controls for power outages to New Model 1 (single-family detached houses and medium offices). The new models will be used as baselines with power outages.
- **New Models 4-6**: Measures 3-5 will change HVAC and hot water systems in the models (DOE Prototype Building Models of single-family detached houses and medium offices) and create New Models 4-6, respectively.
### Deliverables
1. A set of building energy models with all configurations.
2. A set of measures to automatically generate required building energy models based on the DOE Prototype Building Models.
