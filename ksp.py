import pandas as pd
import numpy as np
from math import sqrt
from math import pi

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

orbit['Departure Alt'] = orbit['Departure Radius'] + orbit['Departure Altitude']
orbit['Arrival Alt'] = orbit['Arrival Radius'] + orbit['Arrival Altitude']

for p in planets:
    orbit.loc[orbit['Departure Body'] == p.name,'Departure Parent GM'] = p.GM
    orbit.loc[orbit['Departure Body'] == p.name,'Departure Parent sm_axis'] = p.sm_axis
    orbit.loc[orbit['Arrival Body'] == p.name,'Arrival Parent sm_axis'] = p.sm_axis
    orbit.loc[orbit['Arrival Body'] == p.name,'Arrival Parent GM'] = p.GM

def dv_altitudechange(GM,rA,rB):
    atx = (rA + rB) / 2
    via = sqrt(GM / rA)
    vfb = sqrt(GM / rB)
    vtxa = sqrt(GM * (2 / rA - 1 / atx))
    vtxb = sqrt(GM * (2 / rB - 1 / atx))
    dva = abs(vtxa - via)
    dvb = abs(vtxb - vfb)
    dv = dva + dvb
    return dv

orbit['Delta-v'] = orbit.apply(lambda x: planet_dv(x['Departure sm_axis'],x['Arrival sm_axis'],x['Departure GM'],x['rA'],x['Arrival GM'],x['rB'],x['GMsys']),axis=1)
  

for b in bodies:
    orbit['Delta-v'] = orbit.apply(lambda x: planet_dv(x['ri'],x['rf'],x['GMA'],x['rA'],x['GMB'],x['rB']),axis=1)
    
ksp.to_excel('ksp.xlsx')
