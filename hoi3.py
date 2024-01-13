import ast
import glob
import json
import math
import numpy as np
import os
import pandas as pd
import re

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\technologies'

techs = []

def readall(path, listlike):
    directory = glob.glob(os.path.join(path, '*.txt'))
    for file in directory:
        data = open(file, 'r').read()
        
        try:
            jsn = lua_to_dict(data)
            listlike.append(jsn)
        except:
            try:
                jsn = lua_to_dict_alt(data)
                listlike.append(jsn)
            except:
                pass

def lua_to_dict(lua_code):
    lua_code = re.sub(r'\#+.*', '', lua_code, flags=re.MULTILINE)   
    lua_code = re.sub(r'(\w+)\s*=\s*([" \w.-]*)',  r"'\1': '\2',", lua_code)
    lua_code = lua_code.replace("'',{", '{')
    lua_code = lua_code.replace('}', '},') 
    lua_code = ast.literal_eval('{' + lua_code + '}')
    return lua_code

def lua_to_dict_alt(lua_code):
    lua_code = re.sub(r'\#+.*', '', lua_code, flags=re.MULTILINE)   
    lua_code = re.sub(r'(\w+)\s*=\s*([" \w.-]*)',  r"'\1': '\2',", lua_code)
    lua_code = lua_code.replace("'',{", '{')
    lua_code = lua_code.replace('}', '},') 
    lua_code = re.sub(r'\{\s*(\w*)\s*\},',  r"'\1',", lua_code)
    lua_code = ast.literal_eval('{' + lua_code + '}')
    return lua_code

readall(path, techs)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\static_modifiers.txt'
data = open(path, 'r').read()
start = data.find('base_values')

base_values = lua_to_dict(data[start:])
base_values

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\defines.lua'
data = open(path, 'r').read()

def defines_to_dict(lua_code):
    lua_code = re.sub(r'\--.*', '', lua_code, flags=re.MULTILINE)   
    lua_code = re.sub(r'(\w+)\s*=\s*',  r"'\1':", lua_code)
    lua_code = lua_code.replace("'',{", '{')
#     lua_code = lua_code.replace('}', '},') 
    lua_code = ast.literal_eval('{' + lua_code + '}')
    return lua_code

# print(data)
defines = defines_to_dict(data)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\buildings.txt'
data = open(path, 'r').read()
buildings = lua_to_dict(data)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\combined_arms.txt'
data = open(path, 'r').read()
combinedarms = lua_to_dict(data)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\laws.txt'
data = open(path, 'r').read()
laws = lua_to_dict(data)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\minister_types.txt'
data = open(path, 'r').read()
ministers = lua_to_dict(data)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\strategic_resources.txt'
data = open(path, 'r').read()
resources = lua_to_dict(data)

path = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\units'
units = []
readall(path, units)

file = 'D:\\SteamLibrary\\steamapps\\common\\Hearts of Iron 3\\tfh\\common\\countries\\Germany.txt'
lua_code = open(file, 'r').read()
start = lua_code.find('ministers')
lua_code = lua_code[start:]

people = lua_to_dict(lua_code)

file = 'C:\\Users\\Patrick\\Documents\\Paradox Interactive\\Hearts of Iron III\\save games\\Germany.hoi3'
lua_code = open(file, 'r', encoding='latin-1').read()

start = lua_code.find('1=')
end = lua_code.find('REB=')
lua_code[start:end]

def lua_to_dict(lua_code):
    lua_code = re.sub(r'\#+.*', '', lua_code, flags=re.MULTILINE)   
    lua_code = re.sub(r'(\w+)\s*=\s*([" \w.-]*)',  r"'\1': '\2',", lua_code)
    lua_code = lua_code.replace("'',{", '{')
    lua_code = lua_code.replace('}', '},')
    lua_code = re.sub(r'(?={\s*[0-9.]+)({)([0-9.\s]+)(})',  r'[\2]', lua_code)
    lua_code = re.sub(r'(?<=\d)\s+(?=\d|\-)',  r',', lua_code)
