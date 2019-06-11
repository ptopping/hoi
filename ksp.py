import pandas as pd
import numpy as np
from math import sqrt
from math import pi

class PART(object):
    """docstring for PART"""
    def __init__(self, **kwargs):
        self.attributes = kwargs
        self.modules = {}
        self.resources = {}
        self.models = {}

    def addMODULE(self, mod):
        self.modules.update(mod.__dict__)

    def addRESOURCE(self,resource):
        self.resources.update(resource.__dict__)

    def addMODEL(self,model):
        self.models.update(model.__dict__)

class MODULE(object):
    """docstring for MODULE"""
    def __init__(self, **kwargs):
        self.attributes = kwargs
        self.variants = {}
        self.fxlooks = {}

    def addVARIANT(self, var):
        self.variants.update(var.__dict__)

    def addCONSTRAINLOOKFX(self, looks):
        self.fxlooks.update(looks.__dict__)
        
class VARIANT(object):
    """docstring for VARIANT"""
    def __init__(self, **kwargs):
        self.attributes = kwargs
        self.textures = {}
    
    def addTEXTURE(self, txt):
        self.textures.update(txt.__dict__)

class TEXTURE(object):
    """docstring for TEXTURE"""
    def __init__(self, **kwargs):
        self.attributes = kwargs

class CONSTRAINLOOKFX(object):
    """docstring for CONSTRAINLOOKFX"""
    def __init__(self, **kwargs):
        self.attributes = kwargs

class RESOURCE(object):
    """docstring for RESOURCE"""
    def __init__(self, **kwargs):
        self.attributes = kwargs                        

class MODEL(object):
    """docstring for MODEL"""
    def __init__(self, **kwargs):
        self.attributes = kwargs
                        
BlackAndWhite = VARIANT(name = 'BlackAndWhite', displayName = '#autoLOC_8007122', themeName = 'BlackAndWhite', primaryColor = '#ffffff', secondaryColor = '#000000')
BlackAndWhite.addTEXTURE(TEXTURE(mainTextureURL = 'Squad/Parts/Utility/rockomaxAdapters/Assets/Rockomax_Adapters_diffuse_O',
_BumpMap = 'Squad/Parts/Utility/rockomaxAdapters/Assets/Rockomax_Adapters_normal_O'))
Dark = VARIANT(name = 'Dark', displayName = '#autoLOC_8007117', themeName = 'Dark', primaryColor = '#4c4f47')
Dark.addTEXTURE(TEXTURE(mainTextureURL = 'Squad/Parts/Utility/rockomaxAdapters/Assets/Rockomax_Adapters_diffuse',
_BumpMap = 'Squad/Parts/Utility/rockomaxAdapters/Assets/Rockomax_Adapters_normal'))
White = VARIANT(name = 'White', displayName = '#autoLOC_8007119', themeName = 'White', primaryColor = '#ffffff', secondaryColor = '#ffffff')
White.addTEXTURE(TEXTURE(mainTextureURL = 'Squad/Parts/Utility/rockomaxAdapters/Assets/Rockomax_Adapters_diffuse_W',
_BumpMap = 'Squad/Parts/Utility/rockomaxAdapters/Assets/Rockomax_Adapters_normal'))
ModulePartVariants = MODULE(name = 'ModulePartVariants', baseVariant = 'BlackAndWhite', useMultipleDragCubes = False)
ModulePartVariants.addVARIANT(BlackAndWhite)
ModulePartVariants.addVARIANT(Dark)
ModulePartVariants.addVARIANT(White)
noseCone = PART(name = 'noseCone', module = 'Part', author = 'AlexanderM', mesh = 'aerodynamicNoseCone.mu', scale = 1.0, rescaleFactor = 1, 
node_stack_bottom01 = '0.0, 0.0, 0.0, 0.0, -1.0, 0.0', CenterOfDisplacement = '0.0, 0.2, 0.0', TechRequired = 'stability', entryCost = 2000, cost = 240, category = 'Aero', subcategory = 0,
title = 'Aerodynamic Nose Cone', manufacturer = 'Goliath National Products',
description = 'Aerodynamic, lightweight and mostly non-explosive. As a reminder to all personnel operating nearby, this part is really sharp and itd probably hurt if you fell on it.',
attachRules = '1,0,1,1,0', stackSymmetry = 2, mass = 0.03, dragModelType = 'default', maximum_drag = 0.1, minimum_drag = 0.1, angularDrag = 0.5, crashTolerance = 10, maxTemp = 2400,
emissiveConstant = 0.7, thermalMassModifier = 6.0, fuelCrossFeed = False, bulkheadProfiles = 'size1', tags = 'aero aircraft booster )cap drag fligh plane rocket speed stab stream')
noseCone.addMODULE(ModulePartVariants)

