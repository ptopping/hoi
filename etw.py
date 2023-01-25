import pandas as pd
import numpy as np
# import numpy_financial as npf
import itertools
import pulp

class Building(object):
    def __init__(self, building, buildtime, cost, **kwargs):
        self.Building = building
        self.BuildTime = buildtime
        self.Cost = cost
        self.__dict__.update(kwargs)
        
class Faction(object):
    def __init__(self, faction):
        self.faction = faction
        self.df = pd.DataFrame()
        self.df2 = pd.DataFrame()
        
    def add_region(self, name, theater, wealth, growth, highthresh, lowthresh, gov_build, gov_effect, admincost,
                   turnsremaining):
        taxrates = ['Lowest', 'Low', 'Medium', 'High', 'Highest']
        tax_vals = {'Lowest':.05, 'Low':.1, 'Medium':.15, 'High':.2, 'Highest':.25}
        df = pd.DataFrame(np.array(np.meshgrid(taxrates, taxrates)).T.reshape(-1,2),
                          columns=['UpperClassTax', 'LowerClassTax'])
        
#         df.loc[0, 'TaxRate'] = mintax
#         for x in range(1,5):
#             df.loc[x, 'TaxRate'] = df.loc[x-1, 'TaxRate'] + .05
#         for x in range(5,25):
#             df.loc[x, 'TaxRate'] = df.loc[x-5, 'TaxRate'] + .05
        
        df.loc[df['UpperClassTax'] == 'Lowest', 'Growth'] = growth[0]
        df.loc[df['UpperClassTax'] == 'Low', 'Growth'] = growth[1]
        df.loc[df['UpperClassTax'] == 'Medium', 'Growth'] = growth[2]
        df.loc[df['UpperClassTax'] == 'High', 'Growth'] = growth[3]
        df.loc[df['UpperClassTax'] == 'Highest', 'Growth'] = growth[4]
        df['UCTaxRate'] = df['UpperClassTax'].map(tax_vals)
        df['LCTaxRate'] = df['LowerClassTax'].map(tax_vals)
        df['Region'] = name
        df['Theater'] = theater
        df['RegionWealth'] = wealth
        df['GovernmentBuilding'] = gov_build
        df['GovernorsEffect'] = gov_effect
        df['AdministrationCost'] = admincost
        df['TaxRate'] = df[['GovernmentBuilding', 'GovernorsEffect', 'AdministrationCost', 'UCTaxRate',
                            'LCTaxRate']].sum(axis=1)
        if highthresh is not None:
            ndx = taxrates.index(highthresh)
            for v in taxrates[ndx:]:
                df.loc[df['UpperClassTax'] == v, 'TaxRate'] = 0
        if lowthresh is not None:
            ndx = taxrates.index(lowthresh)
            for v in taxrates[ndx:]:
                df.loc[df['LowerClassTax'] == v, 'TaxRate'] = 0
        df['FV'] = -np.fv(0, turnsremaining, df['Growth'], df['RegionWealth'])
        df['AvgTax'] = df[['RegionWealth','FV']].mean(axis=1) * df['TaxRate']