#     lua_code = re.sub(r'{\s*([0-9.]*)\s*[0-9.]*\s*}',  r"'\1'", lua_code)
    lua_code = ast.literal_eval('{' + lua_code + '}')
    return lua_code

# {\s*(?=\d+)[\s0-9.]*}


regions = lua_to_dict(lua_code[start:end])

file = 'C:\\Users\\Patrick\\Documents\\Paradox Interactive\\Hearts of Iron III\\save games\\Germany.hoi3'
save = open(file, 'r', encoding='latin-1').read()

start = save.find('REB=')
save = save[start:]
save = re.sub(r'\#+.*', '', save, flags=re.MULTILINE)   
save = re.sub(r'(\w+)\s*=\s*(?![\w.]+)',  r"'\1': ", save)
save = re.sub(r'(\w+)\s*=\s*([\w.]+)',  r"'\1': '\2',", save)
save = re.sub(r'(\d\n)',  r"\1,", save)
save = re.sub(r'(\"\n)',  r"\1,", save)
save = save.replace("'',{", '{')
save = save.replace('}', '},')
save = re.sub(r'(?={\s*\w+)({)([\w\s.]+)(})',  r'[\2]', save)
save = re.sub(r'(?<=\w)\s+(?=\w|\-)',  r',', save)
save = re.sub(r'(\d+\.\d\.\d\.\d+)(?!")',  r"'\1'", save)
save = re.sub(r'\[\s*(?=[a-zA-Z])([\w\,]+)',  r"['\1'", save)


save = ast.literal_eval('{' + save)

tech_level = {k: v[0] for k, v in save[0]['GER']['technology'].items()}
tech_level = pd.DataFrame([tech_level]).T
tech_level.rename(columns={0 : 'Tech Level'}, inplace=True)
all_techs_df = pd.DataFrame()

for t in techs:
    df = pd.DataFrame(t).T
    all_techs_df = pd.concat([all_techs_df, df])

tech = pd.merge(all_techs_df,tech_level, left_index=True, right_index=True, how='inner')
tech = tech.apply(pd.to_numeric, errors='ignore')
tech = tech.select_dtypes(include=[np.number]).multiply(tech['Tech Level'], axis = 0)
tech['Tech Level'] = tech['Tech Level'].apply(lambda x : math.sqrt(x))
tech.dropna(how='all', axis=1)

gov = ['head_of_state', 'head_of_government', 'foreign_minister', 'armament_minister', 'minister_of_security', 'minister_of_intelligence', 'chief_of_staff', 'chief_of_army', 'chief_of_navy', 'chief_of_air']
ministers_dict = {k: v for k, v in save[0]['GER'].items() if k in gov}
ministers_dict = {k: people['ministers'].get(v)[k] for k, v in ministers_dict.items()}
economic_effects = pd.merge(left=ministers_df, right=pd.Series(ministers_dict).to_frame(), left_index=True, right_on=0)
# economic_effects.dropna(how='all', axis=1)

laws_dict = {k: v for k, v in save[0]['GER'].items() if k in laws.keys()}
laws_dict2 = {y:laws.get(x).get(y) for x,y in laws_dict.items()}
laws_df = pd.DataFrame(laws_dict2)

economic_effects = pd.concat([economic_effects, laws_df.T])

economic_effects = pd.concat([economic_effects, tech])

reg = {k:v for k, v in regions.items() if v.get('controller') == '"GER"'}
reg = {v.get('strategic_resource').replace('"', ''): k for k, v in reg.items() if v.get('strategic_resource') is not None}
reg = {k: resources.get(k) for k, v in reg.items()}
strategic_resources_df = pd.DataFrame(reg).T
strategic_resources_df = strategic_resources_df.apply(pd.to_numeric, errors='ignore')

economic_effects = pd.concat([economic_effects, strategic_resources_df])