ModuleAeroSurface = MODULE(name = 'ModuleAeroSurface', useInternalDragModel = True, dragCoeff = 0.6, deflectionLiftCoeff = 0.38, ctrlSurfaceRange = 70, ctrlRangeFactor = 0.2,
ctrlSurfaceArea = 1, actuatorSpeed = 20, transformName = 'Flap', defaultActionGroup = 'Brakes', liftingSurfaceCurve = 'SpeedBrake', ignorePitch = True, ignoreYaw = True, uncasedTemp = 1200,
casedTemp = 2400)
FXModuleLookAtConstraint = MODULE(name = 'FXModuleLookAtConstraint')
FXModuleLookAtConstraint.addCONSTRAINLOOKFX(CONSTRAINLOOKFX(targetName = 'PistonArm', rotatorsName = 'PistonBase'))
FXModuleLookAtConstraint.addCONSTRAINLOOKFX(CONSTRAINLOOKFX(targetName = 'PistonBase', rotatorsName = 'PistonArm'))
airbrake1 = PART(name = 'airbrake1', module = 'Part', author = 'Porkjet', mesh = 'Airbrake.mu', rescaleFactor = 1, node_attach = '0.0, 0.0, -0.025, 0.0, 0.0, 1.0, 1',
CoMOffset = '0.0, -0.2, 0.2', CoPOffset = '0.0, -0.2, 0.2', CoLOffset = '0.0, -0.2, 0.2', TechRequired = 'advAerodynamics', entryCost = 20000, cost = 1000, category = 'Aero', subcategory = 0,
title = 'A.I.R.B.R.A.K.E.S', manufacturer = 'C7 Aerospace Division',
description = 'Research into feasible ways to slow down a plane in mid-air showed that loose hull panels are pretty great as drag-inducing deceleration devices. The discovery led to the invention of the Aerodynamically Integrated Retrograde Braking Robustly Armed Kinetic Extending System (A.I.R.B.R.A.K.E.S.), which is now popular mostly as a cheap alternative to longer runways. C7 Engineers are still trying to come up with a shorter name for such a long acronym.',
attachRules = '0,1,0,0,1', mass = 0.05, thermalMassModifier = 5.0, emissiveConstant = 0.4, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02, angularDrag = 2,
crashTolerance = 8, maxTemp = 2400, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf',
tags = '(air airbrake aircraft brake dive drag fligh landing plane slow speed spoil')
airbrake1.addMODULE(ModuleAeroSurface)
airbrake1.addMODULE(FXModuleLookAtConstraint)

ModuleResourceIntake = MODULE(name = 'ModuleResourceIntake', resourceName = 'IntakeAir', checkForOxygen = True, area = 0.0031, intakeSpeed = 15, intakeTransformName = 'Intake',
machCurve = {'key' : '1 1 0 0', 'key' : '1.5 0.9 -0.4312553 -0.4312553', 'key' : '2.5 0.45 -0.5275364 -0.5275364', 'key' : '3.5 0.1 0 0'})
IntakeAir = RESOURCE(name = 'IntakeAir', amount = 2, maxAmount = 2)
airScoop = PART(name = 'airScoop', module = 'Part', author = 'NovaSilisko, Porkjet', mesh = 'RadialIntake.mu', rescaleFactor = 1, node_attach = '0.0, 0.3370661, 0.0, 0.0, 1.0, 0.0',
buoyancy = 0.1, TechRequired = 'aerodynamicSystems', entryCost = 2500, cost = 250, category = 'Aero', subcategory = 0, title = 'XM-G50 Radial Air Intake',
manufacturer = 'Vac-Co Advanced Suction Systems',
description = 'An intake duct version that can be mounted at the sides of a fuselage. Warranty does not cover engine flame-outs or any objects, inanimate or otherwise, sucked in by the intake. Optimized for subsonic flight.',
attachRules = '0,1,0,0,0', mass = 0.02, thermalMassModifier = 6.0, heatConductivity = 0.06, dragModelType = 'default', maximum_drag = 0.2, minimum_drag = 0.2, angularDrag = 1,
crashTolerance = 10, breakingForce = 200, breakingTorque = 200, maxTemp = 2000, bulkheadProfiles = 'srf', tags = 'aero aircraft breathe fligh inlet jet oxygen plane subsonic suck')
airScoop.addMODULE(ModuleResourceIntake)
airScoop.addRESOURCE(IntakeAir)