# #         df['FV'] = npf.fv(0, turnsremaining, df['Growth'], df['Region Wealth'])
        self.df = self.df.append(df)
    
    def calc_tax(self):
        df = self.df.copy()
        df = df[['LowerClassTax', 'UpperClassTax', 'Theater', 'AvgTax']].groupby(['LowerClassTax', 'UpperClassTax',
                                                                                  'Theater'])\
                                                                        .sum()
        selection = pulp.LpVariable.dicts("selection",((lotax, hitax, theater) for lotax, hitax, theater in df.index),
                                          cat='Binary')
        model = pulp.LpProblem("Build Order", pulp.LpMaximize)
        model += pulp.lpSum([selection[lotax, hitax, theater]\
                             * df.loc[(lotax, hitax, theater), 'AvgTax'] for lotax, hitax, theater in df.index])
        for theater in df.index.levels[2]:
            model += pulp.lpSum(selection[lotax, hitax, theater] for lotax in df.index.levels[0]\
                                for hitax in df.index.levels[1]) <= 1                
        model.solve()    
        output = []
        for lotax, hitax, region in selection:
            var_output = {'LowTax': lotax, 'HighTax': hitax, 'Region':region,
                          'Selection': selection[(lotax, hitax, region)].varValue,}
            output.append(var_output)
        df2 = pd.DataFrame(output)
        return df2[df2['Selection'] == 1]

    def add_building(self, lowtax, hightax, theater, region, turnsremaining, **kwargs):
        dic = {
            'Theater':theater,
            'Region':region,
            'RegionWealth':self.df.loc[(self.df['Region'] == region) & (self.df['LowerClassTax'] == lowtax)\
                                       & (self.df['UpperClassTax'] == hightax), 'RegionWealth'].iat[0],
            'TaxRate':self.df.loc[(self.df['Region'] == region) & (self.df['LowerClassTax'] == lowtax)\
                                    & (self.df['UpperClassTax'] == hightax), 'TaxRate'].iat[0],
            'Growth':self.df.loc[(self.df['Region'] == region) & (self.df['LowerClassTax'] == lowtax)\
                                   & (self.df['UpperClassTax'] == hightax), 'Growth'].iat[0]
        }
        for k, v in kwargs.items():
            dic['{}'.format(k)] = v

#         df = pd.Series(dic).to_frame().T
        dic['FVTax'] = 0
        dic['FVGrowth'] = 0
        dic['FVWealth'] = 0
        try:
            dic['Tax1'] = -np.fv(0, 1, (dic.get('NewTax') - dic.get('PriorTax'))\
                                * (dic.get('RegionWealth') + dic.get('Growth') * dic.get('BuildTime')), 0)
            dic['TaxFinal'] = -np.fv(0, 1, (dic.get('NewTax') - dic.get('PriorTax'))\
                                     * (dic.get('RegionWealth') + dic.get('Growth') * turnsremaining), 0)
            dic['TaxPMT'] = np.mean([dic.get('Tax1'), dic.get('TaxFinal')])
            dic['FVTax'] = -np.fv(0, turnsremaining - dic.get('BuildTime'), dic.get('TaxPMT'), 0)
        except:
            pass
        try:
            dic['Growth1'] = -np.fv(0, 1, (dic.get('NewGrowth') - dic.get('PriorGrowth')) * dic.get('TaxRate'), 0)
            dic['GrowthFinal'] = -np.fv(0, turnsremaining - dic.get('BuildTime'), (dic.get('NewGrowth')\
                                                                        - dic.get('PriorGrowth'))\
                                                                        * dic.get('TaxRate'), 0)
            dic['GrowthPMT'] = np.mean([dic.get('Growth1'), dic.get('GrowthFinal')])                          
            dic['FVGrowth'] = -np.fv(0, turnsremaining - dic.get('BuildTime'), dic.get('GrowthPMT'), 0)
        except:
            pass
        try:
            dic['WealthPMT'] = (dic.get('NewWealth') - dic.get('PriorWealth')) * dic.get('TaxRate')
            dic['FVWealth'] = -np.fv(0, turnsremaining - dic.get('BuildTime'), dic['WealthPMT'], 0)
        except:
            pass
        try:
            dic['NPV'] = np.npv(0, [-dic.get('Cost'), dic.get('FVTax'), dic.get('FVGrowth'), dic.get('FVWealth')])
        except:
            pass
        try:
            if dic.get('NPV') >= 1:
                dic['NPVRate'] = dic.get('NPV') / dic.get('Cost')
            else:
                dic['NPVRate'] = 0
        except:
            pass
        df = pd.Series(dic).to_frame().T
        self.df2 = self.df2.append(df)

    def build_order(self, fundsavailable):
        df = self.df2.copy()
        df = df.set_index(['Region','Building'])
        df.fillna(0, inplace=True)
        selection = pulp.LpVariable.dicts("selection",((region, building) for region, building in df.index),cat='Binary')
        model = pulp.LpProblem("Build Order", pulp.LpMaximize)
        model += pulp.lpSum([selection[region, building]\
                             * df.loc[(region, building), 'NPVRate'] for region, building in df.index])
        model += pulp.lpSum([selection[region, building]\
                             * df.loc[(region, building), 'Cost'] for region, building in df.index]) <= fundsavailable
        model.solve()
        output = []
        for region, building in selection:
            var_output = {'Region': region, 'Building': building, 'Selection': selection[(region, building)].varValue,}
            output.append(var_output)
        df2 = pd.DataFrame(output)
        df2 = df2[df2['Selection'] == 1]
        df2 = df2.merge(self.df2[['Region', 'Building', 'Cost', 'NPVRate']], left_on=['Region', 'Building'],
                        right_on=['Region', 'Building'])
        df2['Cost'] = df2['Cost'].apply(pd.to_numeric)
        return df2.append(df2.sum(numeric_only=True), ignore_index=True)