economic_effects.dropna(axis=1, how='all', inplace=True)
economic_effects.loc['global_modifer'] = 1
economic_effects = economic_effects.select_dtypes('number').sum()

economic_effects

reg = {k:v for k, v in regions.items() if v.get('controller') == '"GER"'}
base_ic = sum([v.get('industry')[0] for k, v in reg.items() if v.get('industry') is not None]) + 5

# economic_effects.keys()
# save[0]['GER'].get('Home')
economic_effects['ic_modifier'] * base_ic

aircraft_tech_df = pd.DataFrame(aircraft_tech)
aircraft_doctrine_df = pd.DataFrame(aircraft_doctrine)
armor_tech_df = pd.DataFrame(armor_tech)
arty_tech_df = pd.DataFrame(arty_tech)
buildings_df = pd.DataFrame(buildings)
combined_arms_df = pd.DataFrame(combined_arms)
defines_df = pd.DataFrame(defines)
country_df = defines_df[['country']]
economy_df = defines_df[['economy']]
military_df = defines_df[['military']]
goods_cost_df = defines_df[['goods_cost']]
industry_tech_df = pd.DataFrame(industry_tech)
infantry_tech_df = pd.DataFrame(infantry_tech)
land_doctrine_df = pd.DataFrame(land_doctrine)
laws_df = pd.DataFrame(laws)
ministers_df = pd.DataFrame(minsiters)
static_modifiers_df = pd.DataFrame(static_modifiers)
base_values_df = static_modifiers_df[['base_values']]
naval_doctrine_df = pd.DataFrame(naval_doctrine)
naval_tech_df = pd.DataFrame(naval_tech)
stratgic_resources_df = pd.DataFrame(stratgic_resources)
secret_tech_df = pd.DataFrame(secret_tech)
categories_df = pd.DataFrame(categories)
theories_df = pd.DataFrame(theories)
units_df = pd.DataFrame(units)
all_techs = [aircraft_tech_df.T,aircraft_doctrine_df.T,armor_tech_df.T,arty_tech_df.T,industry_tech_df.T,infantry_tech_df.T,land_doctrine_df.T,naval_doctrine_df.T,naval_tech_df.T,secret_tech_df.T,theories_df.T]
all_techs_df = pd.concat(all_techs)

tech_level = pd.DataFrame([test.get('technology')]).T
tech_level.rename(columns={0 : 'Tech Level'}, inplace=True)
techs = pd.merge(all_techs_df,tech_level, left_index=True, right_index=True, how='inner')
techs = techs.apply(pd.to_numeric, errors='ignore')
techs = techs.select_dtypes(include=[np.number]).multiply(techs['Tech Level'], axis = 0)
techs['Tech Level'] = techs['Tech Level'].apply(lambda x : math.sqrt(x))