ModuleControlSurface = MODULE(name = 'ModuleControlSurface', useInternalDragModel = True, dragCoeff = 0.5, deflectionLiftCoeff = 0.86, ctrlSurfaceRange = 15, ctrlSurfaceArea = 1,
actuatorSpeed = 25, transformName = 'ControlSurface')
airlinerCtrlSrf = PART(name = 'airlinerCtrlSrf', module = 'Part', author = 'Porkjet', rescaleFactor = 1, node_attach = '0.0, 0.0, 0.0, 1.0, 0.0, 0.0', CoMOffset = '0, -0.3730053, 0',
CoLOffset = '0, -0.3730053, 0', CoPOffset = '0, -0.3730053, 0', TechRequired = 'heavyAerodynamics', entryCost = 16400, cost = 800, category = 'Aero', subcategory = 0,
title = 'FAT-455 Aeroplane Control Surface', manufacturer = 'WinterOwl Aircraft Emporium', description = 'Large conventional control surface.', attachRules = '0,1,0,1,1', mass = 0.17,
thermalMassModifier = 6, heatConductivity = 0.12, emissiveConstant = 0.4, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02, angularDrag = 2, crashTolerance = 15,
maxTemp = 1200, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf', tags = 'aileron aircraft (elev flap fligh liner plane )rudder spoil stab')
airlinerCtrlSrf.addMODULE(ModuleControlSurface)
airlinerCtrlSrf.addMODEL(MODEL(model = 'Squad/Parts/Aero/airlinerWings/ControlSurface'))

ModuleLiftingSurface = MODULE(name = 'ModuleLiftingSurface', useInternalDragModel = True, deflectionLiftCoeff = 7.8, dragAtMaxAoA = 0.6, dragAtMinAoA = 0.0)
LiquidFuel = RESOURCE(name = 'LiquidFuel', amount = 0, maxAmount = 600)
airlinerMainWing = PART(name = 'airlinerMainWing', module = 'Part', author = 'Porkjet', rescaleFactor = 1, node_attach = '0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1', CoMOffset = '-2.5, 0.25, 0',
CoLOffset = '-2.5, 0.25, 0', CoPOffset = '-2.5, 0.25, 0', TechRequired = 'heavyAerodynamics', entryCost = 36400, cost = 2800, category = 'Aero', subcategory = 0,
title = 'FAT-455 Aeroplane Main Wing', manufacturer = 'WinterOwl Aircraft Emporium',
description = 'One of the largest lifting surfaces in production. The internal volume of these is big enough to carry generously sized fuel tanks.',
attachRules = '0,1,0,1,1', mass = 0.78, thermalMassModifier = 3, heatConductivity = 0.12, emissiveConstant = 0.4, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02,
angularDrag = 2, crashTolerance = 15, maxTemp = 1200, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf', 
tags = 'aero aircraft airlin fligh foil fuel ?lf lift liquid swept wet')
airlinerMainWing.addMODULE(ModuleLiftingSurface)
airlinerMainWing.addRESOURCE(LiquidFuel)
airlinerMainWing.addMODEL(MODEL(model = 'Squad/Parts/Aero/airlinerWings/MainWing')) 

ModuleControlSurface = MODULE(name = 'ModuleControlSurface', useInternalDragModel = True, dragCoeff = 0.6, deflectionLiftCoeff = 2.69, ctrlSurfaceRange = 15, ctrlSurfaceArea = 0.37,
actuatorSpeed = 25, transformName = 'ctrlSrf')
FlagDecal = MODULE(name = 'FlagDecal', textureQuadName = 'FLAG')
airlinerTailFin = PART(name = 'airlinerTailFin', module = 'Part', author = 'Porkjet', rescaleFactor = 1, node_attach = '0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1', CoLOffset = '-2.0, 0.4, 0',
CoPOffset = '-2.0, 0.4, 0', CoMOffset = '-2.0, 0.4, 0', TechRequired = 'heavyAerodynamics', entryCost = 4000, cost = 1000, category = 'Aero', subcategory = 0,
title = 'FAT-455 Aeroplane Tail Fin', manufacturer = 'WinterOwl Aircraft Emporium', description = 'Large conventional wing with built-in control surface.', attachRules = '0,1,0,1,1',
mass = 0.36, thermalMassModifier = 3.0, heatConductivity = 0.12, emissiveConstant = 0.4, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02, angularDrag = 2,
crashTolerance = 15, maxTemp = 1200, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf',
tags = 'aileron aircraft control (elev fligh foil lift liner )rudder stab swept wing')
airlinerTailFin.addMODULE(ModuleControlSurface)
airlinerTailFin.addMODULE(FlagDecal)
airlinerTailFin.addMODEL(MODEL(model = 'Squad/Parts/Aero/airlinerWings/TailFin'))

ModuleControlSurface = MODULE(name = 'ModuleControlSurface', useInternalDragModel = True, dragCoeff = 0.5, deflectionLiftCoeff = 0.4, ctrlSurfaceRange = 10, ctrlSurfaceArea = 1,
actuatorSpeed = 35, transformName = 'ctrlSrf')
AdvancedCanard = PART(name = 'AdvancedCanard', module = 'Part', author = 'C. Jenkins, Porkjet', rescaleFactor = 1, node_attach = '0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1',
CoMOffset = '-0.4, -0.05, 0', CoLOffset = '-0.4, -0.05, 0', CoPOffset = '-0.4, -0.05, 0', TechRequired = 'hypersonicFlight', entryCost = 9200, cost = 800, category = 'Aero',
subcategory = 0, title = 'Advanced Canard', manufacturer = 'C7 Aerospace Division',
description = 'Our engineers thought this design looked "high tech" and therefore must be clear improvement on earlier models.', attachRules = '0,1,0,1,0', mass = 0.08,
thermalMassModifier = 8.0, heatConductivity = 0.06, emissiveConstant = 0.95, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02, angularDrag = 3, crashTolerance = 12,
maxTemp = 2400, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf', tags = 'aero (air control (elev fighter fligh (fore lift plane )rudder stab swept tail')
AdvancedCanard.addMODULE(ModuleControlSurface)
AdvancedCanard.addMODEL(MODEL(model = 'Squad/Parts/Aero/airplaneFins/AdvCanard'))

ModuleControlSurface = MODULE(name = 'ModuleControlSurface', useInternalDragModel = True, dragCoeff = 0.5, deflectionLiftCoeff = 0.52, ctrlSurfaceRange = 15, ctrlSurfaceArea = 1,
actuatorSpeed = 30, transformName = 'ctrlSrf')
CanardController = PART(name = 'CanardController', module = 'Part', author = 'C. Jenkins, Porkjet', rescaleFactor = 1, node_attach = '0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1',
CoMOffset = '-0.55, -0.15, 0', CoLOffset = '-0.55, -0.15, 0', CoPOffset = '-0.55, -0.15, 0', TechRequired = 'advAerodynamics', entryCost = 11400, cost = 720, category = 'Aero',
subcategory = 0, title = 'Standard Canard', manufacturer = 'C7 Aerospace Division',
description = 'Our engineers had a stroke of inspiration after "visiting" the Kerlington production facilities. Introducing our new controllable canards. Warning, hard maneuvering may cause unintended stage separation.',
attachRules = '0,1,0,1,0', mass = 0.1, thermalMassModifier = 8.0, heatConductivity = 0.06, emissiveConstant = 0.95, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02,
angularDrag = 3, crashTolerance = 12, maxTemp = 2400, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf',
tags = 'aero (air control (elev fligh (fore lift plane )rudder stab swept tail')
CanardController.addMODULE(ModuleControlSurface)
CanardController.addMODEL(MODEL(model = 'Squad/Parts/Aero/airplaneFins/Canard'))

ModuleLiftingSurface = MODULE(name = 'ModuleLiftingSurface', useInternalDragModel = True, deflectionLiftCoeff = 1.37, dragAtMaxAoA = 0.6, dragAtMinAoA = 0.1)
sweptWing = PART(name = 'sweptWing', module = 'Part', author = 'C. Jenkins, Porkjet', rescaleFactor = 1, node_attach = '0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 1', CoMOffset = '1.75,-1.0, 0',
CoLOffset = '1.75,-1.0, 0', CoPOffset = '1.75,-1.0, 0', TechRequired = 'aviation', entryCost = 3600, cost = 620, category = 'Aero', subcategory = 0, title = 'Swept Wings',
manufacturer = 'WinterOwl Aircraft Emporium',
description = 'A prototype swept back wing, part of our "Lets Fly", line. Made of light weight composite materials. Guaranteed to generate lift, not guaranteed to ensure crew safety.',
attachRules = '0,1,0,1,1', mass = 0.275, thermalMassModifier = 8.0, heatConductivity = 0.06, emissiveConstant = 0.95, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02,
angularDrag = 2, crashTolerance = 15, maxTemp = 2400, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf', tags = 'aero (air fligh lift plane')
sweptWing.addMODULE(ModuleControlSurface)   
sweptWing.addMODEL(MODEL(model = 'Squad/Parts/Aero/airplaneFins/Swept'))

ModuleControlSurface = MODULE(name = 'ModuleControlSurface', useInternalDragModel = True, dragCoeff = 0.6, deflectionLiftCoeff = 0.61, ctrlSurfaceRange = 25, ctrlSurfaceArea = 1,
actuatorSpeed = 25, transformName = 'ctrlSrf')
tailfin = PART(name = 'tailfin', module = 'Part', author = 'C. Jenkins, Porkjet', rescaleFactor = 1, node_attach = '0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 1', CoMOffset = '0.75, -0.5, 0',
CoLOffset = '0.75, -0.5, 0', CoPOffset = '0.75, -0.5, 0', TechRequired = 'aviation', entryCost = 3800, cost = 600, category = 'Aero', subcategory = 0, title = 'Tail Fin',
manufacturer = 'C7 Aerospace Division',
description = 'This tailfin has passed extensive modeling in our patented P.A.S system.(Paper Airplane Simulation). This fin has been blunted to prevent accidental dismemberment of installing technicians.',
attachRules = '0,1,0,1,0', mass = 0.125, thermalMassModifier = 8.0, heatConductivity = 0.06, emissiveConstant = 0.95, dragModelType = 'none', maximum_drag = 0.02, minimum_drag = 0.02,
angularDrag = 2, crashTolerance = 12, maxTemp = 2400, explosionPotential = 0.1, fuelCrossFeed = True, bulkheadProfiles = 'srf',
tags = 'aero (air canard control (elev fligh (fore lift plane )rudder stab swept')
tailfin.addMODULE(ModuleControlSurface)
tailfin.addMODEL(MODEL(model = 'Squad/Parts/Aero/airplaneFins/TailFin'))

class CelestialBody(object):
    """docstring for ."""
    def __init__(self,name,type,biomes,sm_axis,radius,GM,rot_per,SOI,atmo_border,atmo_limit,space_border):
        self.name = name
        self.type = type
        self.biomes = biomes
        self.sm_axis = sm_axis
        self.radius = radius
        self.GM = GM
        self.rot_per = rot_per
        self.SOI = SOI
        self.atmo_border = atmo_border
        self.atmo_limit = atmo_limit
        self.space_border = space_border
        self.sync = ((GM*rot_per**2)/(4*pi**2))**(1/3)-radius

kerbol = CelestialBody('Kerbol','Star',['Global'],np.nan,261600000,1.1723328*10**18,432000.00,np.nan,18000,600000,1000000000)
moho = CelestialBody('Moho','Planet',['Global','North Pole','Northern Sinkhole Ridge','Northern Sinkhole','Highlands','Midlands','Minor Craters','Central Lowlands','Western Lowlands',
'South Western Lowlands','South Eastern Lowlands','Canyon','South Pole'],5263138304,250000,1.6860938*10**11,1210000.0,9646663.0,0,0,80000)
eve = CelestialBody('Eve','Planet',['Global','Poles','Lowlands','Midlands','Highlands','Foothills','Peaks','Impact Ejecta','Explodium Sea','Akatsuki Lake','Shallows','Crater Lake',
'Western Sea','Olympus','Craters','Eastern Sea'],9832684544,700000,8.1717302*10**12,80500.000,85109365,22000,90000,400000)
gilly = CelestialBody('Gilly','Moon',['Global','Lowlands','Midlands','Highlands'],31500000,13000,8289449.8,28255.000,126123.27,0,0,6000)
kerbin = CelestialBody('Kerbin','Planet',['Global','Ice Caps','Northern Ice Shelf','Southern Ice Shelf','Tundra','Highlands','Mountains','Grasslands','Deserts','Badlands','Shores',
'Water'],13599840256,600000,3.5316000*10**12,21549.425,84159286,18000,70000,250000)
mun = CelestialBody('Mun','Moon',['Global','Poles','Polar Lowlands','Polar Crater','Highlands','Highland Craters','Midlands','Midland Craters','Lowlands','Northeast Basin','Farside Basin',
'Northwest Crater','East Farside Crater','Canyons','Farside Crater','East Crater','Twin Craters','Southwest Crater'],12000000,200000,6.5138398*10**10,138984.38,2429559.1,0,0,60000)
minmus = CelestialBody('Minmus','Moon',['Global','Poles','Lowlands','Midlands','Highlands','Slopes','Flats','Lesser Flats','Great Flats','Greater Flats'],47000000,60000,1.7658000*10**9,
40400.000,2247428.4,0,0,30000)
duna = CelestialBody('Duna','Planet',['Global','Poles','Polar Highlands','Polar Craters','Highlands','Midlands','Lowlands','Craters','Midland Sea','Northeast Basin','Southern Basin',
'Northern Shelf','Midland Canyon','Eastern Canyon','Western Canyon'],20726155264,320000,3.0136321*10**11,65517.859,47921949,12000,50000,140000)
ike = CelestialBody('Ike','Planet',['Global','Polar Lowlands','Midlands','Lowlands','Eastern Mountain Ridge','Western Mountain Ridge','Central Mountain Range','South Eastern Mountain Range',
'South Pole'],3200000,130000,1.8568369*10**10,65517.862,1049598.9,0,0,50000)
dres = CelestialBody('Dres','Planet',['Global','Poles','Highlands','Midlands','Lowlands','Ridges','Impact Ejecta','Impact Craters','Canyons'],40839348203,138000,2.1484489*10**10,34800.000,
32832840,0,0,25000)
jool = CelestialBody('Jool','Planet',['Global'],68773560320,6000000,2.8252800*10**14,36000.000,2.4559852*10**9,120000,200000,4000000)
laythe = CelestialBody('Laythe','Moon',['Global','Poles','Shores','Dunes','Crescent Bay','The Sagen Sea','Crater Island','Shallows','Crater Bay','Degrasse Sea','Peak'],27184000,500000,
1.9620000*10**12,52980.879,3723645.8,10000,50000,200000)
vall = CelestialBody('Vall','Moon',['Global','Poles','Highlands','Midlands','Lowlands','Mountains','Northeast Basin','Northwest Basin','Southern Basin','Southern Valleys'],43152000,300000,
2.0748150*10**11,105962.09,2406401.4,0,0,90000)
tylo = CelestialBody('Tylo','Moon',['Global','Highlands','Midlands','Lowlands','Mara','Minor Craters','Gagarin Crater','Grissom Crater','Galileio Crater','Tycho Crater'],68500000,600000,
2.8252800*10**12,211926.36,10856518,0,0,250000)
bop = CelestialBody('Bop','Moon',['Global','Poles','Slopes','Peaks','Valley','Ridges'],128500000,65000,2.4868349*10**9,544507.43,1221060.9,0,0,25000)
pol = CelestialBody('Pol','Moon',['Global','Poles','Lowlands','Midlands','Highlands'],179890000,44000,7.2170208*10**8,901902.62,1042138.9,0,0,22000)
eeloo = CelestialBody('Eeloo','Planet',['Global','Poles','Northern Glaciers','Midlands','Lowlands','Ice Canyons','Highlands','Craters','Fragipan','Babbage Patch','Southern Glaciers',
'Mu Glacier'],90118820000,210000,7.4410815*10**10,19460.000,1.1908294*10**8,0,0,60000)

bodies = [kerbol,moho,eve,gilly,kerbin,mun,minmus,duna,ike,dres,jool,laythe,vall,tylo,bop,pol,eeloo]
planets = [b for b in bodies if b.type == 'Planet']

activity = pd.Series(['Surface Sample','EVA Report','Asteroid Sample','Crew Report','Mystery Goo Observation','Materials Study','Temperature Scan','Atmospheric Pressure Scan','Gravity Scan',
'Seismic Scan','Atmosphere Analysis','Infrared Telescope'],name='Activity')
situation = pd.Series(['Surface: Landed','Surface: Splashed','Flying Low','Flying High','In Space Low','In Space High'],name='Situation')
science = pd.DataFrame(np.array(np.meshgrid(activity,situation,[b.name for b in bodies])).T.reshape(-1,3))
science.rename(columns={0:'Activity',1:'Situation',2:'Celestial Body'},inplace=True)

biomes = pd.DataFrame()
for b in bodies:
    biomes = biomes.append(pd.DataFrame(np.array(np.meshgrid(b.name,b.biomes)).T.reshape(-1,2)))

biomes.rename(columns={0:'Celestial Body',1:'Biome'},inplace=True)
ksp = pd.merge(science,biomes,how='left',left_on='Celestial Body', right_on='Celestial Body')

#Remove unavailable experiments
surface = ksp.loc[(ksp['Activity'] == 'Surface Sample') & (~ksp['Situation'].str.contains('Surface')),:]
asteroid = ksp.loc[(ksp['Activity'] == 'Asteroid Sample')]
gravity = ksp.loc[(ksp['Activity'] == 'Gravity Scan') & (ksp['Situation'].str.contains('Flying')),:]
seismic = ksp.loc[(ksp['Activity'] == 'Seismic Scan') & (ksp['Situation'] != 'Surface: Landed'),:]
atmosphere = ksp.loc[(ksp['Activity'] == 'Atmosphere Analysis') & ((ksp['Situation'] == 'Surface: Splashed') | (ksp['Situation'].str.contains('Space'))),:]
infrared = ksp.loc[(ksp['Activity'] == 'Infrared Telescope') & (ksp['Situation'] != 'In Space High'),:]
droplist = pd.concat([surface,asteroid,gravity,seismic,atmosphere,infrared])
ksp.drop(droplist.index,inplace=True)

#Remove local biomes from global experiments
eva = ksp.loc[(ksp['Activity'] == 'EVA Report') & ((ksp['Situation'] == 'Flying High') | (ksp['Situation'] == 'In Space High')) & (ksp['Biome'] != 'Global'),:]
crew = ksp.loc[(ksp['Activity'] == 'Crew Report') & ((ksp['Situation'] == 'Flying High') | (ksp['Situation'].str.contains('Space'))) & (ksp['Biome'] != 'Global'),:] 
mystery = ksp.loc[(ksp['Activity'] == 'Mystery Goo Observation') & (~ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] != 'Global'),:]
materials = ksp.loc[(ksp['Activity'] == 'Materials Study') & (~ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] != 'Global'),:]
temperature = ksp.loc[(ksp['Activity'] == 'Temperature Scan') & (~ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] != 'Global'),:]
atmospheric = ksp.loc[(ksp['Activity'] == 'Atmospheric Pressure Scan') & (~ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] != 'Global'),:]
infrared = ksp.loc[(ksp['Activity'] == 'Infrared Telescope') & (ksp['Biome'] != 'Global'),:]
droplist = pd.concat([eva,crew,mystery,materials,temperature,atmospheric,infrared])
ksp.drop(droplist.index,inplace=True)

#Remove global biomes from local experiments
eva = ksp.loc[(ksp['Activity'] == 'EVA Report') & ((ksp['Situation'] != 'Flying High') & (ksp['Situation'] != 'In Space High')) & (ksp['Biome'] == 'Global'),:]
crew = ksp.loc[(ksp['Activity'] == 'Crew Report') & ((ksp['Situation'] != 'Flying High') & (~ksp['Situation'].str.contains('Space'))) & (ksp['Biome'] == 'Global'),:] 
mystery = ksp.loc[(ksp['Activity'] == 'Mystery Goo Observation') & (ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] == 'Global'),:]
materials = ksp.loc[(ksp['Activity'] == 'Materials Study') & (ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] == 'Global'),:]
temperature = ksp.loc[(ksp['Activity'] == 'Temperature Scan') & (ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] == 'Global'),:]
atmospheric = ksp.loc[(ksp['Activity'] == 'Atmospheric Pressure Scan') & (ksp['Situation'].str.contains('Surface')) & (ksp['Biome'] == 'Global'),:]
gravity = ksp.loc[(ksp['Activity'] == 'Gravity Scan') & (ksp['Biome'] == 'Global'),:]
seismic = ksp.loc[(ksp['Activity'] == 'Seismic Scan') & (ksp['Biome'] == 'Global'),:]
atmosphere = ksp.loc[(ksp['Activity'] == 'Atmosphere Analysis') & (ksp['Biome'] == 'Global'),:]
droplist = pd.concat([eva,crew,mystery,materials,temperature,atmospheric,gravity,seismic,atmosphere])
ksp.drop(droplist.index,inplace=True)