# pd.options.display.max_columns = 35

governorsresidence = Building("Governor's Residence", 3, 1000, PriorTax=0, NewTax=.03)
governorsmansion = Building("Governor's Mansion", 4, 2000, PriorTax=.03, NewTax=.06)
governorspalace = Building("Governor's Mansion", 5, 3000, PriorTax=.06, NewTax=.09)
royalpalace = Building('Royal Palace', 6, 4500, PriorTax=.09, NewTax=.12)
imperialpalace = Building('Imperial Palace', 7, 6000, PriorTax=.12, NewTax=.15)
conservatorium = Building('Conservatorium', 2, 750, PriorGrowth=0, NewGrowth=1)
operahouse = Building('Opera House', 3, 1000, PriorGrowth=1, NewGrowth=2)
grandoperahouse = Building('Grand Opera House', 4, 1500, PriorGrowth=2, NewGrowth=3)
royalobservatory = Building('Royal Observatory', 4, 2500, PriorGrowth=2, NewGrowth=8)
greatmuseum = Building('Great Museum', 5, 3500, PriorGrowth=3, NewGrowth=4)
royalacademy = Building('Royal Academy', 5, 3500, PriorGrowth=8, NewGrowth=12)
berlinacademy = Building('Royal Academy', 8, 10000, PriorGrowth=8, NewGrowth=12)
peasantfarms = Building('Peasant Farms', 1, 300)
tenantedfarms = Building('Tenanted Farms', 2, 500)
# ironmine = Building('Iron Mine')
steammine = Building('Steam-Pumped Iron Mine', 3, 2000)
# industrialmine = Building('Industrial Iron Mining Complex', 3, 2000)
# clearances = Building('Clearances', 2, 500)
# tenantedfarms = Building('Great Estates', 2, 500)
# tenantedfarms = Building('Palatial Estate', 2, 500)
localfishery = Building('Local Fishery', 2, 600)
fishingfleet = Building('Fishing Fleet', 3, 900)
majorfishery = Building('Major Fishery', 4, 1200)
tradingport = Building('Trading Port', 2, 1250, PriorGrowth=0, NewGrowth=1)
commercialport = Building('Commercial Port', 3, 2500, PriorGrowth=1, NewGrowth=3)
commercialbasin = Building('Commercial Basin', 4, 5000, PriorGrowth=3, NewGrowth=5)
globaltradingcompany = Building('Global Trading Company', 5, 10000, PriorGrowth=5, NewGrowth=7)
weavers = Building('Craft Workshops(Weavers)', 2, 1000, PriorGrowth=0, NewGrowth=7)
weaverscottage = Building("Weaver's Cottage", 3, 2000, PriorGrowth=7, NewGrowth=10)
watermill = Building('Water-Powered Cloth Mill', 4, 4000, PriorGrowth=10, NewGrowth=13)
steammill = Building('Steam-Powered Cloth Mill', 6, 6000, PriorGrowth=13, NewGrowth=16)
basicroads = Building('Basic Roads', 2, 750, PriorGrowth=0, NewGrowth=3)
cobbledroads = Building('Cobbled Roads', 3, 1500, PriorGrowth=3, NewGrowth=4)
# metalledroads = Building('Metalled Roads', 6, 6000, PriorGrowth=4, NewGrowth=5)

# governorsresidence = governorsresidence.__dict__
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **governorsresidence.__dict__)
# prussia.df2