economic_effects = ministers_df.T
ministers_dict = {
'head_of_state':'power_hungry_demagogue',
'head_of_government':'silent_workhorse',
'foreign_minister':'great_compromiser',
'armament_minister':'administrative_genius',
'minister_of_security':'man_of_the_people',
'minister_of_intelligence':'dismal_enigma',
'chief_of_staff':'school_of_manoeuvre',
'chief_of_army':'armoured_spearhead_doctrine',
'chief_of_navy':'decisive_naval_battle_doctrine',
'chief_of_air':'air_superiority_doctrine'}
economic_effects = pd.merge(ministers_df.T,pd.DataFrame([ministers_dict]).T, left_index=True, right_on=0, how='inner')
laws_dict = {
'civil_law':'totalitarian_system',
'conscription_law':'two_year_draft',
'economic_law':'war_economy',
'education_investment_law':'big_education_investment',
'industrial_policy_laws':'consumer_product_orientation',
'press_laws':'propaganda_press',
'training_laws':'specialist_training',
}
laws_dict2 = {y:laws.get(x).get(y) for x,y in laws_dict.iteritems()}
laws_df2 = pd.DataFrame(laws_dict2)
economic_effects = economic_effects.append(laws_df2.T)
economic_effects = economic_effects.apply(pd.to_numeric, errors='ignore')
economic_effects.drop(0, axis = 1, inplace=True)
economic_effects = economic_effects.append(techs2)
strategic_resources_df = pd.DataFrame(stratgic_resources)
strat_res = {'aluminium' : raw_input('Aluminum '), 'antibiotics' : raw_input('Antibiotics '),
'automotive_industry' : raw_input('Automotive Industry '), 'ballbearings' : raw_input('Ballbearings '),
'black_soil' : raw_input('Black Soil '), 'cinchona' : raw_input('Cinchona '),
'dockyard_facilities' : raw_input('Dockyard Facilities '), 'fur' : raw_input('Fur '),
'gold' : raw_input('Gold '),'heavy_water' : raw_input('Heavy Water '), 'helium' : raw_input('Helium '),
'horses' : raw_input('Horses '), 'oil_refinery' : raw_input('Oil Refinery '),
'prefab_ship_facilities' : raw_input('Prefab Ship Facilities '), 'rubber' : raw_input('Rubber '), 
'tungsten' : raw_input('Tungsten '), 'uranium' : raw_input('Uranium ')}
strategic_resources_df.loc['Resources'] = pd.Series(strat_res)
strategic_resources_df = strategic_resources_df.T
strategic_resources_df = strategic_resources_df.apply(pd.to_numeric, errors='ignore')
strategic_resources_df = strategic_resources_df.multiply(strategic_resources_df['Resources'], axis = 0)
economic_effects = economic_effects.append(strategic_resources_df)
economic_effects.dropna(axis=1, how='all', inplace=True)
economic_effects.loc['global_modifer'] = 1
economic_effects = economic_effects.sum()

base_ic = 144
actual_ic = (economic_effects['global_ic'] + economic_effects['ic_modifier'] - 1) * base_ic
trade_lp = pd.DataFrame(test)
trade_lp = trade_lp[['home','pool']].dropna(axis = 0, how = 'all')
trade_lp.rename(columns={'home' : 'Produced', 'pool' : 'Stockpile'}, inplace=True)
gc_df2 = goods_cost_df.dropna(axis = 0, how = 'all')
gc_df2.index = gc_df2.index.str.lower()
trade_lp= trade_lp.T.append(gc_df2.T)
trade_lp.loc['Used'] = pd.Series({'metal' : -1,'energy': -2,'rare_materials' : -.5 }) * actual_ic
trade_lp.loc['Converted From'] = pd.Series({'crude_oil' : -.5, 'energy' : (-.05/(.1 + economic_effects['energy_to_oil_conversion'] - 1))}) * actual_ic
trade_lp.loc['Converted To'] = pd.Series({'crude_oil' : .05, 'fuel' : (.5 * economic_effects['refinery_efficiency'])}) * actual_ic
trade_lp.loc['Net Production'] = trade_lp.loc['Net Production'] = trade_lp.loc[['Produced','Used','Converted From','Converted To']].sum(axis=0)

x['Traded'] = pd.Series()
x.set_value('MONEY','Cost',1)
x.T

unit_list = [units.keys()]
empty_df = []
def unit_upgrades(unit):
	x = {y:z.get(unit) for y,z in all_techs_df.iterrows()}
	df = pd.DataFrame(x).T
	df = df.dropna(axis = 0, how='all')
	df = pd.merge(df,tech_level, left_index=True, right_index=True, how='inner')
	df = df.apply(pd.to_numeric, errors='ignore')
	df = df.select_dtypes(include=[np.number]).multiply(df['Tech Level'], axis = 0)
	df['Tech Level'] = df['Tech Level'].apply(lambda x : math.sqrt(x))
	return df
#z = pd.Series(units.get('infantry_brigade'), name = 'Default')
#xx = pd.DataFrame(z)
#xx = xx.T
#df = df.append(xx)
#df = df.apply(pd.to_numeric, errors='ignore')
#df.loc['infantry_brigade'] = df.sum(axis=0)
#df	x = {y:z.get(units) for y,z in all_techs_df.iterrows()}