#Remove atmospheric activities from planets with no atmosphere
droplist = ksp[(ksp['Celestial Body'] != 'Kerbol') & (ksp['Celestial Body'] != 'Eve') & (ksp['Celestial Body'] != 'Kerbin') & (ksp['Celestial Body'] != 'Duna') & (ksp['Celestial Body'] != 'Jool') 
& (ksp['Celestial Body'] != 'Laythe') & (ksp['Situation'].str.contains('Flying'))]
ksp.drop(droplist.index,inplace=True)
droplist = ksp[(ksp['Celestial Body'] != 'Kerbol') & (ksp['Celestial Body'] != 'Eve') & (ksp['Celestial Body'] != 'Kerbin') & (ksp['Celestial Body'] != 'Duna') & (ksp['Celestial Body'] != 'Jool') 
& (ksp['Celestial Body'] != 'Laythe') & (ksp['Activity'] == 'Atmosphere Analysis')]
ksp.drop(droplist.index,inplace=True)

#Remove splashed from planets with no water
droplist = ksp[(ksp['Celestial Body'] != 'Eve') & (ksp['Celestial Body'] != 'Kerbin') & (ksp['Celestial Body'] != 'Laythe') & (ksp['Situation'] == 'Surface: Splashed')]
ksp.drop(droplist.index,inplace=True)