prussia = Faction('Prussia')
year = 1703
winter = True
turnsremaining = (1800 - year) * 2 - winter
prussia.add_region(name='Brandenburg',
                   theater='Europe',
                   wealth=5837,
                   growth=[13, 9, 2, -12, -35],
                   highthresh = None,
                   lowthresh='Highest',
                   gov_build=.12,
                   gov_effect=.02,
                   admincost=0,
                   turnsremaining=turnsremaining)
prussia.add_region(name='Saxony',
                   theater='Europe',
                   wealth=2010,
                   growth=[3, 0, -5, -15, -33],
                   highthresh='Highest',
                   lowthresh='High',
                   gov_build=.00,
                   gov_effect=.02,
                   admincost=0,
                   turnsremaining=turnsremaining)
prussia.add_region(name='West Prussia',
                   theater='Europe',
                   wealth=1275,
                   growth=[7, 4, -2, -14, -34],
                   highthresh='Highest',
                   lowthresh='Medium',
                   gov_build=.00,
                   gov_effect=.02,
                   admincost=0,
                   turnsremaining=turnsremaining)
prussia.add_region(name='East Prussia',
                   theater='Europe',
                   wealth=4547,
                   growth=[12, 8, 1, -13, -35],
                   highthresh=None,
                   lowthresh=None,
                   gov_build=.09,
                   gov_effect=.02,
                   admincost=0,
                   turnsremaining=turnsremaining)
# prussia.add_region(name='Poland',
#                    theater='Europe',
#                    wealth=2625,
#                    growth=[14, 10, 3, -12, -35],
#                    highthresh='High',
#                    lowthresh=None,
#                    mintax=.169,
#                    turnsremaining=turnsremaining)
prussia.df
prussia.calc_tax()

lowtax = prussia.calc_tax().iloc[0,0]
hightax = prussia.calc_tax().iloc[0,1]

# Brandenburg
prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
                     **imperialpalace.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **royalobservatory.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **tenantedfarms.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **tenantedfarms.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **commercialport.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **watermill.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Brandenburg', turnsremaining=turnsremaining,
#                      **cobbledroads.__dict__)

# Saxony
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Saxony', turnsremaining=turnsremaining,
#                      **governorspalace.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Saxony', turnsremaining=turnsremaining,
#                      **grandoperahouse.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Saxony', turnsremaining=turnsremaining,
#                      **tenantedfarms.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Saxony', turnsremaining=turnsremaining,
#                      **steammine.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Saxony', turnsremaining=turnsremaining,
#                      **cobbledroads.__dict__)

# West Prussia
prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='West Prussia', turnsremaining=turnsremaining,
                     **governorsresidence.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='West Prussia', turnsremaining=turnsremaining,
#                      PriorWealth=0, NewWealth=175, **tenantedfarms.__dict__)
prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='West Prussia', turnsremaining=turnsremaining,
                     PriorWealth=600, NewWealth=900, **weaverscottage.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='West Prussia', turnsremaining=turnsremaining,
#                      **cobbledroads.__dict__)

# East Prussia
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='East Prussia', turnsremaining=turnsremaining,
#                      **grandoperahouse.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='East Prussia', turnsremaining=turnsremaining,
#                      PriorWealth=0, NewWealth=175, **tenantedfarms.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='East Prussia', turnsremaining=turnsremaining,
#                      PriorWealth=525, NewWealth=787, **weaverscottage.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='East Prussia', turnsremaining=turnsremaining,
#                      **cobbledroads.__dict__)

# Poland
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Poland', turnsremaining=turnsremaining,
#                      **governorspalace.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Poland', turnsremaining=turnsremaining,
#                      **royalobservatory.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Poland', turnsremaining=turnsremaining,
#                      **tenantedfarms.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Poland', turnsremaining=turnsremaining,
#                      **tenantedfarms.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Poland', turnsremaining=turnsremaining,
#                      **weaverscottage.__dict__)
# prussia.add_building(lowtax=lowtax, hightax=hightax, theater='Europe', region='Poland', turnsremaining=turnsremaining,
#                      **cobbledroads.__dict__)
prussia.df2