#x = {y:z.get('infantry_brigade') for y,z in all_techs_df.iterrows()}
#df = pd.DataFrame(x).T
#df = df.dropna(axis = 0, how='all')
#df = pd.merge(df,tech_level, left_index=True, right_index=True, how='inner')
#df = df.apply(pd.to_numeric, errors='ignore')
#df = df.select_dtypes(include=[np.number]).multiply(df['Tech Level'], axis = 0)
#df['Tech Level'] = df['Tech Level'].apply(lambda x : math.sqrt(x))
#z = pd.Series(units.get('infantry_brigade'), name = 'Default')
#xx = pd.DataFrame(z)
#xx = xx.T
#df = df.append(xx)
#df = df.apply(pd.to_numeric, errors='ignore')
#df.loc['infantry_brigade'] = df.sum(axis=0)
#df

x = units_df.T
x[[u'active', u'air_attack', u'air_defence', u'air_detection',
       u'ap_attack', u'armor_value',
       u'build_cost_ic', u'build_cost_manpower',
       u'build_time', u'capital',
       u'combat_width', u'completion_size', u'convoy_attack',
       u'default_morale', u'default_organisation', u'defensiveness', 
       u'distance', 
       u'fuel_consumption', u'hard_attack', u'hull', 
       u'is_buildable', u'max_percentage_of_type',
       u'max_strength', u'maximum_speed', u'minimum_of_type', u'officers', u'on_completion', u'priority',
       u'radio_strength', u'range', u'repair_cost_multiplier',
       u'sea_attack', u'sea_defence', u'shore_bombardment', u'soft_attack',
       u'softness', u'strategic_attack', u'sub_attack',
       u'sub_detection', u'supply_consumption', u'suppression',
       u'surface_defence', u'surface_detection', u'toughness', u'transport',
       u'transport_capability', u'transport_weight', u'type', u'unit_group',
       u'usable_by', u'visibility']]

def ter_atk_base(terrain):
    some_var = {k : categories.get(terrain).get('attack') if units.get(k).get(terrain) is None
    else categories.get(terrain).get('attack') if units.get(k).get(terrain).get('attack') is None 
    else categories.get(terrain).get('attack') + units.get(k).get(terrain).get('attack') for k in units.iterkeys()}
    return some_var

def amp_atk_base(terrain):
    some_var = {k : defines.get('military').get(terrain) if units.get(k).get('river') is None
    else defines.get('military').get(terrain) if units.get(k).get('river').get('attack') is None 
    else defines.get('military').get(terrain) + units.get(k).get('river').get('attack') for k in units.iterkeys()}
    return some_var

def ter_def_base(terrain):
    some_var = {k : None if units.get(k).get(terrain) is None
    else None if units.get(k).get(terrain).get('defence') is None 
    else units.get(k).get(terrain).get('defence') for k in units.iterkeys()}
    return some_var

def amp_def_base(terrain):
    some_var = {k : None if units.get(k).get(terrain) is None
    else None if units.get(k).get(terrain).get('defence') is None 
    else units.get(k).get(terrain).get('defence') for k in units.iterkeys()}
    
terrains = categories.keys()
terrains.remove('ocean')
amp_terrains = ['RIVER_CROSSING_PENALTY','AMPHIBIOUS_LANDING_PENALTY']
terrain_atk_dict = {x : ter_atk_base(x) for x in terrains}
amp_atk_dict = {x : amp_atk_base(x) for x in amp_terrains}
terrains.append('river')
terrains.append('amphibious')
terrain_def_dict = {x : ter_def_base(x) for x in terrains}

terrain_attack_df = pd.concat([pd.DataFrame(terrain_atk_dict),pd.DataFrame(amp_atk_dict)],axis=1)
terrain_defense_df = pd.DataFrame(terrain_def_dict)