#Remove surface from planets with no surface
droplist = ksp[((ksp['Celestial Body'] == 'Kerbol') | (ksp['Celestial Body'] == 'Jool')) & (ksp['Situation'].str.contains('Surface'))]
ksp.drop(droplist.index,inplace=True)

#Different Landings for eve
droplist = ksp[(ksp['Celestial Body'] == 'Eve') & (ksp['Situation'] == 'Surface: Landed') & ((ksp['Biome'] == 'Explodium Sea') | (ksp['Biome'] == 'Akatsuki Lake') | 
(ksp['Biome'] == 'Shallows') | (ksp['Biome'] == 'Crater Lake') | (ksp['Biome'] == 'Western Sea') | (ksp['Biome'] == 'Eastern Sea'))]
ksp.drop(droplist.index,inplace=True)
droplist = ksp[(ksp['Celestial Body'] == 'Eve') & (ksp['Situation'] == 'Surface: Splashed') & (ksp['Biome'] != 'Explodium Sea') & (ksp['Biome'] != 'Akatsuki Lake') & 
(ksp['Biome'] != 'Shallows') & (ksp['Biome'] != 'Crater Lake') & (ksp['Biome'] != 'Western Sea') & (ksp['Biome'] != 'Eastern Sea')]
ksp.drop(droplist.index,inplace=True)

