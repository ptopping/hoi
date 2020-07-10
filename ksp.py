import pandas as pd
import numpy as np
from math import sqrt
from math import pi

import pandas as pd

class CelestialBody(object):
    """docstring for CelestialBody"""
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.properties = {}
        self.orbit = {}
        self.scaled = {}

    def add_properties(self, property):
        self.properties.update(property.__dict__)

    def add_orbit(self, orbit):
        self.orbit.update(orbit.__dict__)

    def add_atmosphere(self, scaled):
        self.scaled.update(scaled.__dict__)

class Properties(object):
    """docstring for Properties"""
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.sciencevalues = {}
        self.biomes = []

    def add_science(self, sciencevalues):
        self.sciencevalues.update(sciencevalues.__dict__)

    def add_biome(self, biome):
        self.biomes.append(biome.__dict__.get('name'))

class Orbit(object):
    """docstring for Orbit
    referenceBody: The body that this body is orbiting around.
    semiMajorAxis: The altitude of the highest point in the orbit
    longitudeOfAscendingNode: The position of the highest point on the orbit
                              circle
    color: The color of the orbit line in the Tracking Station
    nodeColor: The color of the circle that marks the planets current position
               on the orbit
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Atmosphere(object):
    """docstring for Atmosphere
    enabled: Whether the body has an atmosphere.
    oxygen: Whether the atmosphere contains oxygen
    staticDensityASL: Atmospheric density at sea level. Used to calculate the
                      parameters of the atmosphere if no curves are used.
    atmosphereDepth: The height of the atmosphere.
    pressureCurveIsNormalized: Whether the pressure curve should use absolute
                               (0 - atmosphereDepth) or relative (0 - 1)
                               values.
    staticPressureASL: The static pressure at sea level. Used to calculate the
                       parameters of the atmosphere if no curves are used.
    temperatureCurveIsNormalized: Whether the temperature curve should use
                                  absolute (0 - atmosphereDepth) or relative
                                  (0 - 1) values.
    temperatureSeaLevel: The static temperature at sea level. Used to
                         calculate the parameters of the atmosphere if no
                         curves are used.
    ambientColor: All objects inside of the atmosphere will slightly shine in
                  this color.
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Biome(object):
    """docstring for Biome"""
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)