#Different Landings for Kerbin
droplist = ksp[(ksp['Celestial Body'] == 'Kerbin') & (ksp['Situation'] == 'Surface: Landed') & (ksp['Biome'] == 'Water')]
ksp.drop(droplist.index,inplace=True)
droplist = ksp[(ksp['Celestial Body'] == 'Kerbin') & (ksp['Situation'] == 'Surface: Splashed') & (ksp['Biome'] != 'Water')]
ksp.drop(droplist.index,inplace=True)

#Different Landings for Laythe
droplist = ksp[(ksp['Celestial Body'] == 'Laythe') & (ksp['Situation'] == 'Surface: Landed') & ((ksp['Biome'] == 'Crescent Bay') | (ksp['Biome'] == 'The Sagen Sea') | 
(ksp['Biome'] == 'Shallows') | (ksp['Biome'] == 'Crater Bay') | (ksp['Biome'] == 'Degrasse Sea'))]
ksp.drop(droplist.index,inplace=True)
droplist = ksp[(ksp['Celestial Body'] == 'Laythe') & (ksp['Situation'] == 'Surface: Splashed') & (ksp['Biome'] != 'Crescent Bay') & (ksp['Biome'] != 'The Sagen Sea') & 
(ksp['Biome'] != 'Shallows') & (ksp['Biome'] != 'Crater Bay') & (ksp['Biome'] != 'Degrasse Sea')]
ksp.drop(droplist.index,inplace=True)

#Altitudes for experiments
ksp.loc[ksp['Situation'].str.contains('Surface'),'Altitude Min'] = 0
ksp.loc[ksp['Situation'].str.contains('Surface'),'Altitude Max'] = 0
ksp.loc[ksp['Situation'] == 'Flying Low', 'Altitude Min'] = 0

for b in bodies:
    ksp.loc[(ksp['Situation'] == 'Flying Low') & (ksp['Celestial Body'] == b.name), 'Altitude Max'] = b.atmo_border
    ksp.loc[(ksp['Situation'] == 'Flying High') & (ksp['Celestial Body'] == b.name), 'Altitude Min'] = b.atmo_border
    ksp.loc[(ksp['Situation'] == 'Flying High') & (ksp['Celestial Body'] == b.name), 'Altitude Max'] = b.atmo_limit
    ksp.loc[(ksp['Situation'] == 'In Space Low') & (ksp['Celestial Body'] == b.name), 'Altitude Min'] = b.atmo_limit
    ksp.loc[(ksp['Situation'] == 'In Space Low') & (ksp['Celestial Body'] == b.name), 'Altitude Max'] = b.space_border
    ksp.loc[(ksp['Situation'] == 'In Space High') & (ksp['Celestial Body'] == b.name), 'Altitude Min'] = b.space_border
    ksp.loc[(ksp['Situation'] == 'In Space High') & (ksp['Celestial Body'] == b.name), 'Altitude Max'] = b.SOI