class ScienceValues(object):
    """docstring for ScienceValues
    landedDataValue: Science multiplier for landed science.
    splashedDataValue: Science multiplier for splashed down science.
    flyingLowDataValue: Science multiplier for flying low science.
    flyingHighDataValue: Science multiplier for flying high science.
    inSpaceLowDataValue: Science multiplier for in space low science.
    inSpaceHighDataValue: Science multiplier for in space high science.
    flyingAltitudeThreshold: Altitude when "flying at <body>" transitions
                             from/to "from <body>'s upper atmosphere"
    spaceAltitudeThreshold: Altitude when "in space low" transitions from/to
                            "in space high"
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

bop = CelestialBody(name='Bop', barycenter=False, identifier='Squad/Bop',
                    implements=None, finalizeOrbit=False,
                    randomMainMenuBody=False, contractWeight=30)

properties = Properties(description='Bop is a small moon in the vicinity of '\
                        'Jool. In Kerbal mythology, Bop is believed to be '\
                        'the home of the Kraken, a mischievous creature '\
                        'said to play with the ships of hapless explorers, '\
                        'by spinning them out of control until torn asunder,'\
                        ' then casting them into oblivion.', radius=65000,
                        geeASL=0.0600204949543182, mass=3.72610898343278E+19,
                        gravParameter=2486834944.41491, rotates=True,
                        rotationPeriod=544507.428516654, tidallyLocked=True,
                        initialRotation=230,
                        inverseRotThresholdAltitude=100000,
                        albedo=0.200000002980232,
                        emissivity=0.800000011920929,
                        coreTemperatureOffset=10, 
                        timewarpAltitudeLimits=[0, 24500, 24500, 24500, 40000,
                                                60000, 80000, 100000],
                        sphereOfInfluence=1221060.86284253,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/bop_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Bop^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=12, splashedDataValue=1,
                              flyingLowDataValue=1, flyingHighDataValue=1,
                              inSpaceLowDataValue=9, inSpaceHighDataValue=8,
                              recoveryValue=8, flyingAltitudeThreshold=18000,
                              spaceAltitudeThreshold=25000)

peaks = Biome(name='Peaks', displayName='Peaks', value=0,
              color=[0.866666675, 0.800000012, 0.654901981, 1])

ridges = Biome(name='Ridges', displayName='Ridges', value=0,
               color=[0.768627465, 0.698039234, 0.545098066, 1])

poles = Biome(name='Poles', displayName='Poles', value=0,
              color=[0.960784316, 0.886274517, 0.725490212, 1])

slopes = Biome(name='Slopes', displayName='Slopes', value=0,
               color=[0.68235296, 0.615686297, 0.470588237, 1])

valley = Biome(name='Valley', displayName='Valley', value=0, 
               color=[0.592156887, 0.549019635, 0.450980395, 1])

orbit = Orbit(referenceBody='Jool', inclination=15,
              eccentricity=0.234999999403954, semiMajorAxis=128500000,
              longitudeOfAscendingNode=10, argumentOfPeriapsis=25,
              meanAnomalyAtEpoch=0.899999976158142,
              meanAnomalyAtEpochD=51.5662001957363, epoch=0,
              color=[0.729411781, 0.627451003, 0.494117647, 0.501960814],
              nodeColor=[0.729411781, 0.627451003, 0.494117647, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.12, 12], period=544507.428516654)

properties.add_science(sciencevalues)
biomes = [peaks, ridges, poles, slopes, valley]
for b in biome:
    properties.add_biome(b)
bop.add_properties(properties)
bop.add_orbit(orbit)

dres = CelestialBody(name='Dres', barycenter=False, identifier='Squad/Dres',
                     implements=None, finalizeOrbit=False,
                     randomMainMenuBody=False, contractWeight=30)

properties = Properties(description='Dres is a very small planet. It was '\
                        'the first planet considered to be a dwarf. It’s '\
                        'orbit is highly irregular and together with it’s '\
                        'size it took a long time to discover since half '\
                        'the time it was not where scientists expected to '\
                        'find a planet. Due to its nature of frequenting '\
                        'the bad parts of space. This dwarf planet was '\
                        'officially labeled as “Not to be trusted” by the '\
                        'scientific community.', radius=138000,
                        geeASL=0.115039284567105, mass=3.21909365785247E+20,
                        gravParameter=21484488600, rotates=True,
                        rotationPeriod=34800, tidallyLocked=False, 
                        initialRotation=25,
                        inverseRotThresholdAltitude=100000, albedo=0.12,
                        emissivity=0.88, coreTemperatureOffset=0,
                        timewarpAltitudeLimits=[0, 10000, 10000, 30000, 50000,
                                                100000, 200000, 300000],
                        sphereOfInfluence=32832839.5767762,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/dres_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Dres^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=8, splashedDataValue=1,
                              flyingLowDataValue=1, flyingHighDataValue=1,
                              inSpaceLowDataValue=7, inSpaceHighDataValue=6,
                              recoveryValue=6, flyingAltitudeThreshold=18000,
                              spaceAltitudeThreshold=25000)

poles = Biome(name='Poles', displayName='Poles', value=0,
              color=[0.972549021, 0.929411769, 0.862745106, 1])

midlands = Biome(name='Midlands', displayName='Midlands', value=0,
                 color = [0.525490224, 0.505882382, 0.470588237, 1])

lowlands = Biome(name='Lowlands', displayName='Lowlands', value=0,
                 color=[0.458823532, 0.443137258, 0.419607848, 1])

ridges = Biome(name='Ridges', displayName='Ridges', value=0,
               color=[0.694117665, 0.654901981, 0.592156887, 1])

highlands = Biome(name='Highlands', displayName='Highlands', value=0,
                  color=[0.819607854, 0.760784328, 0.670588255, 1])

impact_craters=Biome(name='Impact Craters', displayName='Impact Craters',
                     value=0, color=[0.380392164, 0.36470589, 0.349019617, 1])

impact_ejecta = Biome(name='Impact Ejecta', displayName='Impact Ejecta',
                      value=0,
                      color=[0.611764729, 0.580392182, 0.533333361, 1])

canyons = Biome(name='Canyons', displayName='Canyons', value=0,
                color=[0.333333343, 0.321568638, 0.305882365, 1])

orbit = Orbit(referenceBody='Sun', inclination=5, eccentricity=0.145,
              semiMajorAxis=40839348203, longitudeOfAscendingNode=280,
              argumentOfPeriapsis=90, meanAnomalyAtEpoch=3.14000010490417,
              meanAnomalyAtEpochD=179.908753681645, epoch=0,
              color=[0.352941185, 0.266666681, 0.196078435, 0.501960814],
              nodeColor=[0.352941185, 0.266666681, 0.196078435, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.03, 25], period=47893063.1385932)

properties.add_science(sciencevalues)
properties.add_science(sciencevalues)
biomes = [poles, midlands, lowlands, ridges, highlands, impact_craters,
          impact_ejecta, canyons]
for b in biome:
    properties.add_biome(b)
dres.add_properties(properties)
dres.add_orbit(orbit)

duna =  CelestialBody(name='Duna', barycenter=False, identifier='Squad/Duna',
                      implements=None, finalizeOrbit=False,
                      randomMainMenuBody=False, contractWeight=30)
        
properties = Properties(description='Also known as the red dot that you can '\
                        'see if you squint at it really hard, Duna has long '\
                        'been a wonder to Kerbalkind. The planet has been '\
                        'held in much awe, due to its striking red color '\
                        'and stark contrast to the color green.',
                        radius=320000, geeASL=0.300102493404406,
                        mass=4.51542702477492E+21,
                        gravParameter=301363211975.098, rotates=True,
                        rotationPeriod=65517.859375, tidallyLocked=False,
                        initialRotation=90,
                        inverseRotThresholdAltitude=100000,
                        albedo=0.170000001788139,
                        emissivity=0.829999983310699, coreTemperatureOffset=0,
                        timewarpAltitudeLimits=[0, 30000, 30000, 60000,
                                                100000, 300000, 600000,
                                                800000],
                        sphereOfInfluence=47921949.369738,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/duna_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Duna^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=8, splashedDataValue=1,
                              flyingLowDataValue=5, flyingHighDataValue=5,
                              inSpaceLowDataValue=7, inSpaceHighDataValue=5,
                              recoveryValue=5, flyingAltitudeThreshold=12000,
                              spaceAltitudeThreshold=140000)

poles = Biome(name='Poles', displayName='Poles', value=0, color=[1,1,1,1])

midlands = Biome(name='Midlands', displayName='Midlands', value=0,
                 color=[0.988235295, 0.549019635, 0.349019617, 1])

lowlands = Biome(name='Lowlands', displayName='Lowlands', value=0,
                 color=[0.913725495, 0.41568628, 0.192156866, 1])

craters = Biome(name='Craters', displayName='Craters', value=0,
                color=[0.717647076, 0.396078438, 0.00392156886, 1])

highlands = Biome(name='Highlands', displayName='Highlands', value=0,
                  color=[1, 0.666666687, 0.513725519, 1])

midland_sea = Biome(name='Midland Sea', displayName='Midland Sea', value=0,
                    color=[1, 0.568627477, 0.00784313772, 1])

northern_basin = Biome(name='Northern Basin', displayName='Northeast Basin',
                       value=0,
                       color=[0.709803939, 0.160784319, 0.13333334, 1])

southern_basin = Biome(name='Southern Basin', displayName='Southern Basin',
                       value=0,
                       color=[0.823529422, 0.290196091, 0.262745112, 1])

northern_shelf = Biome(name='Northern Shelf', displayName='Northern Shelf',
                       value=0,
                       color=[0.580392182, 0.0705882385, 0.0431372561, 1])

midland_canyon = Biome(name='Midland Canyon', displayName='Midland Canyon',
                       value=0,
                       color=[0.733333349, 0.345098048, 0.0352941193, 1])

eastern_canyon = Biome(name='Eastern Canyon', displayName='Eastern Canyon',
                       value=0, color=[0.600000024, 0.266666681, 0, 1])

western_canyon = Biome(name='Western Canyon', displayName='Western Canyon',
                       value=0, color=[0.435294122, 0.192156866, 0, 1])

polar_highlands = Biome(name='Polar Highlands', displayName='Polar Highlands',
                        value=0,
                        color=[0.90196079, 0.90196079, 0.90196079, 1])

polar_craters = Biome(name='Polar Craters', displayName='Polar Craters',
                      value=0,
                      color=[0.745098054, 0.745098054, 0.745098054, 1])

orbit = Orbit(referenceBody='Sun', inclination=0.0599999986588955,
              eccentricity=0.0509999990463257, semiMajorAxis=20726155264,
              longitudeOfAscendingNode=135.5, argumentOfPeriapsis=0,
              meanAnomalyAtEpoch=3.14000010490417,
              meanAnomalyAtEpochD=179.908753681645, epoch=0,
              color=[0.639215708, 0.247058824, 0.156862751, 0.501960814],
              nodeColor=[0.639215708, 0.247058824, 0.156862751, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.03, 25], period=17315400.1425698)

atmosphere = Atmosphere(enabled=True, oxygen=False,
                        staticDensityASL=0.149935108881759,
                        adiabaticIndex=1.20000004768372,
                        atmosphereDepth=50000,
                        gasMassLapseRate=3.04406677337964,
                        atmosphereMolarMass=0.0430000014603138,
                        pressureCurveIsNormalized=False,
                        staticPressureASL=6.75500011444092,
                        temperatureCurveIsNormalized=False,
                        temperatureLapseRate=0.005, temperatureSeaLevel=250,
                        ambientColor=[0.323529422, 0.220170617, 0.173659176,
                                      1],
                        lightColor=[0.509465635, 0.588402689, 0.643137276, 0],
                        addAFG=True)

properties.add_science(sciencevalues)
biomes = [poles, midlands, lowlands, craters, highlands, midland_sea,
          northern_basin, southern_basin, northern_shelf, midland_canyon,
          eastern_canyon, western_canyon, polar_highlands, polar_craters]
for b in biome:
    properties.add_biome(b)
duna.add_properties(properties)
duna.add_orbit(orbit)
duna.add_atmosphere(atmosphere)

eeloo = CelestialBody(name='Eeloo', barycenter=False,
                      identifier='Squad/Eeloo', implements=None,
                      finalizeOrbit=False, randomMainMenuBody=False,
                      contractWeight=30)
        
properties = Properties(description='There’s been a considerable amount of '\
                        'controversy around the status of Eeloo as being a '\
                        'proper planet or a just “lump of ice going around '\
                        'the Sun”. The debate is still ongoing, since most '\
                        'academic summits held to address the issue have '\
                        'devolved into, on good days, petty name calling, '\
                        'and on worse ones, all-out brawls.', radius=210000,
                        geeASL=0.172058761891442, mass=1.11492242417007E+21,
                        gravParameter=74410814527.0496, rotates=True,
                        rotationPeriod=19460, tidallyLocked=False,
                        initialRotation=25,
                        inverseRotThresholdAltitude=100000, albedo=0.5,
                        emissivity=0.5, coreTemperatureOffset=0,
                        timewarpAltitudeLimits=[0, 4000, 4000, 20000, 30000,
                                                40000, 70000, 150000],
                        sphereOfInfluence=119082941.647812,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/eeloo_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Eeloo^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=15, splashedDataValue=1,
                              flyingLowDataValue=1, flyingHighDataValue=1,
                              inSpaceLowDataValue=12, inSpaceHighDataValue=10,
                              recoveryValue=10, flyingAltitudeThreshold=18000,
                              spaceAltitudeThreshold=60000)

poles = Biome(name='Poles', displayName='Poles', value=0, color=1, 1, 1, 1)

northern_glaciers = Biome(name='Northern Glaciers',
                           displayName='Northern Glaciers', value=0,
                           color = [0.792156875, 0.792156875, 0.792156875, 1])

lowlands = Biome(name='Lowlands', displayName='Lowlands', value=0,
                  color = [0.482352942, 0.639215708, 0.905882359, 1])

highlands = Biome(name='Highlands', displayName='Highlands', value=0,
                  color=[0.835294127, 0.854901969, 0.882352948, 1])

ice_canyons = Biome(name='Ice Canyons', displayName='Ice Canyons', value=0,
                    color=[1, 0.709803939, 0.388235301, 1])

craters = Biome(name='Craters', displayName='Craters', value=0,
                color=[0.87843138, 0.533333361, 0.13333334, 1])

midlands = Biome(name='Midlands', displayName='Midlands', value=0,
                 color=[0.745098054, 0.807843149, 0.909803927, 1])

fragipan = Biome(name='Fragipan', displayName='Fragipan', value=0,
                 color=[1, 0.80392158, 0.580392182, 1])

babbage_patch = Biome(name='Babbage Patch', displayName='Babbage Patch',
                      value=0, color=[0.592156887, 0.701960802, 0.894117653,
                                      1])

southern_glaciers = Biome(name='Southern Glaciers',
                          displayName='Southern Glaciers', value=0,
                          color=[0.87843138, 0.87843138, 0.87843138, 1])

mu_glacier = Biome(name='Mu Glacier', displayName='Mu Glacier', value=0,
                   color=[0.486274511, 0.486274511, 0.486274511, 1])

orbit = Orbit(referenceBody='Sun', inclination=6.15, eccentricity=0.26,
              semiMajorAxis=90118820000, longitudeOfAscendingNode=50,
              argumentOfPeriapsis=260, meanAnomalyAtEpoch=3.14000010490417,
              meanAnomalyAtEpochD=179.908753681645, epoch=0,
              color=[0.407843143, 0.41568628, 0.41568628, 0.501960814],
              nodeColor=[0.407843143, 0.41568628, 0.41568628, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.03, 25], period=156992048.397359)

properties.add_science(sciencevalues)
biomes = [poles, northern_glaciers, lowlands, highlands, ice_canyons, craters,
          midlands, fragipan, babbage_patch, southern_glaciers, mu_glacier]
for b in biome:
    properties.add_biome(b)
eeloo.add_properties(properties)
eeloo.add_orbit(orbit)

eve = CelestialBody(name='Eve', barycenter=False, identifier='Squad/Eve',
                    implements=None, finalizeOrbit=False,
                    randomMainMenuBody=False, contractWeight=30)

properties = Properties(description='Eve is certainly the purplest object '\
                        'in the solar system. It’s one of the larger, most '\
                        'visible objects, mainly because of its very, very '\
                        'purple tint.It is considered by some to be almost '\
                        'a sister planet to Kerbin. Well, despite the '\
                        'purple, and the toxic atmosphere, and the extreme '\
                        'press- ures and temperatures. Actually, it’s not '\
                        'very similar at all is it? Who are those people?',
                        radius=700000, geeASL=1.7005807760833,
                        mass=1.2243980038014E+23,
                        gravParameter=8171730229210.87, rotates=True,
                        rotationPeriod=80500, tidallyLocked=False,
                        initialRotation=0, inverseRotThresholdAltitude=100000,
                        albedo=0.449999988079071,
                        emissivity=0.550000011920929, coreTemperatureOffset=0,
                        timewarpAltitudeLimits=[0, 30000, 30000, 60000, 
                                                120000, 240000, 480000,
                                                600000],
                        sphereOfInfluence=85109364.7382441,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/eve_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Eve^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=8, splashedDataValue=8,
                              flyingLowDataValue=6, flyingHighDataValue=6,
                              inSpaceLowDataValue=7, inSpaceHighDataValue=5,
                              recoveryValue=5, flyingAltitudeThreshold=22000,
                              spaceAltitudeThreshold=400000)

poles = Biome(name='Poles', displayName='Poles', value=0,
              color=[0.862745106, 0.75686276, 0.996078432, 1])

midlands = Biome(name='Midlands', displayName='Midlands', value=0,
                 color=[0.450980395, 0.180392161, 0.525490224, 1])

explodium_sea = Biome(name='Explodium Sea', displayName='Explodium Sea',
                      value=0, color=[0.694117665, 0.349019617, 0.513725519,
                                      1])

lowlands = Biome(name='Lowlands', displayName='Lowlands', value=0,
                 color=[0.360784322, 0.0980392173, 0.435294122, 1])

highlands = Biome(name='Highlands', displayName='Highlands', value=0,
                  color=[0.541176498, 0.286274523, 0.611764729, 1])

peaks = Biome(name='Peaks', displayName='Peaks', value=0,
              color=[0.65882355, 0.443137258, 0.729411781, 1])

impact_ejecta = Biome(name='Impact Ejecta', displayName='Impact Ejecta',
                      value=0, color=[0.654901981, 0.396078438, 0.980392158,
                                      1])

crater_lake = Biome(name='Crater Lake', displayName='Crater Lake', value=0,
                    color=[0.556862772, 0.184313729, 0.360784322, 1])

western_sea = Biome(name='Western Sea', displayName='Western Sea', value=0,
                    color=[0.835294127, 0.556862772, 0.690196097, 1])

olympus = Biome(name='Olympus', displayName='Olympus', value=0,
                color=[1 ,1, 1, 1])

eastern_sea = Biome(name='Eastern Sea', displayName='Eastern Sea', value=0,
                    color=[0.41568628, 0.0705882385, 0.235294119, 1])

craters = Biome(name='Craters', displayName='Craters', value=0,
                color=[0.654901981, 0.396078438, 0.980392158, 1])

foothills = Biome(name='Foothills', displayName='Foothills', value=0,
                  color=[0.811764717, 0.650980413, 0.854901969, 1])

akatsuki_lake = Biome(name='Akatsuki Lake', displayName='Akatsuki Lake',
                      value=0, color=[0.729411781, 0.568627477, 0.741176486,
                                      1])

shallows = Biome(name='Shallows', displayName='Shallows', value=0,
                 color=[0.545098066, 0.400000006, 0.552941203, 1])

orbit = Orbit(referenceBody='Sun', inclination=2.09999990463257,
              eccentricity=0.00999999977648258, semiMajorAxis=9832684544,
              longitudeOfAscendingNode=15, argumentOfPeriapsis=0,
              meanAnomalyAtEpoch=3.14000010490417,
              meanAnomalyAtEpochD=179.908753681645, epoch=0,
              color=[0.423529416, 0.125490203, 0.894117653,0.501960814],
              nodeColor=[0.423529416, 0.125490203, 0.894117653, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.03, 25], period=5657995.14648304)

atmosphere = Atmosphere(enabled=True, oxygen=False,
                        staticDensityASL=6.23837138885624,
                        adiabaticIndex=1.20000004768372,
                        atmosphereDepth=90000,
                        gasMassLapseRate=19.0254171112692,
                        atmosphereMolarMass=0.0430000014603138,
                        pressureCurveIsNormalized=False,
                        staticPressureASL=506.625,
                        temperatureCurveIsNormalized=False,
                        temperatureLapseRate=0.00453333333333333,
                        temperatureSeaLevel=408,
                        ambientColor=[0.223535195, 0.194325268, 0.305882365, 
                                      1],
                        lightColor=[0.449885309, 0.514925361, 0.347322196, 1],
                        addAFG=True)

properties.add_science(sciencevalues)
biomes = [poles, midlands, explodium_sea, lowlands, highlands, peaks,
          impact_ejecta, crater_lake, western_sea, olympus, eastern_sea,
          craters, foothills, akatsuki_lake, shallows]
for b in biome:
    properties.add_biome(b)
eve.add_properties(properties)
eve.add_orbit(orbit)
eve.add_atmosphere(atmosphere)
            
gilly = CelestialBody(name='Gilly', barycenter=False,
                      identifier='Squad/Gilly', implements=None,
                      finalizeOrbit=False, randomMainMenuBody=False,
                      contractWeight=30)
properties = Properties(description='Gilly is a lumpy rock wandering around '\
                        'the orbit of Eve. It’s by far the smallest natural '\
                        'satellite that the Kerbal Astronomical Society has '\
                        'discovered. Due to the large amount of squinting '\
                        'and eye strain associated with its discovery, '\
                        'wearing glasses has now become synonymous with '\
                        'being an accomplished Astronomer.', radius=13000,
                        geeASL=0.00500170791285985, mass=1.24203632781093E+17,
                        gravParameter=8289449.81471635, rotates=True,
                        rotationPeriod=28255, tidallyLocked=False,
                        initialRotation=5, inverseRotThresholdAltitude=100000,
                        albedo=0.15, emissivity=0.85,
                        coreTemperatureOffset=20,
                        timewarpAltitudeLimits=[0, 8000, 8000, 8000, 20000,
                                                40000, 80000, 100000],
                        sphereOfInfluence=126123.271704568,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/gilly_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Gilly^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=9, splashedDataValue=1,
                              flyingLowDataValue=1, flyingHighDataValue=1,
                              inSpaceLowDataValue=8, inSpaceHighDataValue=6,
                              recoveryValue=6, flyingAltitudeThreshold=18000,
                              spaceAltitudeThreshold=6000)

midlands = Biome(name='Midlands', displayName='Midlands', value=0,
                 color=[0.796078444, 0.631372571, 0.36470589, 1])
                
lowlands = Biome(name='Lowlands', displayName='Lowlands', value=0,
                 color=[0.647058845, 0.505882382, 0.278431386, 1])

highlands = Biome(name='Highlands', displayName='Highlands', value=0,
                  color = [0.917647064, 0.792156875, 0.588235319, 1])

orbit = Orbit(referenceBody='Eve', inclination=12,
              eccentricity=0.550000011920929, semiMajorAxis=31500000,
              longitudeOfAscendingNode=80, argumentOfPeriapsis=10,
              meanAnomalyAtEpoch=0.899999976158142,
              meanAnomalyAtEpochD=51.5662001957363, epoch=0,
              color=[0.635294139, 0.494117647, 0.431372553, 0.501960814],
              nodeColor=[0.635294139, 0.494117647, 0.431372553, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.12, 12], period=388587.376847929)

properties.add_science(sciencevalues)
biomes = [midlands, lowlands, highlands]
for b in biome:
    properties.add_biome(b)
eve.add_properties(properties)
eve.add_orbit(orbit)

ike = CelestialBody(name='Ike', barycenter=False, identifier='Squad/Ike',
                    implements=None, finalizeOrbit=False,
                    randomMainMenuBody=False, contractWeight=30)

properties = Properties(description='Ike is a relatively large, grey object '\
                        'occasionally seen orbiting Duna. Scientists have '\
                        'postulated that Ike is seemingly perfectly '\
                        'positioned to sneakily interfere with any object '\
                        'that presumes to come orbiting near its parent.',
                        radius=130000, geeASL=0.112038263210561,
                        mass=2.78216152235874E+20,
                        gravParameter=18568368573.144, rotates=True,
                        rotationPeriod=65517.8621348081, tidallyLocked=True,
                        initialRotation=0, inverseRotThresholdAltitude=100000,
                        albedo = 0.14, emissivity = 0.86,
                        coreTemperatureOffset=2,
                        timewarpAltitudeLimits=[0, 5000, 5000, 10000, 25000,
                                                50000, 100000, 200000],
                        sphereOfInfluence=1049598.93931162,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        biomeMap='BUILTIN/ike_biome', nonExactThreshold=-1,
                        exactSearch=False, useTheInName=False,
                        displayName='Ike^N', selectable=True,
                        RnDVisibility='Visible', RnDRotation=False,
                        maxZoom=60000)

sciencevalues = ScienceValues(landedDataValue=8, splashedDataValue=1,
                              flyingLowDataValue=1, flyingHighDataValue=1,
                              inSpaceLowDataValue=7, inSpaceHighDataValue=5,
                              recoveryValue=5, flyingAltitudeThreshold=18000,
                              spaceAltitudeThreshold=50000)

polar_lowlands = Biome(name='Polar Lowlands', displayName='Polar Lowlands',
                       value=0, color=[0.474509805, 0.466666669, 0.4627451,
                                       1])

midlands = Biome(name='Midlands', displayName='Midlands', value=0,
                 color=[0.576470613, 0.576470613, 0.576470613, 1])

eastern_mountain_ridge = Biome(name='Eastern Mountain Ridge',
                               displayName='Eastern Mountain Ridge', value=0,
                               color=[1, 1, 1, 1])
western_mountain_ridge = Biome(name='Western Mountain Ridge',
                               displayName='Western Mountain Ridge', value=0,
                               color=[0.925490201, 0.925490201, 0.925490201,
                                      1])

lowlands = Biome(name='Lowlands', displayName='Lowlands', value=0,
                 color=[0.407843143, 0.407843143, 0.407843143, 1])

south_eastern_mountain_range = Biome(name='South Eastern Mountain Range',
                                     displayName='South Eastern Mountain '\
                                     'Range', value=0, color=[0.854901969,
                                                              0.854901969,
                                                              0.854901969,
                                                              1])

south_pole = Biome(name='South Pole', displayName='South Pole', value=0,
                   color=[0.517647088, 0.517647088, 0.517647088, 1])

central_mountain_range = Biome(name='Central Mountain Range',
                               displayName='Central Mountain Range', value=0,
                               color = [0.800000012, 0.800000012, 0.800000012,
                                        1])

orbit = Orbit(referenceBody='Duna', inclination=0.200000002980232,
              eccentricity=0.0299999993294477, semiMajorAxis=3200000,
              longitudeOfAscendingNode=0, argumentOfPeriapsis=0,
              meanAnomalyAtEpoch=1.70000004768372,
              meanAnomalyAtEpochD=97.4028279043159, epoch=0,
              color=[0.521568656, 0.541176498, 0.603921592, 0.501960814],
              nodeColor=[0.521568656, 0.541176498, 0.603921592, 0.501960814],
              mode='REDRAW_AND_RECALCULATE', icon='ALL',
              cameraSmaRatioBounds=[0.03, 25], period=65517.8621348081)

jool = CelestialBody(name='Jool', barycenter=False, identifier='Squad/Jool',
                     implements=None, finalizeOrbit=False,
                     randomMainMenuBody=False, contractWeight=30)
        
properties = Properties(description='Jool is particularly known for being a '\
                        'rather large, predominantly green planet. '\
                        'Kerbalkind has longed to visit it since it was '\
                        'first spotted in the sky. Philosophers reason that '\
                        'the swirling green planet must be a really nice '\
                        'place to visit, on account of its wholesome '\
                        'coloration.If you look at Jool through a '\
                        'telescope, it is fuzzy.', radius=6000000,
                        geeASL=0.800273295870079, mass=4.23321273059351E+24,
                        gravParameter=282528004209995, rotates=True,
                        rotationPeriod=36000, tidallyLocked=False,
                        initialRotation=0, inverseRotThresholdAltitude=220000,
                        albedo=0.52, emissivity=0.48,
                        coreTemperatureOffset=80,
                        timewarpAltitudeLimits=[0, 0, 15000, 60000, 150000,
                                                300000, 600000, 1200000],
                        sphereOfInfluence=2455985185.42347,
                        solarRotationPeriod=False,
                        navballSwitchRadiusMult=0.06,
                        navballSwitchRadiusMultLow=0.055,
                        nonExactThreshold=0.05, exactSearch=False,
                        useTheInName=False, displayName='Jool^N',
                        selectable=True, RnDVisibility='Visible',
                        RnDRotation=False, maxZoom=60000
            ScienceValues
            {
                landedDataValue = 30
                splashedDataValue = 1
                flyingLowDataValue = 12
                flyingHighDataValue = 9
                inSpaceLowDataValue = 7
                inSpaceHighDataValue = 6
                recoveryValue = 6
                flyingAltitudeThreshold = 120000
                spaceAltitudeThreshold = 4000000
            }
        }
        Orbit
        {
            referenceBody = Sun
            inclination = 1.30400002002716
            eccentricity = 0.0500000007450581
            semiMajorAxis = 68773560320
            longitudeOfAscendingNode = 52
            argumentOfPeriapsis = 0
            meanAnomalyAtEpoch = 0.100000001490116
            meanAnomalyAtEpochD = 5.72957803668559
            epoch = 0
            color = 0.329411775,0.521568656,0.0745098069,0.501960814
            nodeColor = 0.329411775,0.521568656,0.0745098069,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.03 25
            period = 104661432.107989
        }
        Atmosphere
        {
            enabled = True
            oxygen = False
            staticDensityASL = 6.70262205528434
            adiabaticIndex = 1.43
            atmosphereDepth = 200000
            gasMassLapseRate = 2.07657256052129
            atmosphereMolarMass = 0.0022
            pressureCurveIsNormalized = False // Whether the pressure curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            staticPressureASL = 1519.875
            temperatureCurveIsNormalized = False // Whether the temperature curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            temperatureLapseRate = 0.001
            temperatureSeaLevel = 200
            ambientColor = 0.0754820928,0.208955199,0.0686121732,1
            lightColor = 0.674509823,0.596078455,0.850980401,0
            addAFG = True
{
    Body
    {
        name = Kerbin
        barycenter = False
        identifier = Squad/Kerbin
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = A unique world, Kerbin has flat plains, soaring mountains and wide, blue oceans. Home to the Kerbals, it has just the right conditions to support a vast, seemingly undepletable population of the eager green creatures.Reaching a stable orbit around Kerbin is one of the first things budding space programs strive for. It is said that those who can get their ship into orbit are halfway to anywhere.
            radius = 600000
            geeASL = 1.00034160493135
            mass = 5.29151583439215E+22
            gravParameter = 3531600000000
            rotates = True
            rotationPeriod = 21549.4251830898
            tidallyLocked = False
            initialRotation = 90
            inverseRotThresholdAltitude = 100000
            albedo = 0.35
            emissivity = 0.65
            coreTemperatureOffset = 0
            timewarpAltitudeLimits = 0 30000 30000 60000 120000 240000 480000 600000
            sphereOfInfluence = 84159286.4796305
            solarRotationPeriod = True
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/kerbin_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Kerbin^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 0.3
                splashedDataValue = 0.4
                flyingLowDataValue = 0.7
                flyingHighDataValue = 0.9
                inSpaceLowDataValue = 1
                inSpaceHighDataValue = 1.5
                recoveryValue = 1
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 250000
            }
            Biomes
            {
                Value
                {
                    name = Water
                    displayName = Water
                    value = 0
                    color = 0.215686277,0.384313732,0.670588255,1
                }
                Value
                {
                    name = Grasslands
                    displayName = Grasslands
                    value = 0
                    color = 0.513725519,0.737254918,0.180392161,1
                }
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.36470589,0.521568656,0.164705887,1
                }
                Value
                {
                    name = Shores
                    displayName = Shores
                    value = 0
                    color = 0.980392158,0.949019611,0.717647076,1
                }
                Value
                {
                    name = Mountains
                    displayName = Mountains
                    value = 0
                    color = 0.654901981,0.654901981,0.654901981,1
                }
                Value
                {
                    name = Deserts
                    displayName = Deserts
                    value = 0
                    color = 0.917647064,0.749019623,0.435294122,1
                }
                Value
                {
                    name = Badlands
                    displayName = Badlands
                    value = 0
                    color = 0.592156887,0.309803933,0.137254909,1
                }
                Value
                {
                    name = Tundra
                    displayName = Tundra
                    value = 0
                    color = 0.78039217,0.56078434,0.874509811,1
                }
                Value
                {
                    name = Ice Caps
                    displayName = Ice Caps
                    value = 0
                    color = 1,1,1,1
                }
                Value
                {
                    name = Northern Ice Shelf
                    displayName = Northern Ice Shelf
                    value = 0
                    color = 0.894117653,0.992156863,1,1
                }
                Value
                {
                    name = Southern Ice Shelf
                    displayName = Southern Ice Shelf
                    value = 0
                    color = 0.847058833,0.847058833,0.847058833,1
                }
            }
        }
        Orbit
        {
            referenceBody = Sun
            inclination = 0
            eccentricity = 0
            semiMajorAxis = 13599840256
            longitudeOfAscendingNode = 0
            argumentOfPeriapsis = 0
            meanAnomalyAtEpoch = 3.14000010490417
            meanAnomalyAtEpochD = 179.908753681645
            epoch = 0
            color = 0.541176498,0.792156875,0.760784328,0.501960814
            nodeColor = 0.541176498,0.792156875,0.760784328,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.03 25
            period = 9203544.61750141
        }
        Atmosphere
        {
            enabled = True
            oxygen = True
            staticDensityASL = 1.22497705725583
            adiabaticIndex = 1.39999997615814
            atmosphereDepth = 70000
            gasMassLapseRate = 8.33518264702189
            atmosphereMolarMass = 0.0289644002914429
            pressureCurveIsNormalized = False // Whether the pressure curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            staticPressureASL = 101.324996948242
            temperatureCurveIsNormalized = False // Whether the temperature curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            temperatureLapseRate = 0.0041
            temperatureSeaLevel = 287
            ambientColor = 0.243137255,0.250980407,0.254901975,1
            lightColor = 0.649999976,0.569999993,0.474999994,0.5
            addAFG = True
{
    Body
    {
        name = Laythe
        barycenter = False
        identifier = Squad/Laythe
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = When Laythe was first discovered, it was not entered in the records because the scientist in charge thought he was looking at Kerbin.Luckily this error was corrected when a plucky intern informed him that “telescopes don’t work that way”.The intern was shortly afterwards “promoted” and moved to the experimental rocket testing program.
            radius = 500000
            geeASL = 0.800273295870079
            mass = 2.93973106291216E+22
            gravParameter = 1962000029236.08
            rotates = True
            rotationPeriod = 52980.8790593796
            tidallyLocked = True
            initialRotation = 90
            inverseRotThresholdAltitude = 100000
            albedo = 0.3
            emissivity = 0.7
            coreTemperatureOffset = 80
            timewarpAltitudeLimits = 0 30000 30000 60000 120000 240000 480000 600000
            sphereOfInfluence = 3723645.81113302
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/laythe_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Laythe^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 14
                splashedDataValue = 12
                flyingLowDataValue = 11
                flyingHighDataValue = 10
                inSpaceLowDataValue = 9
                inSpaceHighDataValue = 8
                recoveryValue = 8
                flyingAltitudeThreshold = 10000
                spaceAltitudeThreshold = 200000
            }
            Biomes
            {
                Value
                {
                    name = Poles
                    displayName = Poles
                    value = 0
                    color = 0.725490212,0.835294127,0.890196085,1
                }
                Value
                {
                    name = Shores
                    displayName = Shores
                    value = 0
                    color = 1,0.925490201,0.647058845,1
                }
                Value
                {
                    name = Dunes
                    displayName = Dunes
                    value = 0
                    color = 0.839215696,0.745098054,0.384313732,1
                }
                Value
                {
                    name = Crescent Bay
                    displayName = Crescent Bay
                    value = 0
                    color = 0.368627459,0.43921569,0.800000012,1
                }
                Value
                {
                    name = The Sagen Sea
                    displayName = The Sagen Sea
                    value = 0
                    color = 0.149019614,0.384313732,0.686274529,1
                }
                Value
                {
                    name = Crater Island
                    displayName = Crater Island
                    value = 0
                    color = 0.678431392,0.580392182,0.196078435,1
                }
                Value
                {
                    name = Shallows
                    displayName = Shallows
                    value = 0
                    color = 0.443137258,0.619607866,0.843137264,1
                }
                Value
                {
                    name = Crater Bay
                    displayName = Crater Bay
                    value = 0
                    color = 0.282352954,0.490196079,0.760784328,1
                }
                Value
                {
                    name = DeGrasse Sea
                    displayName = Degrasse Sea
                    value = 0
                    color = 0.0470588244,0.266666681,0.549019635,1
                }
                Value
                {
                    name = Peaks
                    displayName = Peaks
                    value = 0
                    color = 1,0.964705884,0.835294127,1
                }
            }
        }
        Orbit
        {
            referenceBody = Jool
            inclination = 0
            eccentricity = 0
            semiMajorAxis = 27184000
            longitudeOfAscendingNode = 0
            argumentOfPeriapsis = 0
            meanAnomalyAtEpoch = 3.14000010490417
            meanAnomalyAtEpochD = 179.908753681645
            epoch = 0
            color = 0.266666681,0.337254912,0.611764729,0.501960814
            nodeColor = 0.266666681,0.337254912,0.611764729,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.03 25
            period = 52980.8790593796
        }
        Atmosphere
        {
            enabled = True
            oxygen = True
            staticDensityASL = 0.764571404126208
            adiabaticIndex = 1.39999997615814
            atmosphereDepth = 50000
            gasMassLapseRate = 4.84741125702493
            atmosphereMolarMass = 0.0289644002914429
            pressureCurveIsNormalized = False // Whether the pressure curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            staticPressureASL = 60.795
            temperatureCurveIsNormalized = False // Whether the temperature curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            temperatureLapseRate = 0.00564
            temperatureSeaLevel = 282
            ambientColor = 0.187128037,0.239393175,0.305882365,1
            lightColor = 0.843283594,0.668219268,0.49830395,0
            addAFG = True
{
    Body
    {
        name = Minmus
        barycenter = False
        identifier = Squad/Minmus
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = Minmus is the smallest moon orbiting Kerbin. From the surface of Kerbin, it can be seen on clear days as a tiny blue speck in the sky. It is often mistaken as dirt on telescope lenses or dead pixels, but the top minds at the Kerbal Astronomical Society assure us it is a real moon nevertheless.
            radius = 60000
            geeASL = 0.05001708099188
            mass = 2.64575795662095E+19
            gravParameter = 1765800026.31247
            rotates = True
            rotationPeriod = 40400
            tidallyLocked = False
            initialRotation = 230
            inverseRotThresholdAltitude = 100000
            albedo = 0.5
            emissivity = 0.7
            coreTemperatureOffset = 1
            timewarpAltitudeLimits = 0 3000 3000 6000 12000 24000 48000 60000
            sphereOfInfluence = 2247428.3879023
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/minmus_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Minmus^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 5
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 4
                inSpaceHighDataValue = 2.5
                recoveryValue = 2.5
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 30000
            }
            Biomes
            {
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.380392164,0.513725519,0.509803951,1
                }
                Value
                {
                    name = Midlands
                    displayName = Midlands
                    value = 0
                    color = 0.529411793,0.670588255,0.615686297,1
                }
                Value
                {
                    name = Lowlands
                    displayName = Lowlands
                    value = 0
                    color = 0.690196097,0.882352948,0.807843149,1
                }
                Value
                {
                    name = Flats
                    displayName = Flats
                    value = 0
                    color = 0.752941191,1,0.905882359,1
                }
                Value
                {
                    name = Great Flats
                    displayName = Great Flats
                    value = 0
                    color = 0.411764711,0.760784328,0.737254918,1
                }
                Value
                {
                    name = Greater Flats
                    displayName = Greater Flats
                    value = 0
                    color = 0.647058845,0.843137264,0.850980401,1
                }
                Value
                {
                    name = Lesser Flats
                    displayName = Lesser Flats
                    value = 0
                    color = 0.545098066,0.831372559,0.811764717,1
                }
                Value
                {
                    name = Poles
                    displayName = Poles
                    value = 0
                    color = 1,1,1,1
                }
                Value
                {
                    name = Slopes
                    displayName = Slopes
                    value = 0
                    color = 0.600000024,0.800000012,0.733333349,1
                }
            }
        }
        Orbit
        {
            referenceBody = Kerbin
            inclination = 6
            eccentricity = 0
            semiMajorAxis = 47000000
            longitudeOfAscendingNode = 78
            argumentOfPeriapsis = 38
            meanAnomalyAtEpoch = 0.899999976158142
            meanAnomalyAtEpochD = 51.5662001957363
            epoch = 0
            color = 0.556862772,0.454901963,0.627451003,0.501960814
            nodeColor = 0.556862772,0.454901963,0.627451003,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.12 12
            period = 1077310.52101881
        }

{
    Body
    {
        name = Moho
        barycenter = False
        identifier = Squad/Moho
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = Moho figures in Kerbal mythology as a fiery place with oceans of flowing lava. In reality however, it’s much less interesting. Scientists speculate about possible ways to make it “awesome like in the stories”. Some of those ideas have led to new breakthroughs in aerospace technology.
            radius = 250000
            geeASL = 0.275093947318621
            mass = 2.52633139930162E+21
            gravParameter = 168609378654.509
            rotates = True
            rotationPeriod = 1210000
            tidallyLocked = False
            initialRotation = 190
            inverseRotThresholdAltitude = 100000
            albedo = 0.1
            emissivity = 0.9
            coreTemperatureOffset = 0
            timewarpAltitudeLimits = 0 10000 10000 30000 50000 100000 200000 300000
            sphereOfInfluence = 9646663.02332811
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/moho_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Moho^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 10
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 8
                inSpaceHighDataValue = 7
                recoveryValue = 7
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 80000
            }
            Biomes
            {
                Value
                {
                    name = North Pole
                    displayName = North Pole
                    value = 0
                    color = 0.839215696,0.741176486,0.650980413,1
                }
                Value
                {
                    name = Northern Sinkhole Ridge
                    displayName = Northern Sinkhole Ridge
                    value = 0
                    color = 0.650980413,0.501960814,0.368627459,1
                }
                Value
                {
                    name = Northern Sinkhole
                    displayName = Northern Sinkhole
                    value = 0
                    color = 0.4627451,0.419607848,0.384313732,1
                }
                Value
                {
                    name = Midlands
                    displayName = Midlands
                    value = 0
                    color = 0.70588237,0.56078434,0.427450985,1
                }
                Value
                {
                    name = Western Lowlands
                    displayName = Western Lowlands
                    value = 0
                    color = 0.345098048,0.294117659,0.254901975,1
                }
                Value
                {
                    name = Central Lowlands
                    displayName = Central Lowlands
                    value = 0
                    color = 0.345098048,0.309803933,0.282352954,1
                }
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.776470602,0.623529434,0.486274511,1
                }
                Value
                {
                    name = Minor Craters
                    displayName = Minor Craters
                    value = 0
                    color = 0.301960796,0.266666681,0.239215687,1
                }
                Value
                {
                    name = South Western Lowlands
                    displayName = South Western Lowlands
                    value = 0
                    color = 0.388235301,0.345098048,0.309803933,1
                }
                Value
                {
                    name = South Eastern Lowlands
                    displayName = South Eastern Lowlands
                    value = 0
                    color = 0.419607848,0.376470596,0.337254912,1
                }
                Value
                {
                    name = Canyon
                    displayName = Canyon
                    value = 0
                    color = 0.294117659,0.243137255,0.203921571,1
                }
                Value
                {
                    name = South Pole
                    displayName = South Pole
                    value = 0
                    color = 0.847058833,0.698039234,0.564705908,1
                }
            }
        }
        Orbit
        {
            referenceBody = Sun
            inclination = 7
            eccentricity = 0.200000002980232
            semiMajorAxis = 5263138304
            longitudeOfAscendingNode = 70
            argumentOfPeriapsis = 15
            meanAnomalyAtEpoch = 3.14000010490417
            meanAnomalyAtEpochD = 179.908753681645
            epoch = 0
            color = 0.933333337,0.713725507,0.533333361,0.501960814
            nodeColor = 0.933333337,0.713725507,0.533333361,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.03 25
            period = 2215754.21968432
        }

{
    Body
    {
        name = Mun
        barycenter = False
        identifier = Squad/Mun
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = The Mun, is a large satellite orbiting Kerbin. It is mostly gray in appearance, with craters of various sizes dotting its otherwise smooth surface.The Mun’s discovery is widely regarded as one of the more important breakthroughs of Kerbal evolution. Granted, it didn’t happen all that long ago, but it’s still fair to say Kerbals are wiser and more evolved now than they were back then.
            radius = 200000
            geeASL = 0.166056700098353
            mass = 9.7599066119646E+20
            gravParameter = 65138397520.7807
            rotates = True
            rotationPeriod = 138984.376574476
            tidallyLocked = True
            initialRotation = 230
            inverseRotThresholdAltitude = 100000
            albedo = 0.1
            emissivity = 0.9
            coreTemperatureOffset = 5
            timewarpAltitudeLimits = 0 5000 5000 10000 25000 50000 100000 200000
            sphereOfInfluence = 2429559.11656475
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/mun_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = True
            displayName = The Mun^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 4
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 3
                inSpaceHighDataValue = 2
                recoveryValue = 2
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 60000
            }
            Biomes
            {
                Value
                {
                    name = Midlands
                    displayName = Midlands
                    value = 0
                    color = 0.36470589,0.458823532,0.509803951,1
                }
                Value
                {
                    name = Northern Basin
                    displayName = Northeast Basin
                    value = 0
                    color = 0.423529416,0.458823532,0.576470613,1
                }
                Value
                {
                    name = East Crater
                    displayName = East Crater
                    value = 0
                    color = 0.580392182,0.627451003,0.796078444,1
                }
                Value
                {
                    name = Northwest Crater
                    displayName = Northwest Crater
                    value = 0
                    color = 0.407843143,0.474509805,0.694117665,1
                }
                Value
                {
                    name = Southwest Crater
                    displayName = Southwest Crater
                    value = 0
                    color = 0.65882355,0.678431392,0.737254918,1
                }
                Value
                {
                    name = Farside Crater
                    displayName = Farside Crater
                    value = 0
                    color = 0.56078434,0.647058845,0.90196079,1
                }
                Value
                {
                    name = Canyons
                    displayName = Canyons
                    value = 0
                    color = 0.325490206,0.368627459,0.521568656,1
                }
                Value
                {
                    name = Polar Crater
                    displayName = Polar Crater
                    value = 0
                    color = 0.603921592,0.647058845,0.670588255,1
                }
                Value
                {
                    name = Poles
                    displayName = Poles
                    value = 0
                    color = 0.917647064,0.925490201,0.929411769,1
                }
                Value
                {
                    name = Polar Lowlands
                    displayName = Polar Lowlands
                    value = 0
                    color = 0.811764717,0.827450991,0.839215696,1
                }
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.450980395,0.53725493,0.58431375,1
                }
                Value
                {
                    name = Highland Craters
                    displayName = Highland Craters
                    value = 0
                    color = 0.694117665,0.733333349,0.870588243,1
                }
                Value
                {
                    name = Midland Craters
                    displayName = Midland Craters
                    value = 0
                    color = 0.164705887,0.247058824,0.294117659,1
                }
                Value
                {
                    name = East Farside Crater
                    displayName = East Farside Crater
                    value = 0
                    color = 0.603921592,0.611764729,0.917647064,1
                }
                Value
                {
                    name = Twin Craters
                    displayName = Twin Craters
                    value = 0
                    color = 0.678431392,0.745098054,0.945098042,1
                }
                Value
                {
                    name = Lowlands
                    displayName = Lowlands
                    value = 0
                    color = 0.254901975,0.356862754,0.41568628,1
                }
                Value
                {
                    name = Farside Basin
                    displayName = Farside Basin
                    value = 0
                    color = 0.529411793,0.556862772,0.639215708,1
                }
            }
        }
        Orbit
        {
            referenceBody = Kerbin
            inclination = 0
            eccentricity = 0
            semiMajorAxis = 12000000
            longitudeOfAscendingNode = 0
            argumentOfPeriapsis = 0
            meanAnomalyAtEpoch = 1.70000004768372
            meanAnomalyAtEpochD = 97.4028279043159
            epoch = 0
            color = 0.611764729,0.627451003,0.70588237,0.501960814
            nodeColor = 0.611764729,0.627451003,0.70588237,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.03 25
            period = 138984.376574476
        }

{
    Body
    {
        name = Pol
        barycenter = False
        identifier = Squad/Pol
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = This moon was especially hard to spot, as it looks just like a pollen grain, particularly when observed through telescopes based near dusty fields.Pol was finally discovered when someone decided to write down the location of the pollen, after having given up on yet another failed attempt to be rid of the smudge.
            radius = 44000
            geeASL = 0.0380129809873912
            mass = 1.08135065806823E+19
            gravParameter = 721702080
            rotates = True
            rotationPeriod = 901902.623531173
            tidallyLocked = True
            initialRotation = 25
            inverseRotThresholdAltitude = 100000
            albedo = 0.5
            emissivity = 0.5
            coreTemperatureOffset = 7
            timewarpAltitudeLimits = 0 5000 5000 5000 8000 12000 30000 90000
            sphereOfInfluence = 1042138.89230178
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/pol_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Pol^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 12
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 9
                inSpaceHighDataValue = 8
                recoveryValue = 8
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 22000
            }
            Biomes
            {
                Value
                {
                    name = Poles
                    displayName = Poles
                    value = 0
                    color = 1,0.952941179,0.772549033,1
                }
                Value
                {
                    name = Lowlands
                    displayName = Lowlands
                    value = 0
                    color = 0.713725507,0.647058845,0.407843143,1
                }
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.960784316,0.894117653,0.639215708,1
                }
                Value
                {
                    name = Midlands
                    displayName = Midlands
                    value = 0
                    color = 0.831372559,0.75686276,0.478431374,1
                }
            }
        }
        Orbit
        {
            referenceBody = Jool
            inclination = 4.25
            eccentricity = 0.17085
            semiMajorAxis = 179890000
            longitudeOfAscendingNode = 2
            argumentOfPeriapsis = 15
            meanAnomalyAtEpoch = 0.899999976158142
            meanAnomalyAtEpochD = 51.5662001957363
            epoch = 0
            color = 0.862745106,0.894117653,0.674509823,0.501960814
            nodeColor = 0.862745106,0.894117653,0.674509823,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.12 12
            period = 901902.623531173
        }

{
    Body
    {
        name = Sun
        barycenter = False
        identifier = Squad/Sun
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = The Sun is the most well known object in the daytime sky. Scientists have noted a particular burning sensation and potential loss of vision if it is stared at for long periods of time. This is especially important to keep in mind considering the effect shiny objects have on the average Kerbal.
            radius = 261600000
            geeASL = 1.74684656100137
            mass = 1.75654591319326E+28
            gravParameter = 1.17233279483249E+18
            rotates = True
            rotationPeriod = 432000
            tidallyLocked = False
            initialRotation = 0
            inverseRotThresholdAltitude = 600000
            albedo = 0
            emissivity = 0
            coreTemperatureOffset = 0
            timewarpAltitudeLimits = 0 3270000 3270000 6540000 1.308E+07 2.616E+07 5.232E+07 6.54E+07
            sphereOfInfluence = Infinity
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            nonExactThreshold = 0.05
            exactSearch = False
            useTheInName = True
            displayName = The Sun^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = True
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 1
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 11
                inSpaceHighDataValue = 2
                recoveryValue = 4
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 1E+09
            }
        }
        Atmosphere
        {
            enabled = True
            oxygen = False
            staticDensityASL = 0.00072492861572823
            adiabaticIndex = 1.42999994754791
            atmosphereDepth = 600000
            gasMassLapseRate = 0.465695397616382
            atmosphereMolarMass = 0.00219999998807907
            pressureCurveIsNormalized = False // Whether the pressure curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            staticPressureASL = 16
            temperatureCurveIsNormalized = False // Whether the temperature curve should use absolute (0 - atmosphereDepth) or relative (0 - 1) values.
            temperatureLapseRate = 0.00973333333333333
            temperatureSeaLevel = 5840
            ambientColor = 0,0,0,0
            addAFG = True
{
    Body
    {
        name = Tylo
        barycenter = False
        identifier = Squad/Tylo
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = Tylo was the first moon of Jool to be discovered by the Kerbal Astronomical Society. After many failed attempts to take a flawless picture of Jool to hang on the office walls, it was finally discovered that the wandering white smear was indeed a moon.Scientists speculate that the view from the surface with Laythe, Vall and Jool overhead must be “quite something”.
            radius = 600000
            geeASL = 0.800273295870079
            mass = 4.23321273059351E+22
            gravParameter = 2825280042099.95
            rotates = True
            rotationPeriod = 211926.35802123
            tidallyLocked = True
            initialRotation = 0
            inverseRotThresholdAltitude = 100000
            albedo = 0.1
            emissivity = 0.9
            coreTemperatureOffset = 20
            timewarpAltitudeLimits = 0 30000 30000 60000 120000 240000 480000 600000
            sphereOfInfluence = 10856518.3683586
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/tylo_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Tylo^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 12
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 10
                inSpaceHighDataValue = 8
                recoveryValue = 8
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 250000
            }
            Biomes
            {
                Value
                {
                    name = Midlands
                    displayName = Midlands
                    value = 0
                    color = 0.701960802,0.639215708,0.603921592,1
                }
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.792156875,0.733333349,0.701960802,1
                }
                Value
                {
                    name = Lowlands
                    displayName = Lowlands
                    value = 0
                    color = 0.619607866,0.556862772,0.517647088,1
                }
                Value
                {
                    name = Mara
                    displayName = Mara
                    value = 0
                    color = 0.53725493,0.474509805,0.435294122,1
                }
                Value
                {
                    name = Minor Craters
                    displayName = Minor Craters
                    value = 0
                    color = 0.447058827,0.388235301,0.352941185,1
                }
                Value
                {
                    name = Tycho Crater
                    displayName = Tycho Crater
                    value = 0
                    color = 0.827450991,0.643137276,0.533333361,1
                }
                Value
                {
                    name = Galileio Crater
                    displayName = Galileio Crater
                    value = 0
                    color = 0.741176486,0.541176498,0.423529416,1
                }
                Value
                {
                    name = Grissom Crater
                    displayName = Grissom Crater
                    value = 0
                    color = 0.666666687,0.458823532,0.337254912,1
                }
                Value
                {
                    name = Gagarin Crater
                    displayName = Gagarin Crater
                    value = 0
                    color = 0.58431375,0.388235301,0.274509817,1
                }
            }
        }
        Orbit
        {
            referenceBody = Jool
            inclination = 0.025000000372529
            eccentricity = 0
            semiMajorAxis = 68500000
            longitudeOfAscendingNode = 0
            argumentOfPeriapsis = 0
            meanAnomalyAtEpoch = 3.14000010490417
            meanAnomalyAtEpochD = 179.908753681645
            epoch = 0
            color = 0.827450991,0.666666687,0.666666687,0.501960814
            nodeColor = 0.827450991,0.666666687,0.666666687,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.03 25
            period = 211926.35802123
        }

{
    Body
    {
        name = Vall
        barycenter = False
        identifier = Squad/Vall
        implements = 
        finalizeOrbit = False
        randomMainMenuBody = False
        contractWeight = 30
        Properties
        {
            description = Vall was one of the last Moons of Jool to be discovered. Frustrated scientists kept attempting to wipe it off the lenses of their telescopes. Eventually after a rash of returned telescopes, Advanced Optics Co. finally decided to just tell them it was an actual object in the sky.
            radius = 300000
            geeASL = 0.235080276562617
            mass = 3.10876554482042E+21
            gravParameter = 207481499473.751
            rotates = True
            rotationPeriod = 105962.088893924
            tidallyLocked = True
            initialRotation = 0
            inverseRotThresholdAltitude = 100000
            albedo = 0.5
            emissivity = 0.7
            coreTemperatureOffset = 40
            timewarpAltitudeLimits = 0 24500 24500 24500 40000 60000 80000 100000
            sphereOfInfluence = 2406401.44479404
            solarRotationPeriod = False
            navballSwitchRadiusMult = 0.06
            navballSwitchRadiusMultLow = 0.055
            biomeMap = BUILTIN/vall_biome
            nonExactThreshold = -1
            exactSearch = False
            useTheInName = False
            displayName = Vall^N
            selectable = True
            RnDVisibility = Visible
            RnDRotation = False
            maxZoom = 60000
            ScienceValues
            {
                landedDataValue = 12
                splashedDataValue = 1
                flyingLowDataValue = 1
                flyingHighDataValue = 1
                inSpaceLowDataValue = 9
                inSpaceHighDataValue = 8
                recoveryValue = 8
                flyingAltitudeThreshold = 18000
                spaceAltitudeThreshold = 90000
            }
            Biomes
            {
                Value
                {
                    name = Poles
                    displayName = Poles
                    value = 0
                    color = 0.745098054,0.968627453,0.988235295,1
                }
                Value
                {
                    name = Midlands
                    displayName = Midlands
                    value = 0
                    color = 0.419607848,0.776470602,0.807843149,1
                }
                Value
                {
                    name = Highlands
                    displayName = Highlands
                    value = 0
                    color = 0.270588249,0.698039234,0.737254918,1
                }
                Value
                {
                    name = Lowlands
                    displayName = Lowlands
                    value = 0
                    color = 1,1,1,1
                }
                Value
                {
                    name = Northeast Basin
                    displayName = Northeast Basin
                    value = 0
                    color = 0.698039234,0.698039234,0.698039234,1
                }
                Value
                {
                    name = Northwest Basin
                    displayName = Northwest Basin
                    value = 0
                    color = 0.588235319,0.588235319,0.588235319,1
                }
                Value
                {
                    name = Southern Basin
                    displayName = Southern Basin
                    value = 0
                    color = 0.866666675,0.866666675,0.866666675,1
                }
                Value
                {
                    name = Southern Valleys
                    displayName = Southern Valleys
                    value = 0
                    color = 0.78039217,0.78039217,0.78039217,1
                }
                Value
                {
                    name = Mountains
                    displayName = Mountains
                    value = 0
                    color = 0.611764729,0.850980401,0.870588243,1
                }
            }
        }
        Orbit
        {
            referenceBody = Jool
            inclination = 0
            eccentricity = 0
            semiMajorAxis = 43152000
            longitudeOfAscendingNode = 0
            argumentOfPeriapsis = 0
            meanAnomalyAtEpoch = 0.899999976158142
            meanAnomalyAtEpochD = 51.5662001957363
            epoch = 0
            color = 0.431372553,0.607843161,0.70588237,0.501960814
            nodeColor = 0.431372553,0.607843161,0.70588237,0.501960814
            mode = REDRAW_AND_RECALCULATE
            icon = ALL
            cameraSmaRatioBounds = 0.12 12
            period = 105962.088893924
        }                                                       


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