dv_altitude change(body,initalt,finalalt):
    rA = body.radius + initalt
    rB = body.radius + finalalt
    GM = body.GM
    atx = (rA + rB) / 2
    ViA = =sqrt(GM / rA)
    VfB = sqrt(GM / rB)
    VtxA = sqrt(GM * (2 / rA - 1 / atx)
    VtxB = sqrt(GM * (2 / rB - 1 / atx)
    DVA = abs(VtxA - ViA)
    DVB = abs(VfB - VtxB)
    DVT = DVA + DVB
    return DVT
    
dv_lunartransfer(body1,body2,initalt,finalalt):    
    GM1 = body1.gm
	GM2 = body2.gm
	r1 = body1.radius + initalt
	r2 = body2.radius + finalalt
	aM = body2.sm_axis
	atx = (r1 + aM) / 2
	Vi1 = sqrt(GM1 / r1)
	VtxA = sqrt(GM1 * (2 / rA - 1 / atx)
	
	

dv_planetrarytransfer():
    
dv_lunarlunarttransfer():

    
orbit = ksp[['Celestial Body','Situation','Altitude Min']].drop_duplicates()
departure = orbit.rename(columns={'Celestial Body':'Departure Body','Situation':'Departure Situation','Altitude Min':'Departure Altitude'})
arrival = orbit.rename(columns={'Celestial Body':'Arrival Body','Situation':'Arrival Situation','Altitude Min':'Arrival Altitude'})
departure['key']=0
arrival['key']=0
orbit = departure.merge(arrival,how='outer')
orbit.drop('key',axis=1,inplace=True)
orbit = orbit[(orbit['Departure Situation'].str.contains('Space')) & (orbit['Arrival Situation'].str.contains('Space'))]

for b in bodies:
    orbit.loc[orbit['Departure Body'] == b.name,'Kerbol GM'] = kerbol.GM
    orbit.loc[orbit['Departure Body'] == b.name,'Departure sm_Axis'] = b.sm_axis
    orbit.loc[orbit['Departure Body'] == b.name,'Departure Radius'] = b.radius
    orbit.loc[orbit['Departure Body'] == b.name,'Departure GM'] = b.GM
    orbit.loc[orbit['Arrival Body'] == b.name,'Arrival sm_axis'] = b.sm_axis
    orbit.loc[orbit['Arrival Body'] == b.name,'Arrival Radius'] = b.radius
    orbit.loc[orbit['Arrival Body'] == b.name,'Arrival GM'] = b.GM

orbit['Departure Altitude'] = orbit['Departure Radius'] + orbit['Departure Altitude']
orbit['Arrival Altitude'] = orbit['Arrival Radius'] + orbit['Arrival Altitude']

for p in planets:
    orbit.loc[orbit['Departure Body'] == p.name,'Departure Parent GM'] = p.GM
    orbit.loc[orbit['Departure Body'] == p.name,'Departure Parent sm_axis'] = p.sm_axis
    orbit.loc[orbit['Arrival Body'] == p.name,'Arrival Parent sm_axis'] = p.sm_axis
    orbit.loc[orbit['Arrival Body'] == p.name,'Arrival Parent GM'] = p.GM

def dv_altitudechange(GM,ri,rf):
    atx = (ri + rf) / 2
    vii = sqrt(GM / ri)
    vff = sqrt(GM / rf)
    vtxi = sqrt(GM * (2 / ri - 1 / atx))
    vtxf = sqrt(GM * (2 / rf - 1 / atx))
    dvi = abs(vtxi - vii)
    dvf = abs(vtxf - vff)
    dv = dvi + dvi
    return dv

def dv_lunartransfer(GMP, GMM, ri, rf, sm):
    atx = (ri + sm) / 2
    vii = sqrt(GMP / ri)
    vff = sqrt(GMM / rf)
    vm = sqrt(GMP / sm)
    vtxi = sqrt(GM * (2 / ri - 1 / atx))
    vtxf = sqrt(GM * (2 / sm - 1 / atx))
    dvi = abs(vtxi - vii)
    mav = vm - vtxf
    mov = sqrt(mav ** 2 + 2 * GMM / rf)
    dvf = abs(mov - vff)
    dv = dvi + dvf
    return dv

orbit['Altitude Change'] = orbit.apply(lambda x: dv_altitudechange(x['Departure GM'],x['Departure Altitude'],x['Arrival Altitude']),axis=1)


ksp.to_excel('ksp.xlsx')
